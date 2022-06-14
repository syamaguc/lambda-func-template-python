import os
import requests
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random


def setup_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    user_agent = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    ]
    UA = user_agent[random.randrange(0, len(user_agent), 1)]
    options.add_argument("--user-agent=" + UA)
    dl_path = '/tmp/downloads'
    options.add_experimental_option(
        "prefs",
        {"download.default_directory": dl_path,
            "download.prompt_for_download": False},
    )
    options.binary_location = '/opt/chrome/chrome'
    chrome = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    chrome.implicitly_wait(10)
    return chrome


def post_chatwork(msg):
    apiurl = 'https://api.chatwork.com/v2'
    roomid = os.environ['CW_ROOM_ID']
    apikey = os.environ['CW_API_KEY']
    post_message_url = f'{apiurl}/rooms/{roomid}/messages'
    headers = {'X-ChatWorkToken': apikey}
    params = {'body': msg}
    return requests.post(post_message_url, headers=headers, params=params)


def post_slack(msg):
    SLACK_WEB_HOOK_URL = os.environ['SLACK_WEB_HOOK_URL']

    requests.post(SLACK_WEB_HOOK_URL, data=json.dumps({
        'text': msg,
        'username': 'lambda-notification',
        'icon_emoji': ':smile_cat:',
        'link_names': 1,
    }))
