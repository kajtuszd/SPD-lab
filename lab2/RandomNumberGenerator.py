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


def calculate(rj, pj, qj, task_number):
    Sj = []
    Cj = []
    Cjq = []
    Sj.append(max(rj[0], 0))
    Cj.append(Sj[0] + pj[0])
    Cjq.append(Cj[0] + qj[0])
    Cmax = Cjq[0]
    for j in range(1, task_number):
        Sj.append(max(rj[j], Cj[j-1]))
        Cj.append(Sj[j] + pj[j])
        Cjq.append(Cj[j] + qj[j])
        Cmax = max(Cmax, Cjq[j])
    return [[Sj, Cj, Cjq], Cmax]


def Schrage(tasks, rj, pj, qj):
    k = 1
    G = []
    tasks = list(tasks)
    N = tasks
    tasks = []
    t = min(rj)
    while (len(G)) or (len(N)):
        while (len(N)) and (min(rj) <= t):
            j = rj.index(min(rj))
            rj[j] = 99999999999
            G.append(j + 1)
            N.remove(j + 1)
        if len(G):
            j = qj.index(max([qj[i - 1] for i in G])) + 1
            qj[j - 1]= - 99999999999
            G.remove(j) 
            tasks.append(j)
            t += pj[j - 1]
            k += 1
        else:
            t = min(rj)
    return tasks



def Schrage_ptmn(tasks, rj, pj, qj):
    Ng = []
    tasks = list(tasks)
    Nn = tasks
    tasks = []
    l = 0 
    qj[0] = 99999999999
    t = min(rj)
    Cmax = 0
    while (len(Ng)) or (len(Nn)):
        while (len(Nn)) and (min(rj) <= t):
            j = rj.index(min(rj))
            Ng.append(j + 1)
            Nn.remove(j + 1)
            if qj[j-1] > qj[l]:
                pj[l] = t - rj[j-1]
                t = rj[j-1]
                if pj[l] > 0:
                    Ng.append(j + 1)  
            rj[j] = 99999999999          
        if len(Ng):
            j = qj.index(max([qj[i - 1] for i in Ng])) + 1
            Ng.remove(j)
            tasks.append(j)
            l = j # +1 ??
            t += pj[j - 1]
            Cmax = max(Cmax, t + qj[j - 1])
            qj[j - 1] = - 99999999999
        else:
            t = min(rj)
    return tasks



def main():
    seed = int(input("Enter Z number: "))
    generator = RandomNumberGenerator(seed)
    task_number = int(input("Enter tasks number: "))
    tasks = range(1, task_number + 1)
    rj, pj, qj, pi, Tab = [], [], [], [], []

    for task in tasks:
        pj.append(generator.nextInt(1, 29))
        pi.append(task)

    sum = 0
    for num in pj:
        sum += num

    for _ in tasks:
        rj.append(generator.nextInt(1, sum))

    X = sum 
    for _ in tasks:
        qj.append(generator.nextInt(1, X))
    
    print("\nnr: {} \nRj: {} \nPj: {} \nQj: {}".format(pi, rj, pj, qj))
    [[Sj, Cj, Cjq], Cmax] = calculate(rj, pj, qj, task_number)
    print("\npi: {} \nS: {} \nC: {} \nCq: {}".format(pi, Sj, Cj, Cjq))
    print("Cmax: {}".format(Cmax))

    for task in tasks:
        Tab.append([pi[task-1], rj[task-1], pj[task-1], qj[task-1]])

    pi = Schrage(tasks, rj, pj, qj)
    sort = {x: i for i, x in enumerate(pi)}
    Tab.sort(key = lambda x: sort[x[0]])

    [[Sj, Cj, Cjq], Cmax] = calculate([row[1] for row in Tab], [row[2] for row in Tab], [row[3] for row in Tab], task_number)
    print("\npi: {} \nS: {} \nC: {} \nCq: {}".format(pi, Sj, Cj, Cjq))
    print("Cmax: {}".format(Cmax))

    print("\n\n ____________ \n")
    rj = [row[1] for row in Tab]
    pj = [row[2] for row in Tab]
    qj = [row[3] for row in Tab]
    pi = Schrage_ptmn(tasks, rj, pj, qj)
    sort = {x: i for i, x in enumerate(pi)}
    Tab.sort(key = lambda x: sort[x[0]])

    [[Sj, Cj, Cjq], Cmax] = calculate([row[1] for row in Tab], [row[2] for row in Tab], [row[3] for row in Tab], task_number)
    print("\npi: {} \nS: {} \nC: {} \nCq: {}".format(pi, Sj, Cj, Cjq))
    print("Cmax: {}".format(Cmax))



if __name__ == "__main__":
    main()
