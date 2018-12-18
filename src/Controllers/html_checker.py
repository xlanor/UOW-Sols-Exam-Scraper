#! /usr/bin/env python3
from Models.result_model import ResultModel
from typing import List

from bs4 import BeautifulSoup


class HtmlChecker:
    def __init__(self, html_string: str):
        self.__soupObj = BeautifulSoup(html_string, "html.parser")
        self.__rmObjects = []

    @property
    def rmObjects(self) -> List[ResultModel]:
        return self.__rmObjects

    def find_tables(self):
        self.__find_table_details(self.__soupObj.findAll("table")[0].findAll("tr"))

    def __find_table_details(self, soupResult):
        trCount = 0
        for tr in soupResult:
            trCount += 1
            if trCount == 1:
                continue
            details = tr.findAll("td")
            count = 0
            prep_dict = {}
            for detail in details:
                if count == 3:
                    prep_dict["module"] = detail.text
                elif count == 4:
                    prep_dict["nom_cp"] = detail.text
                elif count == 5:
                    prep_dict["mark"] = detail.text if detail.text.strip() else None
                elif count == 6:
                    prep_dict["grade"] = detail.text if detail.text.strip() else None
                elif count == 7:
                    prep_dict["status"] = detail.text

                count += 1

            self.__loadResultModel(prep_dict)

    def __loadResultModel(self, resultDict: dict):
        rm = ResultModel(resultDict)
        self.__rmObjects.append(rm)
