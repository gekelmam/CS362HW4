def fullName(first, last):
	if(type(first) != str or type(last) != str):
		raise ValueError("Input has to be a string")
	return str(first) + " " + str(last)
