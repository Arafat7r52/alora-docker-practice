from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host='redis', port=6379)

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.get('/')
def root():
    return {'message': 'Alora Giving API'}

@app.get('/version')
def version():
    return {'version': '1.0.0'}

@app.get('/counter')
def counter():
    r.incr('visits')
    return {'visits': int(r.get('visits'))}