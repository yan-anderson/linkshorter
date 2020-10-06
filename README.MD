# Short link, please!

Link shorter project

### Documentation
Swagger - load swagger.yaml from project

Postman - https://documenter.getpostman.com/view/5643963/TVRha8t1

### Running

Setup ``src/.env`` file, specify config type:
    
- local - for local running
- test - for test running
- docker - for docker running

```
CONFIG=local
```

Setup selected config in ``src/config/``

- local_config.py
- test_config.py
- docker_config.oy

And run Flask

```
python src/app.py
```

## Running tests

Set config and run

```
pytest src/app.py
```

## Running Docker

Set ``CONFIG=docker`` in ``src/.env``

```
docker-compose build -v
docker-compose up -d
```