#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# @anthor haotian
# @date 2022/6/29
# @file 026前缀树.py


class Node:
    def __init__(self, this_value):
        self.this_value = this_value
        self.children = {}


class BaseTrie:
    def __init__(self):
        self.children = {'root': Node("root")}

    def add_new_path(self, new_path):
        temp_node = self.children['root']
        for node in new_path:
            if node in temp_node.children:
                temp_node = temp_node.children[node]
            else:
                new_node = Node(node)
                temp_node.children[node] = new_node
                temp_node = temp_node.children[node]

    # 删除时 只需要删除最后一个节点即可
    def delete_a_path(self, a_path):
        temp_node = self.children['root']
        for node in a_path:
            if node in temp_node.children:
                if len(temp_node.children) == 1:
                    temp_node.children = {}
                    return
                temp_node = temp_node.children[node]

    def get_sim_path(self, a_path):
        res = []
        temp_node = self.children['root'].children.get(a_path[0])
        if not temp_node:
            return []
        self.get_sim_pathes(temp_node, a_path, '', res)
        return res

    def print_trie(self):
        temp_node = self.children['root']

        self.get_pathes(temp_node, '')

    def get_pathes(self, child_tree, now_path):
        if child_tree.children == {}:
            print(now_path + child_tree.this_value)
        else:
            now_path += child_tree.this_value
            for child_node in child_tree.children:
                self.get_pathes(child_tree.children[child_node], now_path)

    def get_sim_pathes(self, child_tree, left_path, found_path, collector):
        if len(left_path) > 0 and child_tree.this_value != left_path[0]:
            return
        elif len(left_path) == 0 and child_tree.children == {}:
            found_path += child_tree.this_value
            collector.append(found_path)
        else:
            found_path += child_tree.this_value
            for child_node in child_tree.children:
                self.get_sim_pathes(child_tree.children[child_node], left_path[1:], found_path)

import time
if __name__ == '__main__':
    ss = ["我爱北京天安门。", "我爱北京的天安门。"]
#     ss = list(open(r'C:\Users\lipy\eclipse-workspace\Lab\src\test\short_long_text\tianlongbabu.txt', 'r', encoding='utf8').readlines())
    a_simple_trie = BaseTrie()
    for s in ss:
        a_simple_trie.add_new_path(list(s))
#     print(a_simple_trie.__dict__)
    a_simple_trie.print_trie()
    a_simple_trie.delete_a_path('十九 虽万千人吾往矣\n')
    t1 = time.time()
    print(a_simple_trie.get_sim_path("十九"))
    t2 = time.time()
    print("耗时是", t2-t1)

