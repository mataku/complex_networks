#!/usr/bin/env python3
# coding: utf-8

# CNN(Connecting Nearest Neighbor)モデル
# 考え方: "友達の友達は、友達だ"
# ・友達の友達とは、友達になる可能性がある

# CNN モデルのアルゴリズム
# (以下の1, 2を繰り返す)
#
# 1. 1-pの確率で新たなノードを作成し、
#    既存のノードからランダムに1つ選び、リンクを結ぶ.
#    結んだ先のノードの近傍(そのノードからでているリンクの宛先ノード)を潜在的なリンク(potential edge)とする
# 2. pの確率で、potential edgeの中から1つランダムで選び、実リンクとする
#

import random

# class Node():
#     def __init__(self, id):
#         self.link = []
#         self.id = id

class CNN():

    def __init__(self, p = 0.2, steps = 100):

        self.links = {}
        self.index_of_node = 2

        for id in range(self.index_of_node + 1):
            self.links[id] = {}

        self.potential_links = []
        self.p = p
        self.steps = steps

        random.seed()


    # 初期状態のネットワークを生成
    # 0 - 1 - 2 -> 0 - 2が潜在辺
    def generate_init_network(self):

        for index in range(2):
            self.links[index][index+1] = 0
            self.links[index+1][index] = 0

        self.potential_links.append((0,2))

    def add_node(self):
        self.index_of_node += 1
        self.links[self.index_of_node] = {}

        target_index = random.randint(0, self.index_of_node - 1)
        self.potential_links += [(self.index_of_node, x) for x in self.links[target_index].keys()]

        self.links[self.index_of_node][target_index] = 0
        self.links[target_index][self.index_of_node] = 0


    def convert_potential_link(self):
        potential_source_node, potential_target_node = random.choice(self.potential_links)
        self.links[potential_source_node][potential_target_node] = 0
        self.links[potential_target_node][potential_source_node] = 0

    def generate(self):

        for _ in range(self.steps):
            rnd_value = random.random()
            if rnd_value < self.p:
                self.convert_potential_link()
            else:
                self.add_node()


def print_links(links):
    for source in links:
        for target in links[source]:
            print(source, target)



temp = CNN()
temp.generate_init_network()
temp.generate()
