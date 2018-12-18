# File to test telegram message model
import pytest

from Controllers.html_checker import HtmlChecker
from Models.telegram_message import TGMessage

EXISTS_HTML = ""
NOT_EXISTS_HTML = ""

with open("src/Tests/Sources/exist.html") as ex:
    exString = ex.read()
    EXISTS_HTML += exString

with open("src/Tests/Sources/not_exist.html") as nex:
    nexString = nex.read()
    NOT_EXISTS_HTML += nexString


def test_telegram_message_model():
    existHtml = HtmlChecker(exString)
    existHtml.find_tables()
    tableExist = existHtml.rmObjects
    notExistHtml = HtmlChecker(nexString)
    notExistHtml.find_tables()
    notTableExist = notExistHtml.rmObjects

    tgMsgExist = TGMessage("S1234567", tableExist, [ "CSCI235", "CSCI204" ])
    existMessage = tgMsgExist.messageJson()
    tgMsgNotExist = TGMessage("S1234567", notTableExist, [ "CSCI235", "CSCI204" ])
    notExistMessage = tgMsgNotExist.messageJson()
    r1 = "CSCI204 found: 31/C"
    r2 = "CSCI235 found: 31/C"
    r3 = "CSCI204 unreleased."
    r4 = "CSCI235 unreleased."
    
    # TODO FIX THE ASSERTIONS HERE
    assert r1 in existMessage.get("text")
    assert r2 in existMessage.get("text")
    assert r3 not in existMessage.get("text")
    assert r4 not in existMessage.get("text")
    assert r1 not in notExistMessage.get("text")
    assert r2 not in notExistMessage.get("text")
    assert r3 in notExistMessage.get("text")
    assert r4 in notExistMessage.get("text")
    ## assert r2 not in notExistMessage.get("text")
    # assert r1 in notExistMessage.get("text")
    # assert notExistMessage.get("chat_id") == "S1234567"
    assert existMessage.get("chat_id") == "S1234567"
