# Storing and Retrieving Data with Redis and Python
## A FastAPI example for managing data in Redis
<div>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/redis/redis-original.svg" width=50/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg" width=50/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width=50/>
</div>               

## First steps:
### Up the redis service:
```docker-compose up -d```

### Then install dependencies:
```pip install -r requirements.txt```

### Finally run the example:
```uvicorn main:app --port 5000```

### POST 'localhost:5000/notify' to Create data: 
req body:
```
  {
    "to":"Lucas",
    "message":"Hello world!"
  }
```

### GET 'localhost:5000/notifications/Lucas' to Retrieve data:
returns
```
  [
    "Hello world!"
  ]
```
