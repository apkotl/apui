from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import main_router
from src.config import CORS_CONFIG


# Create Application
app = FastAPI()

# Include Main Router
app.include_router(main_router)

# Add CORS configuration
app.add_middleware(CORSMiddleware, **CORS_CONFIG)

