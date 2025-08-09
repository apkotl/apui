from fastapi import FastAPI, APIRouter


from src.auth.router import router as auth_router
from src.sandbox.info.router import router as info_router
from src.sandbox.db.router import router as db_router
from src.sandbox.redis.router import router as redis_router

from src.art.router import router as art_router





def apply_routers(app: FastAPI) -> FastAPI:
    router_v1 = APIRouter(prefix="/v1")
    router_v2 = APIRouter(prefix="/v2")

    router_v1.include_router(art_router)

    router_v1.include_router(info_router)
    router_v1.include_router(db_router)
    router_v1.include_router(redis_router)
    app.include_router(router_v1)

    router_v2.include_router(db_router)
    app.include_router(router_v2)


    #app.include_router(redis_router)
    #app.include_router(info_router)
    app.include_router(auth_router)
    #app.include_router(info_router)
    #app.include_router(db_setup_router)
    #app.include_router(books_router)
    return app



