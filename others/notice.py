import json
import os
from typing import NoReturn

import requests


WEB_HOOK_URL = os.environ.get("SLACK_WEB_HOOK_URL")
USERNAME = "通知"


def post(message: str) -> NoReturn:
    requests.post(WEB_HOOK_URL, data=json.dumps({"text": message, "username": USERNAME}))
