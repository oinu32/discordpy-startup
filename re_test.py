# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 23:40:45 2020

@author: watashi
"""
import MessageController
    

MsgCtrl = MessageController.MessageController()

print("入力をしてください:")
string = input()
MsgCtrl.InputProcess(string)

