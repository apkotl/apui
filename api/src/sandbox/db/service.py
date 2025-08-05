from typing import Annotated

from fastapi import Depends

from src.databases.dependencies import AsyncSessionDep

from .service_db_01_create_all import setup_database
from .service_db_02_books import insert_books





class ServiceDb:
    def __init__(self, session: AsyncSessionDep):
        self.session = session

    async def setup_database(self) -> None:
        await setup_database(self.session)

    async def insert_data(self) -> None:
        await insert_books(self.session)





def get_service_db(session: AsyncSessionDep) -> ServiceDb:
    return ServiceDb(session)

ServiceDbDep = Annotated[ServiceDb, Depends(get_service_db)]