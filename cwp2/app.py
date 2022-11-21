from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return {"message": 'Hello FastAPI!'}


database = ['pranoy', 'rohit', 'rakesh']

@app.get('/user/{username}')
async def user(username: str):
    if username in database:
        return {"message": f'Yes, {username} is exist on database!'}
    
    return {"message": f"{username} not exist on database!"}
