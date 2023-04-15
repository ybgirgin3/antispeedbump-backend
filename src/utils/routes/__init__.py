from antispeedbump.bot import Bot
from pprint import pprint
from pathlib import Path


def _get_from_another(username: str, collect: bool):
  if not Path("database.db").exists():
    from antispeedbump.commons import SQL_ALCHEMY_ENGINES, _create_table

    _create_table("Sites", SQL_ALCHEMY_ENGINES["antispeedbump"])
    _create_table("Queue", SQL_ALCHEMY_ENGINES["antispeedbump"])

  try:
    ret = Bot(
      target_user=username,
      will_create_content=collect,
    ).get_data_from_another()
    pret = {"full_name": ret["full_name"],
            "profile_picture": ret["profile_picture"]}
    pprint(pret)
    return pret

  except Exception as e:
    return {"error": e}


def _post_content():
  import json

  # read creds
  with open('src/credientials.json') as f:
    creds = json.loads(f.read())

  ret = Bot(
    username=creds['username'],
    password=creds['password'],
    post_type=type).post_content()
  return ret
