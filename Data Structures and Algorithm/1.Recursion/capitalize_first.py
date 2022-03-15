def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].capitalize())
    return result + capitalizeFirst(arr[1:])


print(capitalizeFirst(['car', 'banana', 'lemon']))
