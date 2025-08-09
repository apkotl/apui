from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.databases.dependencies import get_async_session

from .service_db_01_create_all import setup_database
from .service_db_02_books import insert_books
from .service_db_03_auth import insert_users





class DbService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def setup_database(self) -> None:
        await setup_database(self.session)

    async def insert_data(self) -> None:
        await insert_books(self.session)
        await insert_users(self.session)



def get_db_service(session: AsyncSession = Depends(get_async_session)) -> DbService:
    return DbService(session)