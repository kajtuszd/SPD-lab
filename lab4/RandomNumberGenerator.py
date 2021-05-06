import math
import numpy as np
import itertools
import sys


class RandomNumberGenerator:

    def __init__(self, seedValue=None):
        self.__seed = seedValue


    def nextInt(self, low, high):
        m = 2147483647
        a = 16807
        b = 127773
        c = 2836
        k = int(self.__seed / b)
        self.__seed = a * (self.__seed % b) - k * c
        if self.__seed < 0:
            self.__seed = self.__seed + m
        value_0_1 = self.__seed
        value_0_1 = value_0_1 / m
        return low + int(math.floor(value_0_1 * (high - low + 1)))


    def nextFloat(self, low, high):
        low *= 100000
        high *= 100000
        val = self.nextInt(low, high) / 100000.0
        return val


def greedy(pj, wj, dj, tab):
    calc = []
    for index, elem in enumerate(tab):
        calc.append([dj[index], tab[index], pj[index], wj[index]])

    calc = sorted(calc, key=lambda x: x[0])
    pj, wj, dj, tab = [], [], [], []
    for value in calc:
        dj.append(value[0])
        tab.append(value[1])
        pj.append(value[2])
        wj.append(value[3])

    C, T, F, witi = calculate(pj, wj, dj, len(tab))
    print(f'\n C: {C}\n T: {T}\n F: {F}\n witi: {witi}\n')
    print(f'\n\n Tab: {tab}\n pj: {pj}\n wj: {wj}\n dj: {dj}\n')



def calculate(pj, wj, dj, tab):
    S, C, T = [], [], []

    S.append(0)
    C.append(S[0] + pj[0])

    for task in range(1, tab):
        S.append(C[task - 1])
        C.append(S[task] + pj[task])

    for task in range(0, tab):
        T.append(max(C[task] - dj[task], 0))

    F = 0
    witi = [None] * tab
    for task in range(0, tab):
        witi[task] = wj[task] * T[task]
        F += witi[task]
    return C, T, F, witi


def brute_force(pj, wj, dj, tab):
    perm = list(itertools.permutations(range(1, tab + 1)))
    res = sys.maxsize

    for i in range(len(perm)):
        pj_i, wj_i, dj_i = [], [], []
        for j in range(len(perm[i])):
            pj_i.append(pj[perm[i][j] - 1])
            wj_i.append(wj[perm[i][j] - 1])
            dj_i.append(dj[perm[i][j] - 1])
        C, T, F, witi = calculate(pj_i, wj_i, dj_i, len(perm[i]))
        if F < res:
            res = F

    C, T, F, witi = calculate(pj, wj, dj, tab)
    print(f'\n C: {C}\n T: {T}\n F: {F}\n witi: {witi}\n')
    print(f'\n\n Tab: {tab}\n pj: {pj}\n wj: {wj}\n dj: {dj}\n')
    return res


def main():
    seed = int(input("Enter Z number: "))
    generator = RandomNumberGenerator(seed)
    task_number = int(input("Enter tasks number: "))
    tasks = range(1, task_number + 1)
    
    tab, pj, wj, dj = [], [], [], []
    
    for task in tasks:
        tab.append(task)
        pj.append(generator.nextInt(1, 29))

    for task in tasks:
        wj.append(generator.nextInt(1, 9))

    for task in tasks:
        dj.append(generator.nextInt(1, 29))

    print(f'\n\n Tab: {tab}\n pj: {pj}\n wj: {wj}\n dj: {dj}\n')
    C, T, target, witi = calculate(pj, wj, dj, task_number)
    print(f'\n C: {C}\n T: {T}\n \n witi: {witi} \n target: {target}')

    print(f'F={brute_force(pj, wj, dj, task_number)}')

    greedy(pj, wj, dj, tab)


if __name__ == "__main__":
    main()

