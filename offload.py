import random
def popSim(pop):
    initPop = pop
    finalPop = initPop
    for people in range(initPop):
        diceRoll = random.randint(1, 6)
        if diceRoll == 6:
            finalPop = finalPop - 1
    return finalPop

