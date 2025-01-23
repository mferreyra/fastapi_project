from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    is_public: bool = True #* este parámetro asi definido por defecto es verdadero
    rating: Optional[int] = None #* este parámetro asi definido es opcional y por defecto es nulo (from typing import Optional)

@app.get("/")
async def root():
    return {"message": "Hola Mundo! desde FASTAPI"}


@app.get("/post")
def get_post():
    return {"data" : "post data"}


@app.post("/create_post")
async def create_post(post: Post):
    #print(post)
    #return {"t": post.title, "c": post.content, "p": post.is_public, "r": post.rating}
    return post.model_dump()
    #return { "data" : post.model_dump()}
    #return post.model_dump_json()