#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 18:06:59 2018

Gradient descent solver


@author: Harald Hoyem
"""
from copy import deepcopy
import matplotlib.pyplot as plt

#Calculate gradient
def gradient(function,arguments):
    gradients = []
    functionBase = function(arguments)
    h = 0.001 #Spread

    for i in range(len(arguments)):
        arguments[i] += h
        gradients.append(float((function(arguments)-functionBase)/h))
        arguments[i] -= h

    return gradients

#Function to multiply two vectors
def multiplyVectors(vector1,vector2):
    value = 0
    for i in range(len(vector1)):
        value += vector1[i]*vector2[i]

    return value

#Find distance
def euclideanDistance(vector1,vector2):
    distance = 0
    for i in range(len(vector1)):
        distance += (vector1[i]-vector2[i])**2
    return distance

#Find the difference of two vectors
def differenceVectors(vector1,vector2):
    vector = []
    for i in range(len(vector1)):
        vector.append(vector1[i]-vector2[i])
    return vector

#Step size determination (does not work yet)
def stepSize(function,arguments1,arguments2):
    #steg

    #Steg 1
    #Beregning arguments1 - arguments2
    vektorDifferanse = differenceVectors(arguments1,arguments2)
    #Steg 2
    #Beregnin function(arguments1) -  function arguments2
    gradientDifferanse = differenceVectors(gradient(function,arguments1),gradient(function,arguments2))
     #Steg 3
    #Beregning multiplyVectors(Steg1, Steg2)
    teller = multiplyVectors(vektorDifferanse,gradientDifferanse)

    #Steg 4
    #Beregning euclideanDistance(function(arguments1),function arguments2)
    nevner = multiplyVectors(gradient(function,arguments1),gradient(function,arguments2))

    return teller/nevner

#Update parameters in optimization
def updateParameters(function,arguments,stepSize):
    grad = gradient(function,arguments)
    for i in range(len(arguments)):
        arguments[i] = arguments[i] - stepSize*grad[i]
    return arguments

#Optimizer (call this to solve)
def optimize(function,startVector):

    vector = startVector
    vectorLast = []
    values = []

    for element in vector:
        vectorLast.append(element+1)

    tolerance = 1/10**10
    difference = 1
    step = .001
    lastValue = function(startVector)
    iterations = 0

    while difference > tolerance:
        vector = updateParameters(function,vector,step)
        difference = abs(lastValue-function(vector))
        iterations += 1
        lastValue = function(vector)
        vectorLast = vector
        values.append(function(vector))

    print("Verdi på objektfunksjonen:",'{:f}'.format(function(vector)))
    print("Optimal vektor:",vector)
    print("Antall iterasjoner:",iterations)

    return values



'''
def f(x):
    return (1-x[0])**2 + 100*(x[1]-x[0]**2)**2

TEST CODE

x = [-1,-1]
y = [120,120,120]


values = optimize(f,x)

plt.plot(values)
plt.show()
'''
