from fastapi import FastAPI
from pydantic import BaseModel
from .api.news_api import get_news_articles


class SearchRequest(BaseModel):
    q: str
    from_date: str


app = FastAPI()


@app.post("/api/search")
async def search(req: SearchRequest):
    """Return news articles for a search query and from_date

    Args:
        req (SearchRequest): a request string
    """
    return get_news_articles(q=req.q, from_date=req.from_date)
