from fastapi import APIRouter, Depends

from src.core.schemas import ResponseSchema
from src.core.exceptions import APIException

from .service import ServiceDbDep

router = APIRouter(tags=["database_setup"])

@router.post(
    path="/databases/setup",
    name="Reset and Setup Database",
    description="Drop and Create all metadata. Initializing the database with initial data."
)
async def db_setup(service: ServiceDbDep):
    try:
        await service.setup_database()
        await service.insert_books()
    except Exception as exp:
        raise APIException(
            type="db",
            detail=str(exp)
        )

    return ResponseSchema[str](detail="DB created")