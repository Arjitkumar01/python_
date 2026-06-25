# quick sort:

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  # last element as pivot

    left = []
    right = []

    for i in arr[:-1]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [8, 3, 5, 1, 9, 6, 2, 7, 4, 10]

print(quick_sort(arr))


# using two pointer

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[low]  # first element as pivot

    left = low + 1
    right = high

    while True:

        while left <= right and arr[left] <= pivot:
            left += 1

        while left <= right and arr[right] > pivot:
            right -= 1

        if left > right:
            break

        arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]

    return right


arr = [8, 3, 5, 1, 9, 6, 2, 7, 4]

quick_sort(arr, 0, len(arr) - 1)

print(arr)