# News App built with Fastapi and React

This app has been deployed to https://fastapi-news-app.herokuapp.com/

To run this app, you need to have [Docker](https://www.docker.com/) installed on your machine.

## Initialiation

Create a `.env` file in the root of the project with the following content:

```
NEWS_API_KEY=yourNewsApiKey
```

Change `yourNewsApiKey` with your own [news API](https://newsapi.org/) key.

## Run the app

If you want to run the app locally, you can do it with the following command:

```
docker build -t fastapi-news-app .
docker run -d --name fastapi-news-app -p 80:80 --env NEWS_API_KEY=yourNewsApiKey fastapi-news-app 
```

Or you can develop locally with the following command in the split terminal:

- For the backend (I do the local with poetry, but you can go to `server/requirements.txt` to `pip install` them)
```
poetry install
uvicorn server.app:app --reload
```
- For the frontend
```
cd client
yarn install
yarn start
```