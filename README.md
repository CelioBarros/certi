# certi

I develop this app with python using Flask framework.

## Run without Docker
### To execute this app need
- install python 3.7
- install pip3
- install flask

#### To run app
```
python3 app/router.py
```

#### To run tests
```
python3 tests/function_test.py
```

## Run with Docker

```
docker build -t certi .
docker run -d -p 3000:3000 certi
```
