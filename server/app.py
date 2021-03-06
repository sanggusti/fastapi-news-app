import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .api.news_api import get_news_articles

DIR = os.path.dirname(__file__)


class SearchRequest(BaseModel):
    q: str
    from_date: str


app = FastAPI()

app.mount(
    "/static", StaticFiles(directory=f"{DIR}/../client/build/static"), name="static"
)


@app.get("/")
async def index():
    """Return application index."""
    return FileResponse(f"{DIR}/../client/build/index.html")


@app.post("/api/search")
async def search(req: SearchRequest):
    """Return news articles for a search query and from_date

    Args:
        req (SearchRequest): a request string
    """
    return get_news_articles(q=req.q, from_date=req.from_date)
