import random


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

def main(k):
    size = k
    array = [1] + [0] * (size - 1)
    numX = 1
    times = 0
    if numX < size:
        while numX < size:
            numX = interaction(array, numX)
            times = times + 1
    print(size, times)


if __name__ == "__main__":
    for i in range(1, 12):
        inputSize = 2 ** i
        main(inputSize)
        
    print("end")
