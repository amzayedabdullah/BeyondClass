from fastapi import APIRouter
from app.api.v1 import auth

api_router = APIRouter()

# Include auth endpoints
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
