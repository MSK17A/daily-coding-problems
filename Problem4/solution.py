import numpy as np

def solution(arr):
	n = len(arr)
	visited_flag = np.zeros(n)

	"""
	Make x as min, take left and right

	Check right or left number (if right number is there then this number 
	is in succcession)
	if left number is there then it is succession and I must find lower number that can be fitted in the array

	another solution is to get the min and max
	[1, 3, 4, 5]

	5 > len(array)
	ignore 5
	1+1

	[2, 4, 5, 6]

	6 > len(array)
	5 > len(array)

	min 2, max 4
	min+1 = 3
	"""
	min = arr[0]
	for x in range(n):
		if(arr[x] < min and arr[x] < n and arr[x] > 0):
			min = arr[x]

	max = arr[0]
	for x in range(n):
		if(arr[x] > max and arr[x] < n):
			max = arr[x]

	if min > 1:
		return min-1
	elif min == 1:
		return max +1
	return min
print(solution([3, 4, -1, 1]))