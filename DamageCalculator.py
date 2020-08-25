# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 01:52:46 2020

@author: watashi
"""

from collections import deque

class DamageCalculator:
    def __init__(self):
        self.mResult = deque()
        self.mResultTotal = 0


    def CalcResult(self):
        for resultTaple in self.mResult:
            resultval = resultTaple[1]#スコアの値を取り出している
            self.mResultTotal = self.mResultTotal + resultval;


    def GetResult(self):
        return self.mResult

    
    def GetResultTotal(self):
        return self.mResultTotal

            
    def InsertResult(self, pName, pDamage):
        self.mResult.append( (pName, pDamage) )    
