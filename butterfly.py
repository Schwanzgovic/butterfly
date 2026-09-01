import numpy as np
import pandas as pd
#import scikit-learn as sklearn
import matplotlib.pyplot as plt

def observationCounter(array):
    observations = ()
    for i in array:
        if type(i) == 'int':
            observations += i
        else:
            observations += 1 
    return observations 

def extractMonth(array):
    monthArray = []
    for i in array:
        month = i.split('-')[1]
        monthArray.append(month)
    return np.array(monthArray) 


df = pd.read_csv("./butterfly.csv")
print(df)
#print()
#plot observations over time 
x = extractMonth(df["Startdatum"])
observationsPerMonth = np.zeros(12)

for i in x:
    observationsPerMonth[int(i) - 1] += 1
print(x)
#y = observationCounter(df["Antal"])
plt.plot(observationsPerMonth)
plt.show()

