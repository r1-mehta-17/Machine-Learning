import numpy as np
# rounds of the array to a given number of decimal places
# random.normal creates an array whose mean = 1.75, standard deviation = 0.20 and number of elements in the array = 500
np_height = np.round(np.random.normal(1.75,0.20,50),2)
np_weight = np.round(np.random.normal(65,0.30,50),2)
height = list(np_height)
weight = list(np_weight)
import matplotlib.pyplot as plt
plt.plot(height,weight)
plt.show()
