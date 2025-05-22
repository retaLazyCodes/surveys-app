from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from src.infrastructure.db.session import get_db


router = APIRouter()


@router.get("/db-check", summary="Test DB connection")
async def db_check(session: AsyncSession = Depends(get_db)):
    try:
        await session.execute(text("SELECT 1"))
        return {"status": "ok", "message": "Database connection successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")
