import pickle


try:
	number = pickle.load( open( "/opt/ninja/drivers/save.p", "rb" ) )
	if (number > 0):
		print number
except EOFError:
	print "Armed"
	#raise StopIteration