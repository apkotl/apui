from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.models import BaseOrm


async def setup_database(session: AsyncSession):
    await reset_schema(session, "art")

    async with session.bind.begin() as conn:
        await conn.run_sync(lambda sync_conn: BaseOrm.metadata.drop_all(sync_conn, checkfirst=True))
        await conn.run_sync(lambda sync_conn: BaseOrm.metadata.create_all(sync_conn))


async def reset_schema(session: AsyncSession, schema_name: str):
    async with session.bind.begin() as conn:
        await conn.execute(text(f"DROP SCHEMA IF EXISTS {schema_name} CASCADE"))
        await conn.execute(text(f"CREATE SCHEMA {schema_name}"))

