def insertionSort1(n, arr):
    defaultIndex = n-1
    result = arr[defaultIndex]
    for i in range(defaultIndex, -1, -1):
         if result < arr[i-1] and i >= 1:
            arr[i] = arr[i-1]
            print(' '.join(str(x) for x in arr))
         else: 
            arr[i] = result
            print(' '.join(str(x) for x in arr))
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
