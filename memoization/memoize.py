###
# This is a nice function decorator for memoizing recursive functions. See
# example usage below
###
def memoize(F):
    # A hash table for storing previous states
    hashed_states = {}
    
    def memoized_F(*args):
        # if we haven't memoized this state, calculate
        # it. Then return it
        if args not in hashed_states:
            hashed_states[args] = F(*args)

        return hashed_states[args]
    
    return memoized_F

###
# Given an existing recursive function (like the one below), adding the
# @memoize will call the decorator to make it memoizable
###
@memoize
def fibonacci(N):
    if N is 0 or N is 1:
        return N
    else:
        return fibonacci(N-1) + fibonacci(N-2)

print(fibonacci(100))
