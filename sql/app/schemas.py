from pydantic import BaseModel


class Client(BaseModel):
    id: int
