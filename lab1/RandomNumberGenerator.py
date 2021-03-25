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


def calculate(rj, pj, tasks):
    Sj = []
    Cj = []
    Sj.append(max(rj[0], 0))
    Cj.append(Sj[0]+pj[0])
    Cmax = Cj[0]
    for task in tasks[:-1]:
        Sj.append(max(rj[task], Cj[task-1]))
        Cj.append(Sj[task] + pj[task])
        Cmax = max(Cmax, Cj[task])
    return [[Sj, Cj], Cmax]


def main():
    seed = int(input("Enter Z number: "))
    generator = RandomNumberGenerator(seed)
    task_number = int(input("Enter tasks number: "))
    tasks = range(1, task_number + 1)
    rj = []
    pj = []
    pi = []
    Tab = []

    for task in tasks:
        pj.append(generator.nextInt(1, 29))
        pi.append(task)

    sum = 0

    for num in pj:
        sum += num

    for _ in tasks:
        rj.append(generator.nextInt(1, sum))

    print("\nnr: {} \nRj: {} \nPj: {}".format(pi, rj, pj))
    [[Sj, Cj], Cmax] = calculate(rj, pj, tasks)
    print("\npi: {} \nS: {} \nC: {}".format(pi, Sj, Cj))

    for task in tasks:
        Tab.append([pi[task-1], rj[task-1], pj[task-1]])

    Tab.sort(key=lambda x: (x[1]))
    [[Sj, Cj], Cmax] = calculate([row[1] for row in Tab], [row[2] for row in Tab], tasks)
    print("\npi: {} \nS: {} \nC: {}".format([row[0] for row in Tab], Sj, Cj))


if __name__ == "__main__":
    main()


