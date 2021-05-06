import math
import sys
import itertools
import numpy as np


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
    lst = []
    for idx in tab:
        lst.append([dj[idx - 1], tab[idx - 1], pj[idx - 1], wj[idx - 1]])

    lst = sorted(lst, key=lambda x: x[0])
    pj, wj, dj, tab = [], [], [], []
    for val in lst:
        dj.append(val[0])
        tab.append(val[1])
        pj.append(val[2])
        wj.append(val[3])

    C, T, F, witi = calculate(pj, wj, dj, len(tab))
    print(f'\n pi: {tab}\n C: {C}\n T: {T}\n witi: {witi}\n F: {F}\n')


def calculate(pj, wj, dj, tab):
    S, C, T = [], [], []

    S.append(0)
    C.append(S[0] + pj[0])

    for elem in range(1, tab):
        S.append(C[elem - 1])
        C.append(S[elem] + pj[elem])

    for elem in range(0, tab):
        T.append(max(C[elem] - dj[elem], 0))

    F = 0
    witi = [None] * tab
    for elem in range(0, tab):
        witi[elem] = wj[elem] * T[elem]
        F += witi[elem]
    return C, T, F, witi


def brute_force(pj, wj, dj, tab):
    perm = list(itertools.permutations(range(1, len(tab) + 1)))
    res = sys.maxsize

    for i in range(len(perm)):
        pj_i, wj_i, dj_i, tab_i = [], [], [], []
        for j in range(len(perm[i])):
            pj_i.append(pj[perm[i][j] - 1])
            wj_i.append(wj[perm[i][j] - 1])
            dj_i.append(dj[perm[i][j] - 1])
            tab_i.append(tab[perm[i][j] - 1])
        C, T, F, witi = calculate(pj_i, wj_i, dj_i, len(perm[i]))
        if F < res:
            res = F
            Copt = C
            Topt = T
            witiopt= witi
            tab_iopt = tab_i

    print(f'\n pi: {tab_iopt}\n C: {Copt}\n T: {Topt}\n witi: {witiopt}\n F: {res}\n')
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

    print(f'\n\n nr: {tab}\n pj: {pj}\n wj: {wj}\n dj: {dj}\n')
    print("natural")
    C, T, target, witi = calculate(pj, wj, dj, task_number)
    print(f'\n pi: {tab}\n C: {C}\n T: {T}\n witi: {witi} \n F: {target}')

    print("\ngreedy")
    greedy(pj, wj, dj, tab)

    print("brute")
    brute_force(pj, wj, dj, tab)


if __name__ == "__main__":
    main()
