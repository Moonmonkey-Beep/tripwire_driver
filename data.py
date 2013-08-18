import pickle


try:
  number = pickle.load( open( "save.p", "rb" ) )
  print number
except EOFError:
  raise StopIteration

