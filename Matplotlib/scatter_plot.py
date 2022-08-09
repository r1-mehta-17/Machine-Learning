import numpy as np
# rounds of the array to a given number of decimal places
# random.normal creates an array whose mean = 1.75, standard deviation = 0.20 and number of elements in the array = 500
np_height = np.round(np.random.normal(1.75,0.20,50),2)
np_weight = np.round(np.random.normal(65,0.30,50),2)
# Converting numpy array to lists
height = list(np_height)
weight = list(np_weight)
# Calculating the mean of the numpy arrays
hmean = np.mean(np_height)
wmean = np.mean(np_weight)
# Importing matplotlib.pyplot
import matplotlib.pyplot as plt
# Building scatter plot of the data we have
plt.scatter(height,weight)
# Labeling x and y axes
plt.xlabel('Height')
plt.ylabel('Weight')
# Giving the plot a title
plt.title('Body Mass Index')
# Displaying the grid
plt.grid(True)
# Displaying the mean BMI as text on the plot
plt.text(hmean,wmean-1,'Mean BMI')
# Modifying the markers/ticks on the y axis as per our requirement
plt.yticks([62,63,64,65,66,67])
# Displaying the plot. This output can be seen in the readme file in the matplotlib folder 
plt.show()
