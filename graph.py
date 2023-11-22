import matplotlib.pyplot as plt
import dataManagement
import loops

def plot_bar_graph(data_list):
    x = range(len(data_list))  # Generating x values based on the length of the input list
    plt.plot(x, data_list)  # Creating the bar graph
    plt.xlabel('Index')  # Label for the x-axis
    plt.ylabel('Number of Occurrences')  # Label for the y-axis
    plt.title('Sim Graph')  # Title of the graph
    plt.axvline(x=11, color='red')  # Adjust color and linestyle as needed
    plt.show()  # Displaying the graph
