def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            nextIndex = j + 1
            if array[j] > array[nextIndex]:
                smallernum = array[nextIndex]
                largernum = array[j]
                array[nextIndex] = largernum
                array[j] = smallernum
    return array


# a test case
print(bubblesort([9, 8, 7, 4, 5, 6, 12, 10, 3]))
