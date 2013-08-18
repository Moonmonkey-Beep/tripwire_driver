import pickle


try:
	number = pickle.load( open( "save.p", "rb" ) )
	if (number > 0):
		print number
except EOFError:
	print ""
	#raise StopIteration