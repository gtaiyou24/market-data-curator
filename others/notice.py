import json
import os
from typing import NoReturn

import requests


WEB_HOOK_URL = os.getenv("SLACK_WEB_HOOK_URL")
SERVER = os.getenv("SERVER")
USERNAME = "[ {} ] Market Data Curator".format(SERVER)


def post(message: str) -> NoReturn:
    requests.post(WEB_HOOK_URL, data=json.dumps({"text": message, "username": USERNAME}))
