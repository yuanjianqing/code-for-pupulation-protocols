import random
import math
import matplotlib.pyplot as plt
import numpy as np


def allX(array):
    size = len(array)
    product = 1
    for i in range(size):
        product = array[i] * product
        if product == 0:
            return 0
    return 1


def exchangeMessage(array, a, b, numX):
    if array[a] == 1 and array[b] == 0:
        array[b] = 1
        return numX + 1
    elif array[a] == 0 and array[b] == 1:
        array[a] = 1
        return numX + 1
    elif array[a] == 1 and array[b] == 1:
        return numX
    else:
        return numX


# interaction, and every element of the array may interact with any other element, return the number of X agents
def interaction(array, numX):
    size = len(array)
    ifInterchanged = [0] * size

    for i in range(size - 1):  # pairs are two elements
        while ifInterchanged[i] == 1:  # to find a element which has not changed
            if i <= size - 2:
                i = i + 1
            else:
                return numX
        interactionIndex = random.randint(i + 1, size - 1)
        while (
            ifInterchanged[interactionIndex] == 1
        ):  # to find a element which has not changed
            interactionIndex = random.randint(i + 1, size - 1)
        numX = exchangeMessage(array, i, interactionIndex, numX)
        ifInterchanged[i] = 1
        ifInterchanged[interactionIndex] = 1
    return numX

def interactionOnePair(array, numX):
    size = len(array)
    interactionIndex1 = random.randint(0, size - 1)
    interactionIndex2 = random.randint(0, size - 1)
    numX =  exchangeMessage(array, interactionIndex1, interactionIndex2, numX)
    return numX

def main(k):
    size = k
    array = [1] + [0] * (size - 1)
    numX = 1
    times = 0
    if numX < size:
        while numX < size:
            numX = interactionOnePair(array, numX)
            #numX = interaction(array, numX)

            #print("number of x:",numX,"number of y:", size - numX)

            times = times + 1
    print(size, times)
    return size, times
    #plt.plot(size, times)
    #plt.show
    #fig, ax = plt.subplots()             # Create a figure containing a single Axes. # Plot some data on the Axes.
    #plt.show()                           # Show the figure.


if __name__ == "__main__":

    x, y = [], []
    for i in range(1,25):
        k = 2**i
        a, b = main(k)
        x.append(a)
        y.append((b/a)**2)
        
    plt.plot(x, y)
    plt.show()
    print("end")
