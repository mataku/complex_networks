#!/usr/bin/env python3
# coding: utf-8

# CNN(Connecting Nearest Neighbor)モデル
# 考え方: "友達の友達は、友達だ"
# ・友達の友達とは、友達になる可能性がある

# CNN モデルのアルゴリズム
# (以下の1, 2を繰り返す)
#
# 0. 1つの頂点から始める
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
        self.index_of_node = 0
        self.links[self.index_of_node] = {}

        self.potential_links = []
        self.p = p
        self.steps = steps

        random.seed()


    # 初期状態のネットワークを生成
    # 参考図: \もしくは/: 実辺, 点は潜在辺を表す
    #     1
    #    / \
    #   /   \
    #  0 ... 2

    def add_node(self):
        self.index_of_node += 1
        self.links[self.index_of_node] = {}

        target_index = random.randint(0, self.index_of_node - 1)
        self.potential_links += [(self.index_of_node, x) for x in self.links[target_index].keys()]

        self.links[self.index_of_node][target_index] = 0
        self.links[target_index][self.index_of_node] = 0


    def convert_potential_link(self):
        if len(self.potential_links) == 0:
            return

        target_index = random.randint(0, len(self.potential_links) - 1)
        potential_source_node, potential_target_node = self.potential_links[target_index]
        self.links[potential_source_node][potential_target_node] = 0
        self.links[potential_target_node][potential_source_node] = 0
        del self.potential_links[target_index]


    def generate(self):
        self.generate_init_network()

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



cnn = CNN(steps = 10000)
cnn.generate()
print_links(cnn.links)
