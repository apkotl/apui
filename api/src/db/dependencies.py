from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.core import AsyncSessionFactory


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