def countingSort(arr):
    # for array in range of 0 to 99
    count = [0] * 100
    for number in arr:
        count[number] += 1
    return count
