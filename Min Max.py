class Min_Max:

    def __init__(self, listt):

        self.listt = listt

        self.length = len(listt)

    def selection(self, element, indexx):

        temp = []

        for i in range(self.length):

            if self.listt[i] != element:





n = int(input())

listt = []

for i in range(n):

    a= int(input())

    listt.append(a)

randomm = Min_Max(listt)

for j in range(len(listt)):

    randomm.selection(listt[j], j)

