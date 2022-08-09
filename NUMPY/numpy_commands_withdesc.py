import numpy as np
# rounds of the array to a given number of decimal places
# random.normal creates an array whose mean = 1.75, standard deviation = 0.20 and number of elements in the array = 500
height = np.round(np.random.normal(1.75,0.20,500),2)
weight = np.round(np.random.normal(65,0.30,500),2)
# we can merge these 2 arrays to form a 2D matrix using np.column_stack((column1,column2))
body = np.column_stack((height,weight))
# calculation of BMI by applying operations to 2 np arrays height and weight which were merged to form a matrix body 
bmi = body[:,1] / body[:,0] ** 2
# using numpy functions std, mean, median, and even correlation coefficients to find the relation of heights with the weight of a person
bmi_std = np.std(bmi)
bmi_mean = np.mean(bmi)
bmi_median = np.median(bmi)
body_corr = np.corrcoef(body[:,0],body[:,1])
print("Standard Deviation of BMI(Body Mass Index) : ",str(bmi_std))
print("Mean of BMI(Body Mass Index) : ",str(bmi_mean))
print("Median of BMI(Body Mass Index) : ",str(bmi_median))
print("Correlation Coefficients of body : ")
print(body_corr)
# Shape attribute represnts the matrix size, i.e., the number of rows and number of columns
print(body.shape)

# OUTPUT :
# Standard Deviation of BMI(Body Mass Index) :  4.860859614817757
# Mean of BMI(Body Mass Index) :  21.520980220318112
# Median of BMI(Body Mass Index) :  21.07603959352336
# Correlation Coefficients of body : 
# [[ 1.         -0.02361888]
#  [-0.02361888  1.        ]]
# (500, 2)
