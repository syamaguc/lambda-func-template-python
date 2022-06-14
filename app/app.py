from utils import post_slack, post_chatwork, setup_chrome
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    # General check
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(os.environ)
    logger.info('## EVENT')
    logger.info(event)

    # Selenium check
    chrome = setup_chrome()
    chrome.get("https://example.com/")
    logger.info('## Selenium')
    logger.info(chrome.find_element_by_xpath("//html").text)

    # Slack & CW check
    post_slack('Hello world from lambda')
    post_chatwork('Hello world from lambda')

    # return check
    return {
        'statusCode': 200,
        'message': 'Hello world !',
        'body': event
    }
