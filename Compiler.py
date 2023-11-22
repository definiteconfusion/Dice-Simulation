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
    median =  mangementlst[4]
    first_quartile =  mangementlst[5]
    third_quartile =  mangementlst[6]
    standard_deviation =  mangementlst[7]
    mean = mangementlst[8]
    
    click.secho(f"""
                AVG Rounds: {numDex} \n 
                NMBR Occurrences: {likelyNum} \n 
                Median: {median}\n
                Mean: {mean} \n
                Standard Deviation: {standard_deviation}\n
                First Quartile: {first_quartile}\n
                Third Quartile: {third_quartile} \n
                RND Eleven: {elevenData} \n
                SD Off: {(mean - 11) / standard_deviation}""", fg='blue')
    
    graph.plot_bar_graph(
        dataset
        )