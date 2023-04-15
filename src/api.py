from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from utils import _get_from_another
from utils import _post_content

api = FastAPI()
origins = ["*"]

api.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


@api.get("/")
def home():
  return {
    "Greetings": "Welcome to the Antispeedbump, you can save and share your instagram post",
  }


@api.post("/get_from_another/")
async def get_from_another(req: Request):
  try:
    get_from_another = await req.json()
    inf = _get_from_another(
      username=get_from_another.get('username'),
      collect=get_from_another.get('collect')
    )

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


if __name__ == '__main__':
  import uvicorn
  uvicorn.run(
    "api:api",
    host="0.0.0.0",
    port=80,
    debug=True,
  )
