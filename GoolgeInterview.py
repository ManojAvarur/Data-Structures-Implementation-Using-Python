def Solve(lists, sum):
    mySet = set({})
    for i in lists:
        if( i in mySet ):
            return mySet
        
        mySet.add( sum - i )
    
    return False


sets = Solve([1,2,3,4,4], 8)

print(sets)