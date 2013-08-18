import pickle
while True:   

	try:
		number = pickle.load( open( "save.p", "rb" ) )
		print number
	except EOFError:
		print "error"
		#raise StopIteration