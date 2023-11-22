def count_numbers(input_list, listMax):
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
    return [counts, likelyVal, valIndex, counts[10]]
