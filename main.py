from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def root():
    return {"data": "This is your posts"}

@app.post("/createposts")
async def root(new_Post: Post):
    print(new_Post)
    return {"new_post": "new_post"}

