# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    print("ok")
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    print(arrA, arrB)
    a = 0
    b = 0
    if(len(arrA) == 0):
        merged_arr = arrB
    elif(len(arrB) == 0):
        merged_arr = arrA
    else:
        while(a < len(arrA) and b < len(arrB)):
            if(arrA[a] < arrB[b]):
                merged_arr[a+b] = arrA[a]
                a += 1
                # print("a", merged_arr, a)
            elif(arrB[b] < arrA[a]):
                merged_arr[a+b] = arrB[b]
                b += 1
                # print("b", merged_arr, b)
    # print("leftover a", arrA[a:])     
    # print("leftover b", arrB[b:])
    if(a == len(arrA)):
        merged_arr = merged_arr[:a+b] + arrB[b:]
    elif(b == len(arrB)):
        merged_arr = merged_arr[:a+b] + arrA[a:]
    
    return merged_arr




# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # print("arr", arr)
    mid = len(arr)//2
    if(len(arr) <= 1):
        return arr
    else:
        left = arr[:mid]
        right = arr[mid:]
        left_sorted = merge_sort(left)
        right_sorted = merge_sort(right)

    print("merged array", merge(left_sorted, right_sorted))
    return merge(left_sorted, right_sorted)




# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    # for(i = 0; i < len(arr); )

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
