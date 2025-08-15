from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.users import router as UserRouter
from .routers.categories import router as CategoryRouter
from .routers.rss_feeds import router as RssFeedRouter
from .routers.blog_posts import router as BlogPostRouter

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UserRouter)
app.include_router(CategoryRouter)
app.include_router(RssFeedRouter)
app.include_router(BlogPostRouter)

@app.get("/")
def read_root():
    return {"message": "Hello World"}
