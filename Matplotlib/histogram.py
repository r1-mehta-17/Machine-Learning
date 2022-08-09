import numpy as np
# rounds of the array to a given number of decimal places
# random.normal creates an array whose mean = 1.75, standard deviation = 0.20 and number of elements in the array = 500
np_height = np.round(np.random.normal(1.75,0.20,50),2)
height = list(np_height)
import matplotlib.pyplot as plt
#histogram is built only for one attribute and the frequencies of the data in this attribute are displayed as bars 
plt.hist(height)
plt.show()
