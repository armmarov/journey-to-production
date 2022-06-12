# Flask API Server

## To initially setup the environment
```
> python3.8 -m venv venv
> source venv/bin/activate
> pip install --upgrade pip
> pip install -r requirements.txt
```

## To run the server
```
> flask run
```

## To open the swagger document
```
1. Open the browser
2. Open the url http://localhost:5000/apidocs
```

## To run health check
```
> flask run
> curl localhost:5000/health
```
