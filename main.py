from fastapi import Body, FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola Mundo! desde FASTAPI"}


@app.get("/post")
def get_post():
    return {"data" : "post data"}


@app.post("/create_post")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"message": "post created!"}