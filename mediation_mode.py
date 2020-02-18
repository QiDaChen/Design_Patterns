#!/usr/bin/python3
# -*- coding:utf-8 -*-
# project:
# user:QiDaChen
# Author: chen.qi
# Mail:chenphoun#outlook.com
# createtime: 2020/2/18 17:01

class InteractiveObject:
    '''进行交互的对象'''
    pass

class InteractiveObjectImplA:
    '''实现类A'''
    pass

class InteractiveObjectImplB:
    '''实现类B'''
    pass

class Meditor:
    '''中介类'''
    def __init__(self):
        self.__interactiveObjectA = InteractiveObjectImplA()
        self.__interactiveObjectB = InteractiveObjectImplB()
    def interative(self):
        '''进行交互的操作'''
        # 通过self.__interactiveObjA 和 self.__interactiveobjB 完成相应的交互操作
        pass