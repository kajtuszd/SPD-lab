import math
import time

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


def calculate(pj, task_number, machine_number):
    Sj, Cj, S, C = [], [], [], []
    S.append(0)
    C.append(S[0] + pj[0][0])
    S.append(max(C[0], 0))
    C.append(S[1] + pj[0][1])
    for m in range(2, machine_number):
        S.append(max(C[m - 1], 0))
        C.append(S[m] + pj[0][m])
    Sj.append(S.copy());    S.clear()
    Cj.append(C.copy());    C.clear()
    Cmax = Cj[0][1]

    for j in range(1, task_number):
        S.append(max(0, Cj[j - 1][0]))
        C.append(S[0] + pj[j][0])
        for m in range(1, machine_number):
            S.append(max(C[m - 1], Cj[j - 1][m]))
            C.append(S[m] + pj[j][m])
        Sj.append(S.copy());    S.clear()
        Cj.append(C.copy());    C.clear()
        Cmax = max(Cmax, Cj[j][machine_number - 1])
    return [[Sj, Cj], Cmax]


def findmin(pj):
    values, idx2 = [], []
    for idx1 in range(len(pj)):
        values.append(min(pj[idx1]))
        idx2.append(pj[idx1].index(values[-1]))
    idx1 = values.index(min(values))
    return idx1, idx2[idx1]


def Johnson2(tasks, pj):
    l = 0
    k = len(tasks) - 1
    tasks = list(tasks)
    N = tasks.copy()
    while len(N):
        j, i = findmin(pj)
        if pj[j][0] < pj[j][1]:
            tasks[l] = j + 1
            l += 1
        else:
            tasks[k] = j + 1
            k -= 1
        N.remove(j + 1)
        pj[j] = [9999999999, 9999999999] # pj.remove(pj[j]) psuje findmin
    return tasks


def main():
    seed = int(input("Enter Z number: "))
    generator = RandomNumberGenerator(seed)
    task_number = int(input("Enter tasks number: "))
    tasks = range(1, task_number + 1)
    machine_number = int(input("Enter machines number: "))
    machines = range(1, machine_number + 1)
    pj, pi, Tab, p = [], [], [], []

    for task in tasks:
        for _ in machines:
            p.append(generator.nextInt(1, 29))
        pj.append(p.copy())
        p.clear()
        pi.append(task)

    print(pj)

    [[Sj, Cj], Cmax] = calculate(pj, task_number, machine_number)

    print("\nnr: {} \nCj: {} \nCmax: {}".format(pi, Cj, Cmax))

    for task in tasks:
        Tab.append([pi[task-1], pj[task-1]])

    start = time.time()
    pi = Johnson2(tasks, pj.copy())
    total = time.time() - start
    sort = {x: i for i, x in enumerate(pi)}
    Tab.sort(key = lambda x: sort[x[0]])
    [[Sj, Cj], Cmax] = calculate([row[1] for row in Tab], task_number, machine_number)
    print("\nJohnson \nnr: {} \nCj: {} \nCmax: {}".format(pi, Cj, Cmax))
    print("Working time: {0:02f} s".format(total))


if __name__ == "__main__":
    main()
