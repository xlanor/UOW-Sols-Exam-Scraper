#! /usr/bin/env python3
#
# Model definition for Results.
from typing import Union


def cast_string_or_none(func):
    """
    A decorator to explicitly cast to str else
    leave as Nonetype.
    @param func, a function
    @return func, a nested function.
    """
    def wrapper(*args,**kwargs):
        """
        A function wrapper to explicitly 
        cast to str else leave as Nonetype.
        @param *args
        @param **kwargs
        @return str if function does not return None
        @return None if function returns None.
        """
        returnVal = func(*args,**kwargs)
        return str(returnVal) if returnVal else returnVal
    return wrapper

class ResultModel():
    def __init__(self,dictOfValues:dict):
        """
        {'module': 'CSCI103', 
        'nom_cp': '6', 
        'mark': '87', 
        'grade': 'HD', 
        'status': '87/HD'}
        """
        self.__subjectCode = dictOfValues.get("module")
        self.__nomCp = dictOfValues.get("nom_cp")
        self.__mark = dictOfValues.get("mark")
        self.__grade = dictOfValues.get("grade")
        self.__status = dictOfValues.get("status")
    
    @property
    @cast_string_or_none
    def subjectCode(self)->Union[str,None]:
        return self.__subjectCode
    
    @subjectCode.setter
    def subjectCode(self, sc:str):
        self.__subjectCode = sc
    
    @property
    @cast_string_or_none
    def nomCp(self)->Union[str,None]:
        return self.__nomCp

    @nomCp.setter
    def nomCp(self, ncp:str):
        self.__subjectCode = ncp
    
    @property
    @cast_string_or_none
    def mark(self)->Union[str,None]:
        return self.__mark

    @mark.setter
    def mark(self, mark:str):
        self.__mark = mark
    
    @property
    @cast_string_or_none
    def grade(self)->Union[str,None]:
        return self.__grade
    
    @grade.setter
    def grade(self, g:str):
        self.__grade = g

    @property
    @cast_string_or_none
    def status(self)->Union[str,None]:
        return self.__status

    @status.setter
    def status(self, s:str):
        self.__status = s


    def toDict(self)->dict:
        return { 
                'module': self.subjectCode, 
                'nom_cp': self.nomCp, 
                'mark': self.mark, 
                'grade': self.grade, 
                'status': self.status
            }
