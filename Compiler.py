import dataManagement
import loops
import graph
import click

def trial(trial:int, population:int):
    
    dataset = dataManagement.count_numbers(loops.dataSet(trial,population), population * 2)
    
    
    click.secho(f'σ = {dataset[1]} \n μ = {dataset[0]}', bg='blue')
    
    
    graph.plot_bar_graph(
        dataset[4]
        )