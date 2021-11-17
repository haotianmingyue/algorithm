#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/4
# @file 02完全平方数.py
fp = open('./Data/完全平方数.txt','w')
for i in range(20000):
    print(f"{i**2},",file=fp)

