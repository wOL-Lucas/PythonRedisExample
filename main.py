from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import redis
import os
from dotenv import load_dotenv

load_dotenv()
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PASS = os.getenv("REDIS_PASS")


def get_redis():
    try:
        r = redis.Redis(
            host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASS, decode_responses=True
        )
        yield r
    except redis.RedisError as e:
        raise HTTPException(status_code=500, detail=str(e))


class Notification(BaseModel):
    to: str
    message: str


app = FastAPI()


@app.post("/notify")
def notify(notification: Notification, r: redis.Redis = Depends(get_redis)):
    try:
        r.lpush(notification.to, notification.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": "success"}


@app.get("/notifications/{to}")
def notifications(to: str, r: redis.Redis = Depends(get_redis)) -> list:
    try:
        messages = r.lrange(to, 0, -1)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return messages
