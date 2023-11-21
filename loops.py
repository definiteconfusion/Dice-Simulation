import offload
def dataSet(trials:int=1, pop:int=1):
    numTrials = trials
    initPop = pop

    setupLst = []

    for trials in range(numTrials):
        initPop = 50
        for rounds in range(10**10):
            pop = offload.popSim(initPop)
            if pop == 0:
                setupLst.append(rounds)
                break
            else:
                initPop = pop
    return setupLst