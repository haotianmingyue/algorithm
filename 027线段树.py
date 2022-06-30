#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2022/6/29
# @file 027线段树.py


class seg_tree:
    def __init__(self, length):
        self.tree = [0]*length
        # self.length = length
        self.mask = [0]*length

    def build(self, l: int, r: int,  p: int, a: list):
        if l == r:
            self.tree[p] = a[l]
        else:
            mid = (l+r)//2
            self.build(l, mid, p*2+1, a)
            self.build(mid+1, r, p*2+2, a)
            self.tree[p] = self.tree[p*2+1] + self.tree[p*2+2]

    def update(self, l, r, d, p, cl, cr):
        if cl > r or cr < l:
            return
        elif cl >= l and cr <= r:
            self.tree[p] += ((cr-cl+1)*d)
            if cr > cl:
                self.mask[p] += d
        else:
            # mid = (cl+cr) // 2
            # self.mask[p*2+1] = self.mask[p]
            # self.mask[p*2+2] = self.mask[p]
            # self.tree[p*2+1] += self.mask[p]*(mid - cl + 1)
            # self.tree[p*2+2] += self.mask[p]*(cr - mid)
            # self.mask[p] = 0
            mid = self.push_down(cl, cr, p)
            self.update(l, r, d, p*2+1, cl, mid)
            self.update(l, r, d, p*2+2, mid+1, cr)
            self.tree[p] = self.tree[p*2+1] + self.tree[p*2+2]

    def query(self, l, r, p, cl, cr):
        if cl > r or cr < l:
            return 0
        elif cl >= l and cr <= r:
            return self.tree[p]
        else:
            mid = self.push_down(cl, cr, p)
            # 更新由于懒标记没更新的节点值
            return self.query(l, r, p*2+1, cl, mid) + self.query(l, r, p*2+2, mid+1, cr)

    def push_down(self, cl, cr, p):
        mid = (cl + cr) // 2
        self.mask[p * 2 + 1] = self.mask[p]
        self.mask[p * 2 + 2] = self.mask[p]
        self.tree[p * 2 + 1] += self.mask[p] * (mid - cl + 1)
        self.tree[p * 2 + 2] += self.mask[p] * (cr - mid)
        self.mask[p] = 0
        return mid
    # def __len__(self):


if __name__ == '__main__':
    s_t = seg_tree(30)
    a = [i for i in range(10)]
    # print(a)
    s_t.build(0, len(a)-1, 0, a)
    print(s_t.tree, sum(a))
    # 查询 [2,5] 闭区间的和
    print(s_t.query(2, 5, 0, 0, len(a) - 1))
    s_t.update(2, 7, 2, 0, 0, len(a)-1)
    print(s_t.tree)
    print(s_t.query(2, 5, 0, 0, len(a)-1))
