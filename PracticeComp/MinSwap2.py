import copy

def minimumSwaps(arr):
    temp = {a: i for i, a in enumerate(arr)}
    swaps = 0
    for i in range(len(arr)):
        actual, expected = arr[i], i + 1
        actual_i, expected_i = i, temp[expected]
        if actual != expected:
            arr[actual_i] = expected
            arr[expected_i] = actual
            temp[actual] = expected_i
            temp[expected] = actual_i
            swaps += 1
    return swaps


n = int(input())
arr = list(map(int, input().split(' ')))
swap = minimumSwaps(arr)
print(swap)