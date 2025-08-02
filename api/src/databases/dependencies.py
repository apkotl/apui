from typing import Annotated, AsyncGenerator

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
import redis.asyncio as redis

from src.databases.connect import AsyncSessionFactory, redis_manager


# PostgresSQL
async def get_async_session():
    async with AsyncSessionFactory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

AsyncSessionDep = Annotated[AsyncSession, Depends(get_async_session)]


# Redis
async def get_redis_client() -> AsyncGenerator[redis.Redis, None]:
    """Dependency for getting Redis Client"""
    client = await redis_manager.get_client()
    try:
        yield client
    #except Exception:
    #    raise
    finally:
        await client.close()

AsyncRedisClientDep = Annotated[redis.Redis, Depends(get_redis_client)]
