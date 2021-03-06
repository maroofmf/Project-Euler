'''
Author: Maroof
Problems from Project Euler
Please uncomment the code you wish to run.
'''

# ------------------------------------------------------------------------------------------------------------------- #
# Problem 1: Multiples of 3 and 5
# ------------------------------------------------------------------------------------------------------------------- #

# upperBound = 1000
# sum = 0;
# multiples_3 = 0
# multiples_5 = 0
# multiplicative_value = 1
#
# while(multiplicative_value <= upperBound):
#     multiples_3 = 3 * multiplicative_value
#     multiples_5 = 5 * multiplicative_value
#     if multiples_5 >= upperBound and multiples_3 >= upperBound:
#         break;
#     if multiples_5%3 ==0 or multiples_5 >= upperBound:
#         sum = sum + multiples_3
#     else:
#         sum = sum + multiples_3 + multiples_5
#     multiplicative_value = multiplicative_value + 1
#
# print(sum)

# ------------------------------------------------------------------------------------------------------------------- #
# Problem 2: Even Fibonacci numbers
# ------------------------------------------------------------------------------------------------------------------- #

# import math
# import scipy.constants as constants
#
# goldenRatio = constants.golden
#
# def fibonacciGen(n):
#         return (goldenRatio ** n - (-goldenRatio) ** -n)/math.sqrt(5)
#
# upperBound = 4000000
# # Fibonacci sequence - o,o,e,o,o,e,o,o,e .... even nubers are in the multiples of 3!
# sum = 0
#
# for i in range(1,upperBound):
#     nValue = i * 3
#     fibonacciNumber = round(fibonacciGen(nValue))
#     if fibonacciNumber >= upperBound:
#         break;
#     sum = sum + fibonacciNumber
#
# print(sum)

# ------------------------------------------------------------------------------------------------------------------- #
# Problem 3: Largest Prime Factor
# -------------------------------------------------------------------------------------------------------------------

import sympy
import time
import multiprocessing as mp
import math

global number
number = 1973

#AKS Primality test

def isPrime():
    pool = mp.Pool(10)
    blocks = math.ceil(number/30)
    # blocks = 2
    for index in range(1,blocks+1):
        poolOutput = pool.map(divisibilityTest,range(math.ceil(((number-1)/blocks)*blocks),max(math.floor(((number-1)/blocks)*(blocks-1)),1),-1))
        if 'Composite' in poolOutput:
            return('Composite')
    return ('Prime')

def divisibilityTest(args):
    coefficient = (sympy.binomial(number,args)/number)
    if coefficient %1 != 0:
        return('Composite')
    return('Prime')



def isPrime2():
    for i in range(number-1 , 1, -1):
        coefficient = (sympy.binomial(number,i)/number)
    if coefficient %1 != 0:
        return('Composite')
    return('Prime')


startTime = time.time()
print('The answer for method 1:' + isPrime())
totalTime = (time.time()-startTime)
print('Total Time for method 1:', totalTime)

startTime = time.time()
print('The answer for method 2:' + isPrime2())
totalTime = (time.time()-startTime)
print('Total Time for method 2:', totalTime)


