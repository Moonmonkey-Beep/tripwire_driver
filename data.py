import pickle


while True:
	Try:
		number = pickle.load( open( "save.p", "wb" ) )
		print number
      