import matplotlib.pyplot as plt
import dataManagement
import loops

def plot_bar_graph(data_list):
    x = range(len(data_list))  # Generating x values based on the length of the input list
    plt.bar(x, data_list)  # Creating the bar graph
    plt.xlabel('Index')  # Label for the x-axis
    plt.ylabel('Values')  # Label for the y-axis
    plt.title('Bar Graph')  # Title of the graph
    plt.show()  # Displaying the graph
