#!/usr/bin/env python3
# coding: utf-8

# CNN(Connecting Nearest Neighbor)モデル
# 考え方: "友達の友達は、友達"

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
import simplejson

# class Node():
#     def __init__(self, id):
#         self.link = []
#         self.id = id

class CNN():

    def __init__(self, p = 0.2, steps = 100):

        self.links = {}
        self.subscript_of_node = 0
        self.links[self.subscript_of_node] = {}

        self.potential_links = []
        self.p = p
        self.steps = steps

        random.seed()


    def add_node(self):
        self.subscript_of_node += 1
        self.links[self.subscript_of_node] = {}

        target_subscript = random.randint(0, self.subscript_of_node - 1)
        self.potential_links += [(self.subscript_of_node, x) for x in self.links[target_subscript].keys()]

        self.links[self.subscript_of_node][target_subscript] = 0
        self.links[target_subscript][self.subscript_of_node] = 0


    def convert_potential_link(self):
        if len(self.potential_links) == 0:
            return

        target_subscript = random.randint(0, len(self.potential_links) - 1)
        potential_source_node, potential_target_node = self.potential_links[target_subscript]
        self.links[potential_source_node][potential_target_node] = 0
        self.links[potential_target_node][potential_source_node] = 0
        del self.potential_links[target_subscript]


    def generate(self):

        for _ in range(self.steps):
            rnd_value = random.random()
            if rnd_value < self.p:
                self.convert_potential_link()
            else:
                self.add_node()


def to_csv(link_data, separater=' '):
    for source in link_data:
        for target in link_data[source]:
            print(source, target, sep=separater)

def to_json_for_d3(link_data):
    nodes = []
    links = []

    for node in link_data.keys():
        nodes.append({'degree': len(link_data[node]), 'name': node})

        for target in link_data[node]:
            links.append({"source": node, "target": target})

    json = {'links': links, 'nodes': nodes}
    return simplejson.dumps(json)

cnn = CNN(steps = 100)
cnn.generate()

# json = to_json_for_d3(cnn.links)
# csv_data = to_csv(cnn.links))
# print(json)
