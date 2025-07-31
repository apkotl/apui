#from redis import Redis
import redis.asyncio as redis_async

from fastapi import HTTPException, Depends, APIRouter
from pydantic import BaseModel
from typing import Optional, Dict, Any


from src.config.logging import get_logger



# Pydantic модели для запросов
class SetValueRequest(BaseModel):
    key: str
    value: str
    expire: Optional[int] = None  # TTL в секундах


class ListAddRequest(BaseModel):
    key: str
    value: str
    max_size: Optional[int] = 100


class HashSetRequest(BaseModel):
    key: str
    field: str
    value: str



# Dependency для получения Redis клиента
async def get_redis():
    from src.app_factory import redis_client
    return redis_client


router = APIRouter(prefix="/redis", tags=["Redis"])
logger = get_logger('app.api.redis')

# === БАЗОВЫЕ ОПЕРАЦИИ СО СТРОКАМИ ===

@router.post("/set")
async def set_value(request: SetValueRequest, redis: redis_async.Redis = Depends(get_redis)):
    """Установить значение ключа с опциональным TTL"""
    try:
        if request.expire:
            await redis.setex(request.key, request.expire, request.value)
        else:
            await redis.set(request.key, request.value)
        return {"success": True, "message": f"Key '{request.key}' set successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get/{key}")
async def get_value(key: str, redis: redis_async.Redis = Depends(get_redis)):
    """Получить значение по ключу"""
    try:
        value = await redis.get(key)
        if value is None:
            raise HTTPException(status_code=404, detail="Key not found")
        return {"key": key, "value": value}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete/{key}")
async def delete_key(key: str, redis: redis_async.Redis = Depends(get_redis)):
    """Удалить ключ"""
    try:
        deleted = await redis.delete(key)
        if deleted == 0:
            raise HTTPException(status_code=404, detail="Key not found")
        return {"success": True, "message": f"Key '{key}' deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# === ОПЕРАЦИИ СО СПИСКАМИ ===

@router.post("/list/add")
async def add_to_list(request: ListAddRequest, redis: redis_async.Redis = Depends(get_redis)):
    """Добавить элемент в список с ограничением размера"""
    try:
        # Добавляем в начало списка
        await redis.lpush(request.key, request.value)
        # Ограничиваем размер списка
        if request.max_size:
            await redis.ltrim(request.key, 0, request.max_size - 1)

        list_size = await redis.llen(request.key)
        return {
            "success": True,
            "message": "Element added to list",
            "list_size": list_size
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/list/{key}")
async def get_list(key: str, start: int = 0, end: int = -1, redis: redis_async.Redis = Depends(get_redis)):
    """Получить элементы списка"""
    try:
        items = await redis.lrange(key, start, end)
        list_size = await redis.llen(key)
        return {
            "key": key,
            "items": items,
            "total_size": list_size,
            "showing": f"{start} to {end if end != -1 else list_size}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# === ОПЕРАЦИИ С ХЕШАМИ ===

@router.post("/hash/set")
async def set_hash_field(request: HashSetRequest, redis: redis_async.Redis = Depends(get_redis)):
    """Установить поле в хеше"""
    try:
        await redis.hset(request.key, request.field, request.value)
        return {
            "success": True,
            "message": f"Field '{request.field}' set in hash '{request.key}'"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/hash/{key}")
async def get_hash(key: str, redis: redis_async.Redis = Depends(get_redis)):
    """Получить все поля хеша"""
    try:
        hash_data = await redis.hgetall(key)
        if not hash_data:
            raise HTTPException(status_code=404, detail="Hash not found")
        return {"key": key, "data": hash_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/hash/{key}/{field}")
async def get_hash_field(key: str, field: str, redis: redis_async.Redis = Depends(get_redis)):
    """Получить конкретное поле хеша"""
    try:
        value = await redis.hget(key, field)
        if value is None:
            raise HTTPException(status_code=404, detail="Field not found")
        return {"key": key, "field": field, "value": value}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# === ИНФОРМАЦИОННЫЕ ЭНДПОИНТЫ ===

@router.get("/keys")
async def get_keys(pattern: str = "*", redis: redis_async.Redis = Depends(get_redis)):
    """Получить список ключей по паттерну"""
    try:
        keys = await redis.keys(pattern)
        return {"pattern": pattern, "keys": keys, "count": len(keys)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/info/{key}")
async def get_key_info(key: str, redis: redis_async.Redis = Depends(get_redis)):
    """Получить информацию о ключе"""
    try:
        exists = await redis.exists(key)
        if not exists:
            raise HTTPException(status_code=404, detail="Key not found")

        key_type = await redis.type(key)
        ttl = await redis.ttl(key)

        return {
            "key": key,
            "type": key_type,
            "ttl": ttl if ttl > 0 else "no expiration",
            "exists": bool(exists)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# === СЛУЖЕБНЫЕ ЭНДПОИНТЫ ===

@router.get("/ping")
async def ping_redis(redis: redis_async.Redis = Depends(get_redis)):
    """Проверить соединение с Redis"""
    try:
        pong = await redis.ping()
        return {"status": "connected", "response": pong}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Redis connection failed: {str(e)}")


@router.get("/stats")
async def get_redis_stats(redis: redis_async.Redis = Depends(get_redis)):
    """Получить статистику Redis"""
    try:
        info = await redis.info()
        db_size = await redis.dbsize()
        return {
            "database_size": db_size,
            "redis_version": info.get("redis_version"),
            "used_memory": info.get("used_memory_human"),
            "connected_clients": info.get("connected_clients"),
            "uptime_seconds": info.get("uptime_in_seconds")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Главная страница с документацией
@router.get("/endpoints")
async def root():
    return {
        "message": "Redis FastAPI Integration",
        "endpoints": {
            "docs": "/docs",
            "set_value": "POST /redis/set",
            "get_value": "GET /redis/get/{key}",
            "add_to_list": "POST /redis/list/add",
            "get_list": "GET /redis/list/{key}",
            "set_hash": "POST /redis/hash/set",
            "get_hash": "GET /redis/hash/{key}",
            "ping": "GET /redis/ping"
        }
    }