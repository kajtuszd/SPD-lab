import math


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




def calculate(pj, task_number, machine):
    Sj = []
    Cj = []
    Cjq = []
    S = []
    C = []


    S.append(0)
    C.append(S[0]+pj[0][0])
    S.append(max(0,C[0]))
    C.append(S[1]+pj[0][1])
    Sj.append(S.copy())
    S.clear()    
    Cj.append(C.copy())
    C.clear()
    Cmax = Cj[0][1]

    for j in range(1, task_number):
        S.append(max(0,Cj[j-1][0]))
        C.append(S[0]+pj[j][0])
        for m in range(1, machine):
            S.append(max(C[m-1],Cj[j-1][m]))
            C.append(S[m]+pj[j][m])
        Sj.append(S.copy())
        S.clear()
        Cj.append(C.copy())
        C.clear()
        Cmax = max(Cmax, Cj[j][machine-1])
    return [[Sj, Cj, Cjq], Cmax]


def main():
    seed = int(input("Enter Z number: "))
    generator = RandomNumberGenerator(seed)
    task_number = int(input("Enter tasks number: "))
    tasks = range(1, task_number + 1)
    machine = 2
    rj, pj, qj, pi, Tab = [], [], [], [], []
    p = []

    for task in tasks:
        for m in range(1,machine+1):
            p.append(generator.nextInt(1, 29))
        pj.append(p.copy())
        p.clear()
        pi.append(task)

    print(pj)

    [[Sj, Cj, Cjq], Cmax] = calculate(pj, task_number, machine)

    print("\nnr: {} \nCj: {} \nCmax: {}".format(pi, Cj, Cmax))



    # sum = 0
    # for num in pj:
    #     sum += num

    # print("\nnr: {} \nRj: {} \nPj: {} \nQj: {}".format(pi, rj, pj, qj))
    # [[Sj, Cj, Cjq], Cmax] = calculate(rj, pj, qj, task_number)
    # print("\npi: {} \nS: {} \nC: {} \nCq: {}".format(pi, Sj, Cj, Cjq))
    # print("Cmax: {}".format(Cmax))

    # for task in tasks:
    #     Tab.append([pi[task-1], rj[task-1], pj[task-1], qj[task-1]])

    # pi = Schrage(tasks, rj, pj, qj)
    # sort = {x: i for i, x in enumerate(pi)}
    # Tab.sort(key = lambda x: sort[x[0]])

    # [[Sj, Cj, Cjq], Cmax] = calculate([row[1] for row in Tab], [row[2] for row in Tab], [row[3] for row in Tab], task_number)
    # print("\npi: {} \nS: {} \nC: {} \nCq: {}".format(pi, Sj, Cj, Cjq))
    # print("Cmax: {}".format(Cmax))

    # print("\n\n ____________ \n")
    # tasks = [row[0] for row in Tab]
    # rj = [row[1] for row in Tab]
    # pj = [row[2] for row in Tab]
    # qj = [row[3] for row in Tab]
    # pi = Schrage_ptmn(tasks, rj, pj, qj)
    # sort = {x: i for i, x in enumerate(pi)}
    # Tab.sort(key = lambda x: sort[x[0]])

    # [[Sj, Cj, Cjq], Cmax] = calculate([row[1] for row in Tab], [row[2] for row in Tab], [row[3] for row in Tab], task_number)
    # print("\npi: {} \nS: {} \nC: {} \nCq: {}".format(pi, Sj, Cj, Cjq))
    # print("Cmax: {}".format(Cmax))



if __name__ == "__main__":
    main()
