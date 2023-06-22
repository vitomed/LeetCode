from fastapi import FastAPI, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas, service, models, exeptions

app = FastAPI()


@app.get("/clients", response_model=list[schemas.Client])
async def get_cities(session: AsyncSession = Depends(models.get_session)):
    clients = await service.get_clients(session)
    return [schemas.Client(id=c.id) for c in clients]


@app.post("/clients")
async def add_city(session: AsyncSession = Depends(models.get_session)):
    client = service.add_client(session)
    try:
        await session.commit()
        return client
    except IntegrityError:
        await session.rollback()
        raise exeptions.DuplicatedEntryError("The client is already stored")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
