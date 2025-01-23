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


@app.get("/posts")
def get_posts():
    return {"data" : "post data"}


@app.post("/posts")
async def create_posts(post: Post):
    return { "data" : post.model_dump()}
    