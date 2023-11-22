def count_numbers(input_list, listMax):
    # Initialize a list to hold the counts of numbers from 1 to 100
    counts = [0] * listMax
    
    # Iterate through the input list
    for num in input_list:
        # Increment the count for the number encountered
        counts[num - 1] += 1  # Adjust index to match numbers (1 to 100)
    for cleanup in range(len(counts)):
        if cleanup > 100:
            counts.pop(101)
    import pandas as pd
    counts_series = pd.Series(counts)

# Calculate median and quartiles
    median = counts_series.median()
    first_quartile = counts_series.quantile(0.25)
    third_quartile = counts_series.quantile(0.75)
    standard_deviation = counts_series.std()

    lst = [
        median,
        standard_deviation,
        first_quartile,
        third_quartile,
        counts
    ]
    
    return lst
