#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2022/3/22
# @file 023torch.py
import torch
# print(torch.zeros(2,2,2))

import numpy as np
# print((np.array([1,2,3,4])))
#
# print(torch.FloatTensor(np.array([1,2,3,4])))
#
# print(torch.FloatTensor(np.array([1,2,3,4])).unsqueeze(0))
#
# print(torch.FloatTensor(np.concatenate((np.zeros((2, 2)),np.array([[1],[1]])), 1)))


# n_m = torch.ones(5,2,5,5,requires_grad=False)
# # print(n_m)
# n_m[0,0,0,0] = 6
# print(n_m)
#
# print(n_m[0,0.6>0.5,0,0,0])  #所以 bool表示是否选取后面那一列？？

# n = np.array([[1,2,3],[1,2,3]])
# print(n[:,1])
#
# n =  torch.ones((2,0,2,2))
# print(n.size())

#
# a = np.zeros((1,1))
# print(a)
# b = np.ones((1,2))
# print(b)
# print(np.concatenate((a,b),1))
# a = np.array([1,2,3])
# print(a)
# a = torch.ones((1,4))
# b = torch.zeros((1,4))
# print(a)
#
#
# print(torch.clamp(torch.max(a[:,0],b[:,0])-2,min= 1)*torch.clamp(torch.max(a[:,0],b[:,0]),min= 2)>1)
#
# a = torch.asarray([[1,2],[1,2]])
# b = torch.asarray([[2,2],[2,2]])
# print(a*b)

a = 