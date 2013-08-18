# Save a dictionary into a pickle file.
import pickle

number = { 99 }

pickle.dump( number, open( "save.p", "wb" ) )