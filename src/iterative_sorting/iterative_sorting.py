# TO-DO: Complete the selection_sort() function below 
arr = [1,9,4,3,5,6,7,9,44,5,67,2]
arr1 = []
def selection_sort( arr ):
	print("selection arr", arr)
	# loop through n-1 elements
	for i in range(0, len(arr) - 1):
		cur_index = i
		smallest_index = cur_index

		# TO-DO: find next smallest element
		# (hint, can do in 3 loc) 
		for j in range(cur_index, len(arr)):
			if arr[j] <  arr[smallest_index]:
				smallest_index = j

		# TO-DO: swap
		temp = arr[cur_index]
		arr[cur_index] = arr[smallest_index]
		arr[smallest_index] = temp

	return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
	#loop through arr
	#for i in arr, check if it is less than i at index+1
	 #if yes, do nothing
	 #if no, swap places
	if(len(arr) == 0):
		return arr
	did_swap = True
	print("bubble arr", arr)
	while did_swap == True:
		counter = 0
		# print("loop")
		for i in range(len(arr) - 1):
			# print(i, arr[i], arr[i+1])
			if(arr[i] > arr[i + 1]):
				counter = 0
				temp = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp
				i = 0
			else:
				counter += 1
				# print(counter, len(arr)-2)
				# print(arr)

			if counter >= int(len(arr) - 2):
			    did_swap = False

	return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

	return arr

# print("return", bubble_sort(arr))
# print("selection", selection_sort(arr))