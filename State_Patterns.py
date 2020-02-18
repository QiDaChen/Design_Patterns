#!/usr/bin/python3
# -*- coding:utf-8 -*-
# project:
# user:QiDaChen
# Author: chen.qi
# Mail:chenphoun#outlook.com
# createtime: 2020/2/17 13:22
from abc import ABC,ABCMeta,abstractmethod

class Water:
    def __init__(self,state):
        self.__temperature = 25
        self.__state = state

    def setState(self,state):
        self.__state = state

    def changeState(self,state):
        if (self.__state):
            print("由状态{}变成状态{}".format(self.__state,state.GetName()))
        else:
            print("初始化状态{}".format(state.GetName()))
        self.__state = state

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self,temperature):
        self.__temperature = temperature
        if (self.__temperature <= 0):
            self.changeState(SoildState("固态"))
        elif (self.__temperature<=100):
            self.changeState(LiquidState("液态"))
        else:
            self.changeState(GaseousSTate("气态"))

class State(metaclass=ABCMeta):
    '''状态类'''
    def __init__(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def behavios(self,water):
        '''不同状态下的行为'''
        pass

class SoildState(State):
    pass

class LiquidState(State):
    pass

class GaseousSTate(State):
    pass
