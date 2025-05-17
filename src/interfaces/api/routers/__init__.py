from fastapi import APIRouter

from .health import router as health_router
from .db_check import router as db_check

router = APIRouter()
router.include_router(health_router)
router.include_router(db_check)

__all__ = ["router"]