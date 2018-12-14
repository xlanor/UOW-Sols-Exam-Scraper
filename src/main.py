from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from typing import List

import os
import time
import requests
import schedule
import time
import json

# Internal Imports
from Controllers.html_checker import HtmlChecker
import Controllers.selenium_loader as Scraper
from Models.result_model import ResultModel
from Models.telegram_message import TGMessage

print(os.getcwd())
with open ('./config.json') as f:
    configDict = json.loads(f.read())

BOT_TOKEN = configDict.get("token")
CHANNEL_CHAT_ID = configDict.get("channelID")
CLIENT_USERNAME = configDict.get("clientUsn")
CLIENT_PW = configDict.get("clientPw")
LIST_OF_SUBJECTS = configDict.get("modulesToFind")

TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


def find_tables()->List[ResultModel]:
    HtmlObj = Scraper.login(CLIENT_USERNAME,CLIENT_PW)
    HtmlObj.find_tables()
    return HtmlObj.rmObjects
    #markResults = [x.mark if x.mark else None for x in list_obj ]

def send_requests(msg: dict):
    requests.post(TELEGRAM_URL,json=msg)

def job():
    print("Running job")
    result_list = find_tables()
    msgJs = TGMessage(CHANNEL_CHAT_ID,result_list,LIST_OF_SUBJECTS).messageJson()
    send_requests(msgJs)

if __name__ == "__main__":
    schedule.every(10).minutes.do(job)

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except Exception as e:
            print(str(e))
            pass
