def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)


def partition(arr, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and arr[i] < arr[pivot]:
            i += 1
        while j > pivot and arr[j] > arr[pivot]:
            j -= 1
        if j <= i:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j



