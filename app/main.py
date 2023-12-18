from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

mypost = [
    {"title": "My first post", "content": "This is my first post",
        "published": False, "rating": None, "id": 1},
    {"title": "My second post", "content": "This is my second post",
        "published": True, "rating": 5, "id": 2},
    {"title": "My third post", "content": "This is my third post",
        "published": False, "rating": None, "id": 3},
    {"title": "My fourth post", "content": "This is my fourth post",
        "published": True, "rating": 4, "id": 4},
    {"title": "My fifth post", "content": "This is my fifth post",
        "published": False, "rating": None, "id": 5},
    {"title": "My sixth post", "content": "This is my sixth post",
        "published": True, "rating": 3, "id": 6},
    {"title": "My seventh post", "content": "This is my seventh post",
        "published": False, "rating": None, "id": 7},
    {"title": "My eighth post", "content": "This is my eighth post",
        "published": True, "rating": 2, "id": 8},
    {"title": "My ninth post", "content": "This is my ninth post",
        "published": False, "rating": None, "id": 9},
    {"title": "My tenth post", "content": "This is my tenth post",
        "published": True, "rating": 1, "id": 10},
    {"title": "My eleventh post", "content": "This is my eleventh post",
        "published": False, "rating": None, "id": 11},
    {"title": "My twelfth post", "content": "This is my twelfth post",
        "published": True, "rating": 0, "id": 12},
    {"title": "My thirteenth post", "content": "This is my thirteenth post",
        "published": False, "rating": None, "id": 13},
    {"title": "My fourteenth post", "content": "This is my fourteenth post",
        "published": True, "rating": -1, "id": 14},
    {"title": "My fifteenth post", "content": "This is my fifteenth post",
        "published": False, "rating": None, "id": 15},
    {"title": "My sixteenth post", "content": "This is my sixteenth post",
        "published": True, "rating": -2, "id": 16}

]


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def root():
    return {"data": mypost}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def root(post: Post):
    post_dict = post.dict()
    post_dict["id"] = len(mypost) + 1
    mypost.append(post_dict)
    return {"post": post_dict}


@app.get("/posts/{id}")
async def get_post(id: int, response: Response):

    if id >= len(mypost) or id < 0:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "post not found"}
    else:
        return {"post": mypost[id]}


@app.delete("/posts/{id}")
async def delete_post(id: int):
    if id >= len(mypost) or id < 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    else:
        del mypost[id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
async def update_post(id: int, post: Post):
    if id >= len(mypost) or id < 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    else:
        post_dict = post.dict()
        post_dict["id"] = id
        mypost[id] = post_dict
        return {"post": post_dict}
