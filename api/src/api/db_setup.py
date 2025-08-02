from fastapi import APIRouter, HTTPException

from src.dto.api_response import ResponseSchema
from src.core.exceptions import APIException
from src.databases.dependencies import AsyncSessionDep
from src.init import (
    db_01_create_all,
    db_02_books
)

router = APIRouter(tags=["Database - setup"])

@router.post(
    path="/databases/setup",
    name="Reset and Setup Database",
    description="Drop and Create all metadata. Initializing the database with initial data."
)
async def db_setup(session: AsyncSessionDep):
    try:
        await db_01_create_all.setup_database(session)
        await db_02_books.insert_books(session)
    except Exception as exp:
        raise APIException(
            type="db",
            detail=str(exp)
        )

    return ResponseSchema[str](detail="DB created")