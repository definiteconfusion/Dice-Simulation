import pandas as pd
def count_numbers(input_list, listMax):
    
    counts_series = pd.Series(input_list)

    # Calculate median, quartiles, and standard deviation
    median = counts_series.median()
    mean = counts_series.mean()
    first_quartile = counts_series.quantile(0.25)
    third_quartile = counts_series.quantile(0.75)
    standard_deviation = counts_series.std()
    
    
    # Initialize a list to hold the counts of numbers from 1 to 100
    counts = [0] * listMax * 5
    # Iterate through the input list
    for num in input_list:
        # Increment the count for the number encountered
        counts[num - 1] += 1  
    for cleanup in range(len(counts)):
        if cleanup > 100:
            counts.pop(101)
    likelyVal = 0
    valIndex = 0
    for values in range(len(counts)):
        if counts[values] > likelyVal:
            likelyVal = counts[values]
            valIndex = values
    return [counts, likelyVal, valIndex, counts[10], median, first_quartile, third_quartile, standard_deviation, mean]
