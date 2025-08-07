from fastapi import APIRouter, Depends

from src.core.schemas import ResponseSchema
from src.core.exceptions import APIException

from .service import get_db_service, DbService

router = APIRouter(tags=["database_setup"])

@router.post(
    path="/databases/setup",
    name="Reset and Setup Database",
    description="Drop and Create all metadata. Initializing the database with initial data."
)
async def db_setup(service: DbService = Depends(get_db_service)):
    try:
        await service.setup_database()
        await service.insert_data()
    except Exception as exp:
        raise APIException(
            type="db",
            detail=str(exp)
        )

    return ResponseSchema[str](detail="DB created")