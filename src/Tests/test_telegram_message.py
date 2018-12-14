# File to test telegram message model
import pytest

from Controllers.html_checker import HtmlChecker
from Models.telegram_message import TGMessage

EXISTS_HTML = ""
NOT_EXISTS_HTML = ""

with open('src/Tests/Sources/exist.html') as ex:
    exString = ex.read()
    EXISTS_HTML += exString

with open('src/Tests/Sources/not_exist.html') as nex:
    nexString = nex.read()
    NOT_EXISTS_HTML += nexString

def test_telegram_message_model():
    existHtml = HtmlChecker(exString)
    existHtml.find_tables()
    tableExist = existHtml.rmObjects
    notExistHtml = HtmlChecker(nexString)
    notExistHtml.find_tables()
    notTableExist = notExistHtml.rmObjects
    tgMsgExist = TGMessage("S1234567",tableExist,[])
    existMessage = tgMsgExist.messageJson()
    tgMsgNotExist = TGMessage("S1234567",notTableExist,[])
    notExistMessage = tgMsgNotExist.messageJson()
    r1 = "Results have not been released!"
    r2 = "Results have been released!"
    # TODO FIX THE ASSERTIONS HERE
    #assert r2 in existMessage.get("text")
    #assert r1 not in existMessage.get("text")
    ## assert r2 not in notExistMessage.get("text")
    #assert r1 in notExistMessage.get("text")
    #assert notExistMessage.get("chat_id") == "S1234567"
    assert existMessage.get("chat_id") == "S1234567"