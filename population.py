#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import random
import time
import life

class Population:
    def __init__(self, num_life, gene_init, upd_prob, mutation_prob):
        self.num_life = num_life
        self.life_array = []
        self.upd_num = int(upd_prob * num_life)
        self.mutation_num = int(mutation_prob * num_life)
        self.life_array_alive = []
        self.mutation_idx_buf = [idx for idx in range(num_life)]
        for idx in range(num_life):
            gene_tmp = [x for x in gene_init]
            random.shuffle(gene_tmp)
            # print(gene_tmp)
            self.life_array.append(life.Life(gene_tmp))

        return

    def life_dead(self):
        life_array_rank = sorted(self.life_array, key=lambda x: x.__score__(), reverse=True)
        num_alive = self.num_life - self.upd_num
        self.life_array_alive = life_array_rank[0:num_alive]
        # print([x.__score__() for x in life_array_rank])
        # time.sleep(1)

    # random choose alive unit
    def breed(self):
        num_alive = self.num_life - self.upd_num
        new_life_array = []
        for idx in range(self.upd_num):
            idx1, idx2 = random.randint(0, num_alive - 1), random.randint(0, num_alive - 1)
            father1, father2 = self.life_array[idx1], self.life_array[idx2]
            # print(father1.__gene__(), father2.__gene__())
            chd_gene1 = cross_gene(father1.__gene__(), father2.__gene__())
            new_life_array.append(life.Life(chd_gene1))
            # new_life_array.append(Life(chd_gene2))
        self.life_array = new_life_array + self.life_array_alive
        return


    def mutation(self):
        self.mutation_idx_buf = [random.randint(0, self.num_life-1) for idx in range(self.mutation_num)]
        for idx in self.mutation_idx_buf:
            self.life_array[idx].mutation()
        return

    def cnt_score(self, adjmatrix):
        new_life_idx_buf = [idx for idx in range(self.upd_num)]
        cnt_score_idx_buf = list(set(new_life_idx_buf + self.mutation_idx_buf))
        for life_idx in cnt_score_idx_buf:
            self.life_array[life_idx].cnt_score(adjmatrix)

    def revolution(self, adjmatrix, total_time):
        for t in range(total_time):
            self.cnt_score(adjmatrix)
            print('score:',self.get_top_score())
            self.life_dead()
            self.breed()
            if t < total_time - 1:
                self.mutation() # do not mutate in the last time
        return

    def get_top_score(self):
        score_buf = [x.__score__() for x in self.life_array]
        return max(score_buf)

    def __population_gene__(self):
        return [x.__gene__() for x in self.life_array]

def cross_gene(fgene1, fgene2):
    if not len(fgene1) == len(fgene2):
        print('Error: length of two father genes')
        # print(fgene1, fgene2)

    idx1, idx2 = random.randint(0, len(fgene1) - 1), random.randint(0, len(fgene2) - 1)
    idx1, idx2 = min(idx1, idx2), max(idx1, idx2)
    gene_mid = [x for x in fgene1[idx1:idx2]]
    gene_tmp = []
    for g in fgene2:
        if g not in gene_mid:
            gene_tmp.append(g)
    chd_gene = gene_tmp[0:idx1] + gene_mid + gene_tmp[idx1:]
    # print(fgene1, fgene2)
    # print(idx1, idx2)
    # print(chd_gene)
    # time.sleep(1)
    return chd_gene