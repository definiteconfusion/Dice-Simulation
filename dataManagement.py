def count_numbers(input_list, listMax):
    # Initialize a list to hold the counts of numbers from 1 to 100
    counts = [0] * 100
    
    # Iterate through the input list
    for num in input_list:
        # Increment the count for the number encountered
        counts[num - 1] += 1  # Adjust index to match numbers (1 to 100)
    
    return counts