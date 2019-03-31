#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import random
import life
import population


o_dis_func = lambda x, y: (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

def main():
    Num_city = 50
    corrd = [[random.uniform(0,10), random.uniform(0,10)] for idx in range(Num_city)]
    adj_matrix = [[ o_dis_func(corrd[idx1], corrd[idx2]) + 10  \
        for idx1 in range(Num_city)] for idx2 in range(Num_city)]
    Num_unit = 10000

    route_init = [idx for idx in range(Num_city)]
    popul = population.Population(Num_unit, route_init, 0.7, 0.001)
    popul.revolution(adj_matrix, 1000)
    print(popul.__population_gene__())

    return


if __name__ == '__main__':
    main()
