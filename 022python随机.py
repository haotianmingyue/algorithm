#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/12/16
# @file 022python随机.py
# import random
#
# for i in range(28):
#     print(random.uniform(36.3,37.2))
import numpy as np
# a = np.array([[1,2],[3,4]])
# b = np.array([[1,2],[3,4]])
# print(np.concatenate((a,b),axis=1))

a = np.array([[[[1,2,3,4],
              [1,2,3,4],[1,2,3,4]],
              [1,2]]])
a[0,4>1,0] = 0
print(a)

# import numpy as np
# X = np.array([[0,1,2,3],[10,11,12,13],[20,21,22,23],[30,31,32,33]])
# #X 是一个二维数组，维度为 0 ，1；第 0 层 [] 表示第 0 维；第 1 层 [] 表示第 1 维；
#
# # X[n0,n1] 表示第 0 维 取第n0 个元素 ，第 1 维取第 n1 个元素
# print(X[1,0])
# # X[1:3,1:3] 表示第 0 维 取 (1:3)元素 ，第 1 维取第(1:3) 个元素
# print(X[1:3,1:3])
#
# # X[:n0,:n1] 表示第 0 维 取 第0 到 第n0 个元素 ，第 1 维取 第0 到 第n1 个元素
# print(X[:2,:2])
# # X[:,:n1] 表示第 0 维 取 全部元素 ，第 1 维取 第0 到第n1 个元素
# print(X[:,:2])
#
# # X[:,0]) 表示第 0 维 取全部 元素 ，第 1 维取第 0 个元素
# print(X[:,0])
