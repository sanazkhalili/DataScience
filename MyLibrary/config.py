from fastapi import FastAPI
from routers import endpoint

app = FastAPI()

app.include_router(endpoint.route ,tags=['mybook'])