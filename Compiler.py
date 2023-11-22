import dataManagement
import loops
import graph
import click

def trial(trial:int, population:int):
    
    mangementlst = dataManagement.count_numbers(loops.dataSet(trial,population), population * 2)   
    
    dataset = mangementlst[0]
    likelyNum = mangementlst[1]
    numDex = mangementlst[2]
    elevenData = mangementlst[3]
    
    click.secho(f"AVG Rounds: {numDex} \n NMBR Occurrences: {likelyNum} \n \n RND Eleven: {elevenData}", fg='blue')
    
    graph.plot_bar_graph(
        dataset
        )