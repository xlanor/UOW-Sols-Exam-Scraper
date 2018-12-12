#! /usr/bin/env python3
#
#   Class definition for telegram message
#
#####################
from typing import List
from Models.result_model import ResultModel

import arrow

class TGMessage():
    def __init__(self, botCh: str, rm:List[ResultModel]):
        self.__channel = botCh
        self.__resultModels = rm

    @property
    def resultModels(self)->List[ResultModel]:
        return self.__resultModels
    
    @resultModels.setter
    def resultModels(self, g:List[ResultModel]):
        self.__resultModels = g

    def __getDate(self)->str:
        return arrow.utcnow().to('Asia/Singapore').format('DD/MM/YYYY HH:mm:ss')
    
    def __isValid(self)->bool:
        markResults = [x.mark if x.mark else None for x in self.__resultModels ]
        return False if None in markResults else True
    
    def __getDict(self)->List[dict]:
        return [x.toDict() for x in self.__resultModels]
    
    def messageJson(self)->dict:
        returnMsg = f"<b>Result Scraped at {self.__getDate()}</b>\n\n"
        # Do not Use multiline because fucking tg will take it
        isValid = self.__isValid()
        if not isValid:
            returnMsg = f"{returnMsg}Results have not been released!"
        else:
            # cast all to dict.
            returnMsg = f"{returnMsg}Results have been released!"
        return {
            "chat_id":self.__channel,
            "text":returnMsg,
            "parse_mode":"HTML",
            "disable_notification":True
        }

