from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from microservice 2"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"This is Hello {name}"}
