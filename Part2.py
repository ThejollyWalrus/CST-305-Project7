#Mason Hamilton & Dylan Nasser
#CST-305-3:20
#Professor Ricardo Citro
#4/19/2020
#Project 7 Part 2
#Our grouped worked with Tanner Williams and Jared group

#Import libraries used below
import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

#creating all the empty arrays for our functions
arrX = []
arrP = []
arrTime = []
arrNum = []
#setting our rates that we found by hand
arrivalRate = 125
serviceRate = 500

#filling our axis array with 1-15 used as k
axis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#function that finds the utilization and plots it
def utilization(arrivalRate, serviceRate, axis):
    #lamnda / mu
    p = (arrivalRate) / (serviceRate)
    #appending to array p
    arrP.append(p)
    #once the array is full it plots that array
    if len(arrP) == len(axis):
        plt.plot(axis, arrP)
        plt.xlabel('k')
        plt.ylabel('Utilization')
        plt.title('Utilization of Factor k')
        plt.show()

#function that finds the throughput and plots it
def throughput(arrivalRate, axis):
    #throughput x is = to arrival rate above
    x = arrivalRate
    #appending to array arrX
    arrX.append(x)
    #once the array is full it plots that array
    if len(arrX) == len(axis):
        plt.plot(axis, arrX)
        plt.xlabel('k')
        plt.ylabel('Throughput')
        plt.title('Throughput of Factor k')
        plt.show()

#function that finds the average number in the system and plots it
def systemNumber(p, axis):
    #system number equation
    sys = p / (1-p)
    #appending to array arrNum
    arrNum.append(sys)
    #once the array is full it plots that array
    if len(arrNum) == len(axis):
        plt.plot(axis, arrNum)
        plt.xlabel('k')
        plt.ylabel('System Number')
        plt.title('Mean System Number of Factor k')
        plt.show()

#function that find the average time ina system
def systemTime(arrivalRate, serviceRate, axis):
    #system time equation
    sys = (arrivalRate+.25) / (serviceRate)
    #appending to array arrTime
    arrTime.append(sys)
    #once the array is full it plots that array
    if len(arrTime) == len(axis):
        plt.plot(axis, arrTime)
        plt.xlabel('k')
        plt.ylabel('System Time')
        plt.title('Mean System Time of Factor k ')
        plt.show()

#loop that generates all four fucntions
for k in range (1, 16):
    #calling the utilization function buy multiping by k
    utilization(arrivalRate * k, serviceRate * k, axis)
    #calling the thhrougput funciton by multipling arrivalRate by k
    throughput(arrivalRate * k, axis)
    #changingthe val p in the array  back
    p = arrP[k-1]
    #calling the system number
    systemNumber(p, axis)
    #calling the system Time mean by multipling all by k
    systemTime(arrivalRate * k, serviceRate * k, axis)

