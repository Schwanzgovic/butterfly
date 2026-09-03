import numpy as np
import pandas as pd
#import scikit-learn as sklearn
import matplotlib.pyplot as plt

#wrong atm change later "Antal" is strings
def totalObservationCounter(array):
    observations = 0
    for i in array:
        if  i == "noterad":
            observations += 1
        else:
            observations += int(i) 
    return observations 

#replace all "noterad" by a one 
def observationToInt(array):
    intObservations = np.ones(len(array))
    for i in range(len(array)):
        if array[i] == "noterad":
            continue
        else: 
            intObservations[i] = int(array[i])
    return intObservations
            


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

#for i in x:
 #   observationsPerMonth[int(i) - 1] += 1
print(x)

#observations per month with actual values
#for i in range(len(x)):
#    observationsPerMonth[int(x[i]) - 1] += 
y = observationToInt(df["Antal"])
totalObservations = totalObservationCounter(df["Antal"])
empiricalDensity = y/totalObservations

print(empiricalDensity)
#print(df["Antal"])
print(y)

#note that the extra information in the number of observed butterflys doesnt seem to change the distribution
#model idea: assume underlying probability density and approxamite it by empirical density function (observationsPerMonth/totalObservations)

#new idea: pca to find good predictors (but predictors for what??)

#another idea: scatter plot with geographical positions (bigger dots reprensent more sightings) and colour them according to specific (climate?) zones

for i in range(len(x)):
    observationsPerMonth[int(x[i]) - 1] += y[i]

plt.plot(observationsPerMonth)

#scatter plot showing the sightings on the 'map'
#plt.scatter(df["Ost"], df["Nord"])

plt.show()
