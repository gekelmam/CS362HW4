import math

def cubeFunc(a):
	#print("type a = " + str(type(a)))
	if (type(a) != int and type(a) != float):
		raise ValueError("Input has to be an int or float")
	elif (a <= 0):
		raise ValueError("Number has to be greater than 0")
	return (math.pow(a, 3))