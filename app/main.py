from fastapi import FastAPI
from .routers.users import router as UserRouter
from .routers.categories import router as CategoryRouter


app = FastAPI()

app.include_router(UserRouter)
app.include_router(CategoryRouter)


@app.get("/")
def read_root():
    return {"message": "Hello World"}
