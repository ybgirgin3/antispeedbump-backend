from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils import _get_from_another
from utils import _post_content

from pydantic import BaseModel


class GetFromAnother(BaseModel):
    username: str
    collect: bool


api = FastAPI()
origins = ["*"]


@api.get("/")
def home():
    return {
        "Greetings": "Welcome to the Antispeedbump, you can save and share your instagram post",
    }


@api.post("/get_from_another/")
def get_from_another(get_from_another: GetFromAnother):
    try:
        inf = _get_from_another(
            username=get_from_another.username,
            collect=get_from_another.collect)

        ret = {
            "status": 200,
            "response": inf,
        }
        return ret
    except Exception as e:
        raise e


@api.post("/post/")
def post_content():
    try:
        return _post_content()
    except Exception as e:
        raise e
