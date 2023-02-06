from pydantic import BaseModel


class GetFromAnother(BaseModel):
    username: str
    collect: bool
