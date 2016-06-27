#!/usr/bin/env python3
# coding: utf-8

# ・Barabash-Albert model の アルゴリズム
#   1. ノード数n(nは小さい数)の完全グラフを生成
#   2. ノードを1つ追加
#   3. 追加された新規ノードからm本(m<=n)のリンクを、既存のノードへ繋ぐ.
#      リンク先は、そのノードの次数(持っているリンクの本数)が多いほど高くなる
#      (ノードiが選ばれる確率: ノードiの次数 / 全次数(全リンク数) )

# ・インスタンス変数
#   self.links: リンクの状態を示す
#     e.g. self.links[1][2] ノード1からノード2にリンクがある状態
#          値として、0を入れているが、距離を定義する際に使う
#
#   self.number_of_nodes: ノード数
#   self.max_number_of_nodes: 生成されるネットワークにおける最大のノード数の定義
#   self.number_of_links: 総次数 ( n * (n-1) )
#   self.number_of_node_to_link: 新規ノード生成時に、生成するリンク数の定義


from random import seed, randint
from traceback import format_exc
from copy import deepcopy

class BA():

    def __init__(self, init_number_of_nodes = 3, max_number_of_nodes = 100, number_of_node_to_link = None):

        if init_number_of_nodes < 1 or max_number_of_nodes < 1:
            raise Exception("初期ノード数は1以上、生成ノード数は正の数である必要があります。")

        self.links = {}
        self.number_of_nodes = init_number_of_nodes
        self.max_number_of_nodes = max_number_of_nodes
        self.number_of_links = init_number_of_nodes * (init_number_of_nodes - 1)
        self.complete_graph()

        if number_of_node_to_link is not None:
            self.number_of_nodes_to_link = number_of_node_to_link
        else:
            self.number_of_nodes_to_link = self.number_of_nodes


    # 完全グラフの生成
    def complete_graph(self):

        for index in range(self.number_of_nodes):
            self.links[index] = {}

            for x in range(index):
                if x != index:
                    self.links[x][index] = 0
                    self.links[index][x] = 0


    # def number_set(self):
    #     numbers = []
    #     while len(numbers) < self.number_of_nodes_to_link:
    #         temp_number = randint(1, self.number_of_links)
    #         if temp_number not in numbers:
    #             numbers.append(temp_number)
    #     return sorted(numbers, key=int)

    # 新規ノードからリンクを生成する際の、宛先ノードの選定
    def choose_node(self):

        nodes = []
        links = deepcopy(self.links)
        number_of_links = self.number_of_links

        while len(nodes) < self.number_of_nodes_to_link:
            temp_number = 0
            number_to_select = randint(1, number_of_links)
            for x in links.keys():
                temp_number += len(links[x])
                if temp_number >= number_to_select:
                    nodes.append(x)
                    number_of_links = number_of_links - len(links[x])
                    del links[x]
                    break

        return sorted(nodes, key=int)


    def generate(self):
        seed()

        while self.number_of_nodes < self.max_number_of_nodes:
            nodelist = self.choose_node()
            self.links[self.number_of_nodes] = {}
            for x in nodelist:
                self.links[self.number_of_nodes][x] = 0
                self.links[x][self.number_of_nodes] = 0

            # リンク数でなく、総次数を増やすため、2倍
            self.number_of_links += self.number_of_nodes_to_link * 2
            self.number_of_nodes += 1


test = BA(init_number_of_nodes = 3)
test.generate()
