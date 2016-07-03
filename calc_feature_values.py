#!/usr/bin/env python3
# coding: utf-8

from sys import argv

def import_links(filename):
    links = {}
    with open(filename, 'r') as file:
        for line in file:
            source, target = line.strip().split(' ')
            if source not in links:
                links[source] = {}
                links[source][target] = 0
            else:
                links[source][target] = 0
    return links


def degree_distribution(links):
    counter = {}
    for source in links:
        if len(links[source]) not in counter:
            counter[len(links[source])] = 1

        else:
            counter[len(links[source])] += 1

    return counter

network = import_links(argv[1])
degree_dist = degree_distribution(network)

for key in degree_dist:
    print(key, degree_dist[key])
