#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import time
import random

class Life:
    def __init__(self, gene):
        self.gene = gene
        self.score = 0
        return

    def mutation(self):
        idx1, idx2 = random.randint(0, len(self.gene)-1), random.randint(0, len(self.gene)-1)
        self.gene[idx1], self.gene[idx2] = self.gene[idx2], self.gene[idx1]

    def __gene__(self):
        return self.gene

    def cnt_score(self, adjmatrix):
        self.score = 0
        for idx in range(len(self.gene)-2):
            idx2, idx3 = self.gene[idx], self.gene[idx+1]
            self.score = self.score - adjmatrix[idx2][idx3]
        # print(adjmatrix)
        # print(self.score)
        # time.sleep(1)
        return

    def __score__(self):
        return self.score