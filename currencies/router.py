import logging
from sqlite3 import IntegrityError
from typing import Annotated

from fastapi import APIRouter, Depends, Path, status, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from database import get_async_session
from models.models import currency
from currencies.models import Currency

logger = logging.getLogger(__name__)

currencies_router = APIRouter(prefix="/currencies", tags=["currency"])
currency_router = APIRouter(prefix="/currency", tags=["currency"])


@currencies_router.get("/")
async def get_currencies(session: AsyncSession = Depends(get_async_session)):
    logger.info("Retrieving all currencies...")
    query = select(currency)
    currencies = await session.execute(query)
    return currencies.mappings().all()


@currencies_router.post("/", status_code=status.HTTP_201_CREATED)
async def post_currency(
    curr: Currency, session: AsyncSession = Depends(get_async_session)
):
    stmt = (insert(currency).values(**curr.dict())).returning(currency)
    try:
        async with session:
            response = await session.execute(stmt)
            await session.commit()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Currency already exists")
    return response.mappings().fetchone()


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
