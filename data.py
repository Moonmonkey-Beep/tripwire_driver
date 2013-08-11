try:
  from cPickle import dumps, loads
except ImportError:
  from pickle import dumps, loads


while True:                                     
                                  
        number = pickle.load( open( "save.p", "wb" ) )
        print number
      	