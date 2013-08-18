

While True:                                     
        # Load the dictionary back from the pickle file.
        import pickle
        
        number = pickle.load( open( "save.p", "rb" ) )
        print number

