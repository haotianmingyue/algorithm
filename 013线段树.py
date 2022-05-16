#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2021/11/20
# @file 013线段树.py
class Segment_tree():
    def __init__(self,n):
        self.l = [0]*n
    def build(self,s:int,t:int,p:int,a:list):
        if s==t:
            self.l[p] = a[s]
        mid = s + ((t-s)>>1)
        self.build(s,mid,p*2,a)
        self.build(mid+1,t,p*2+1,a)
        self.l[p] = self.l[p*2] + self.l[p*2+1]

    def getsum(self,l,r,s,t,p):
        if l<=s and t<=r:
            return self.l[p]
        m = s + ((t-s)>>1)
        sum :int = 0
        if l<=m:
            sum += self.getsum(l,r,s,m,p*2)
        if r>m:
            sum += self.getsum(l,r,m+1,t,p*2+1)
        return sum


