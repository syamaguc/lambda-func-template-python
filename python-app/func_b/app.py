import logging
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from common.utils import setup_chrome
from selenium.webdriver.common.by import By

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    # General check
    logger.info("## ENVIRONMENT VARIABLES")
    logger.info(os.environ)
    logger.info("## EVENT")
    logger.info(event)

    # Selenium check
    chrome = setup_chrome()
    chrome.get("https://example.com/")
    logger.info("## Selenium")
    logger.info(chrome.find_element(By.TAG_NAME, "h1").text)

    # Slack & CW check
    # post_slack("Hello world from lambda")
    # post_chatwork("Hello world from lambda")

    # return check
    return {"statusCode": 200, "message": "Hello world !", "body": event}
