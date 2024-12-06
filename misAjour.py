import random


allNumOrange=[]
allNumFree=[]
allNumExpresso=[]


def orange():
    numOrange=[77]
    
    for i in range (100):
        for j in range(7):
            a=random.randint(1, 9)
            numOrange.append(a)
        chaine = ''.join(str(x) for x in numOrange)
        num=f"{i+1}-{chaine}"
        allNumOrange.append(num)
        numOrange=[77]
        for element in allNumOrange:
            print(f'{element}\n')


def free():
    numFree=[76]
    
    for i in range (100):
        for j in range(7):
            a=random.randint(1, 9)
            numFree.append(a)
        chaine = ''.join(str(x) for x in numFree)
        num=f"{i+1}-{chaine}"
        allNumFree.append(num)
        numFree=[76]
        for element in allNumFree:
            print(f'{element}\n')

