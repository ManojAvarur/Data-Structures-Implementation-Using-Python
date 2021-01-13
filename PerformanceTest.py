import time

def performanceTest(arr):
    start = time.time()

    for i in arr:
        if( i == 'nemo' ):
            print('Found NEMO!')
        
    end = time.time()

    print( round( end - start ) )



performanceTest( ['nemo']*100000 )