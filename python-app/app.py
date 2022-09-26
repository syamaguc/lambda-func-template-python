import logging
import os

from selenium.webdriver.common.by import By
from utils import post_chatwork, post_slack, setup_chrome

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
