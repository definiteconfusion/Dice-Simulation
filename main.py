import dataManagement
import loops
import graph


graph.plot_bar_graph(
    dataManagement.count_numbers(
        loops.dataSet(5000,100),5000
        )
    )