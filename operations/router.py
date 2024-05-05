from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from models.models import currency

currencies_router = APIRouter(prefix="/currencies", tags=["currency"])


@currencies_router.get("/")
async def get_currencies(session: AsyncSession = Depends(get_async_session)):
    query = select(currency)
    print(query)
    currencies = await session.execute(query)
    return currencies.mappings().all()
