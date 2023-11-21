import dataManagement
import loops
import graph

def trial(trial:int, population:int):
    graph.plot_bar_graph(
        dataManagement.count_numbers(
            loops.dataSet(trial,population), population * 2
            )
        )