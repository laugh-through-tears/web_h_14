from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models, database, users, contacts
from .config import settings
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import aioredis

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    redis = await aioredis.create_redis_pool(settings.REDIS_URL)
    await FastAPILimiter.init(redis)

models.Base.metadata.create_all(bind=database.engine)

app.include_router(users.router)
app.include_router(contacts.router)

@app.get("/", tags=["Root"])
async def read_root():
    """
    Повертає привітальне повідомлення.
    """
    return {"message": "Welcome to the Contacts API"}
