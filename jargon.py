array1 = [3,4,2,4,6]
target = 10
array2 = [8,4,6,7,8]

# def loop():
#     for arr1 in array1:
#         for arr2 in array2:
#             print(arr1,arr2)


# def loop(array):
#     length =  len(array)
#     try:
#         for i in range(length):
#             for arr1 in range(0, length):
#                 if array1[i] + array1[arr1] == target:
#                     return i, arr1
#     except Exception as e:
#         print(e)
        
# loop(array1)

# def concate():
    # array3 = 
    # 

def longestword(string, lists):
    lenght_list = len(lists)
    lenght_string = len(string)
    # count = 0
    dictionary = {}
    
    for i in range(lenght_list):
        count = 0
        for j in range(lenght_string):
            if string[j] in lists[i]:
                count += 1
                dictionary[lists[i]] = count
            else:
                dictionary[lists[i]] = count
                # cases = cases + 1
    print(dictionary)
    print(max(dictionary.keys()))
    # result = max(dict_long.keys())
    for key, value in dictionary.items():
        if value >= max(dictionary.values()):
            return key
    # print(cases)
    return dictionary

s = "abpcplea"
# s = "a"
home = ["ale","apple","monkey","plea"]
longestword(s, home)

dict = {"A":1,"B":2}

print(dict.values())