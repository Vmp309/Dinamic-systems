# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:34:50 2020

@author: Victoria Monteiro Pontes
"""

from pylab import *

t, y = loadtxt('ballmotion.txt', usecols = [0, 1], unpack=True)

#Plotting graph, question a
#plot(t, y)
#xlabel('t(s)')
#ylabel('y(m)')


#Calculating time interval
dt = t[1] - t[0]

#Plotting velocity question b
v = (y[1:] -y[0:-1])/dt

#Plotting average velocity
#plot(v)
#ylabel('v(m/s)')



#Calulating the minimal and maximum velocity
Vmin = min(v)
Vmax = max(v)
print (Vmin)
print (Vmax)

#Calculating arithmetic mean of velocities question d
av = sum(v)/len(v)
print(av)

#Calculating the instant aprox. that the velocity is equal to the arithmetic 
#mean of velocities




