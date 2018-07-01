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
def gradient(function,arguments,weights):
    gradients = []
    functionBase = function(arguments,weights)
    h = 0.001 #Spread

    for i in range(len(arguments)):
        arguments[i] += h
        gradients.append(float((function(arguments,weights)-functionBase)/h))
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
def updateParameters(function,arguments,stepSize,weights):
    grad = gradient(function,arguments,weights)
    for i in range(len(arguments)):
        arguments[i] = arguments[i] - stepSize*grad[i]
    return arguments


def penaltyIneq(value,weight):
    if value < 0:
        return 0
    else:
        return weight*value**3

def penaltyEq(value,weight):
    return weight*value**2

def checkConstraint(func):
    if func<1:
        return True
    else:
        return False

def checkAllConstraints(eq):
    increments = []
    for e in eq:
        if checkConstraint(e):
            increments.append(False)
        else:
            increments.append(True)
    return increments

def concatFunctions(x,weights):
    s = f(x)
    eqVals = eq(x)
    for i in range(len(eqVals)):
        s += penaltyEq(eqVals[i],weights[i])

    return s


#Optimizer of an unconstrainted problem (call this to solve)
def optimizeUnconstrained(function,startVector,weights):

    vector = startVector
    vectorLast = []
    values = []

    for element in vector:
        vectorLast.append(element+1)

    tolerance = 1/10**10
    difference = 1
    step = .00001
    lastValue = function(startVector,weights)
    iterations = 0

    while difference > tolerance:
        vector = updateParameters(function,vector,step,weights)
        difference = abs(lastValue-function(vector,weights))
        iterations += 1
        lastValue = function(vector,weights)
        vectorLast = vector
        values.append(function(vector,weights))

    opVal = function(vector,weights)

    #print("Verdi på objektfunksjonen:",'{:f}'.format(function(vector,weights)))
    #print("Optimal vektor:",vector)
    #print("Antall iterasjoner:",iterations)

    return opVal,values,vector

#Update constraints if they are violated
def updateConstraints(array,weights):
    for i in range(len(array)):
        if array[i]==False:
            weights[i] = weights[i]*10
    return weights

#Check if all constraints are satisfied
def checkConvergence(eq):
    array = checkAllConstraints(eq)
    for a in array:
        if not a:
            return False
    return False

#Function to perform constrained optimization by the penalty method
def optimizeConstrained(function,startVector,eqFunc):

    #Dummy value to set the number of constraints
    eqVal = eqFunc(startVector)

    #Start vector of weights
    weights = [1]*len(eqVal)

    #Iterator on the outer loop
    i = 0

    #Parameters
    lastValue = concatFunctions(startVector,weights)
    difference = 10
    tolerance = 5

    #Initializing
    convergence = False

    while not convergence and difference > tolerance:

        print("Optimerer runde",i)

        #Optimizing the unconstrained problem
        opVal, values, startVector = optimizeUnconstrained(concatFunctions,startVector,weights)

        difference = abs(opVal-lastValue)

        #Checking if we have reached a convergence
        if checkConvergence(eqFunc(startVector)) or difference < tolerance:
            convergence = True
        else:
            #Checking which constraints should be updated
            array = checkAllConstraints(eqFunc(startVector))

            #Calculating new weights
            weights = updateConstraints(array,weights)

            #New last value
            lastValue = concatFunctions(startVector,weights)

            i += 1

    print("Verdi på objektfunksjonen:",'{:f}'.format(function(startVector,weights)))
    print("Optimal vektor:",startVector)
    print("Antall iterasjoner:",i)


#---------------------Tests--------------------#

def f(x,*args):
    s = 0
    for i in x:
        s += i**2
    return s

def eq(x):
    values = []
    for i in x:
        values.append(i**2-100)
    return values

x = [-1]*20
y = [120,120,120]

optimizeConstrained(f,x,eq)
