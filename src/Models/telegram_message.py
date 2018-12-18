#! /usr/bin/env python3
#
#   Class definition for telegram message
#
#####################
from typing import List
from Models.result_model import ResultModel

import arrow


class TGMessage:
    def __init__(self, botCh: str, rm: List[ResultModel], subsToFind: List[str]):
        self.__channel = botCh
        self.__resultModels = rm
        self.__subjectToFind = subsToFind

    @property
    def resultModels(self) -> List[ResultModel]:
        return self.__resultModels

    @resultModels.setter
    def resultModels(self, g: List[ResultModel]):
        self.__resultModels = g

    def __getDate(self) -> str:
        return arrow.utcnow().to("Asia/Singapore").format("DD/MM/YYYY HH:mm:ss")

    def __isValid(self) -> List[str]:
        returnList = []
        for subCode in self.__subjectToFind:
            for rm in self.__resultModels:
                if rm.subjectCode.strip().lower() == subCode.strip().lower():
                    if rm.mark:
                        returnList.append(
                            f"{rm.subjectCode} found: {rm.mark}/{rm.grade}\n"
                        )
                    else:
                        returnList.append(f"{rm.subjectCode} unreleased.\n")
        return returnList

    def __getDict(self) -> List[dict]:
        return [x.toDict() for x in self.__resultModels]

    def messageJson(self) -> dict:
        returnMsg = f"<b>Result Scraped at {self.__getDate()}</b>\n\n"
        # Do not Use multiline because fucking tg will take it
        resultString = self.__isValid()
        resultString = "".join(resultString)
        returnMsg = f"{returnMsg} {resultString}"
        return {
            "chat_id": self.__channel,
            "text": returnMsg,
            "parse_mode": "HTML",
            "disable_notification": True,
        }
