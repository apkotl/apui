from fastapi import APIRouter

from src.db.setup import setup_database
from src.db.dependencies import AsyncSessionDep


router = APIRouter(tags=["Database - setup"])

@router.post(
    path="/db/setup",
    name="Reset and Setup Database",
    description="Drop and Create all metadata. Initializing the database with initial data."
)
async def db_setup(session: AsyncSessionDep):
    await setup_database(session)
    return {'data': 'success'}