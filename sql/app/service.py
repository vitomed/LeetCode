from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Client


async def get_clients(session: AsyncSession) -> list[Client]:
    result = await session.execute(select(Client).limit(10))
    return result.scalars().all()


def add_client(session: AsyncSession) -> Client:
    new_client = Client()
    session.add(new_client)
    return new_client
