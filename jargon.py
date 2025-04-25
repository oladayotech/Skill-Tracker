array1 = [3,4,2,4,6]
target = 10
# array2 = [8,4,6,7,8]

# def loop():
#     for arr1 in array1:
#         for arr2 in array2:
#             print(arr1,arr2)


def loop(array):
    length =  len(array)
    try:
        for i in range(length):
            for arr1 in range(0, length):
                if array1[i] + array1[arr1] == target:
                    return i, arr1
    except Exception as e:
        print(e)
        
loop(array1)
        