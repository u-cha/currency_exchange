from typing import Annotated

from fastapi import APIRouter, Depends, Path
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from models.models import currency

currencies_router = APIRouter(prefix="/currencies", tags=["currency"])
currency_router = APIRouter(prefix="/currency", tags=["currency"])


@currencies_router.get("/")
async def get_currencies(session: AsyncSession = Depends(get_async_session)):
    query = select(currency)
    print(query)
    currencies = await session.execute(query)
    return currencies.mappings().all()


@currency_router.get("/{currency_code}")
async def get_currency(
    currency_code: Annotated[
        str, Path(min_length=3, max_length=3, title="Currency Code to look_up")
    ],
    session: AsyncSession = Depends(get_async_session),
):
    query = select(currency).where(currency.c.code == currency_code)
    result = await session.execute(query)
    response = result.mappings().fetchone()

    if response:
        return response
    return {"message": f"No currency with code {currency_code}"}
