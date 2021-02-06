def avgFunc(arr):
	length = len(arr)
	average = 0
	if (length < 1):
		raise ValueError("Number of elements has to be greater than 0")
	else:
		for x in range(length):
			if (type(x) != int and type(x) != float):
				raise ValueError("Input has to be an int or float")
			average += arr[x]
	return (average/length)