from pydantic import BaseModel


class TodoRequest(BaseModel):
    title: str
    text: str
