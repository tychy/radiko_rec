import requests
import json
from token_file import post_url


def post_slack(name, text):
    "post_url にはincoming web hook"
    requests.post(
        post_url,
        data=json.dumps(
            {"text": text,
             "username": name,
             "icon_emoji": ":python:"}))
    
# post_slack("自動ポスト","Done")
