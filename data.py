import pickle

number = 3
try:
  number = pickle.load( open( "save.p", "rb" ) )

except EOFError:
  raise StopIteration
print number
