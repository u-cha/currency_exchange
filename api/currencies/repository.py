import typing

from fastapi import Depends
from sqlalchemy import RowMapping, select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from models.models import currency


class CurrencyRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_currencies(self) -> typing.Sequence[RowMapping]:
        query = select(currency)
        result: Result = await self.session.execute(query)
        list_all_currencies = result.mappings().all()
        return list_all_currencies

    async def get_currency_by_code(self, currency_code: str) -> RowMapping | None:
        query = select(currency).where(currency.c.code == currency_code)
        result: Result = await self.session.execute(query)
        return result.mappings().fetchone()


async def get_currency_repository(session: AsyncSession = Depends(get_async_session)):
    return CurrencyRepository(session)
