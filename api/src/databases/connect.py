import asyncio
import redis.asyncio as redis

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.databases.config import DATABASE_CONFIG, REDIS_CONFIG


# PostgresSQL
engine = create_async_engine(
    url=DATABASE_CONFIG['url'],
    echo=True,
    pool_size=DATABASE_CONFIG['pool_size'],
    max_overflow=DATABASE_CONFIG['max_overflow'],
)

AsyncSessionFactory = async_sessionmaker(engine, expire_on_commit=False)


# Redis
class RedisManager:
    def __init__(self, config: dict):
        self.config = config
        #self.pool: Optional[redis.ConnectionPool] = None
        self.pool: redis.ConnectionPool | None = None
        self._lock = asyncio.Lock()

    async def init_pool(self):
        """Lazy pool initialization"""
        if self.pool is None:
            async with self._lock:
                if self.pool is None:
                    self.pool = redis.ConnectionPool.from_url(
                        self.config['url'],
                        encoding=self.config.get('encoding', 'utf-8'),
                        decode_responses=self.config.get('decode_responses', True),
                        max_connections=self.config.get('max_connections', 20),
                        retry_on_timeout=self.config.get('retry_on_timeout', True),
                        socket_timeout=self.config.get('socket_timeout', 5),
                        socket_connect_timeout=self.config.get('socket_connect_timeout', 5),
                    )

    async def get_client(self) -> redis.Redis:
        """Connect Redis Client"""
        await self.init_pool()
        return redis.Redis(connection_pool=self.pool)

    async def close(self):
        """Close connection pool"""
        if self.pool:
            await self.pool.disconnect()
            self.pool = None

    async def health_check(self) -> bool:
        """Check Redis State"""
        try:
            client = await self.get_client()
            await client.ping()
            await client.close()
            return True
        except Exception:
            return False

redis_manager = RedisManager(REDIS_CONFIG)