def sum(arr):
    if (len(arr) == 1):
        return arr[0]
    else:
        return sum(arr[1:]) + arr[0]

print(sum([1,2,3,4,5]))