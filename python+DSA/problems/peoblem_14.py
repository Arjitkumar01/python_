def missingRanges(arr, lower, upper):
    result = []
    start = lower

    for num in arr:
        if num > start:
            result.append([start, num - 1])

        start = num + 1

    if start <= upper:
        result.append([start, upper])

    return result


arr = [14, 15, 20, 30, 31, 45]
lower = 10
upper = 50

print(missingRanges(arr, lower, upper))