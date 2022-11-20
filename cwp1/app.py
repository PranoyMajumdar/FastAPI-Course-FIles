from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def homepage():
    return {"message": 'Hello World!'}

@app.post('/add')
async def add(x: int, y:int):
    return {"answer": x+y}