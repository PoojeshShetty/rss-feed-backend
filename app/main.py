from fastapi import FastAPI
from .routers.users import router as UserRouter
from .routers.categories import router as CategoryRouter
from .routers.rss_feeds import router as RssFeedRouter


app = FastAPI()

app.include_router(UserRouter)
app.include_router(CategoryRouter)
app.include_router(RssFeedRouter)

@app.get("/")
def read_root():
    return {"message": "Hello World"}
