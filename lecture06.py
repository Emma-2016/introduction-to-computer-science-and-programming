def squareRootBi(x, epsilon):
    assert x >= 0, 'x must be non-negative, not ' + str(x)
    assert epsilon > 0, 'epsilon must be postive, not ' + str(epsilon)
    low = 0
    high = max(x, 1.0)  #this sovle previous problem
    guess = (low + high) / 2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 1000:
        if guess ** 2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        ctr += 1
    assert ctr <= 1000, 'Iteration count exceeded'
    print 'Bi method. Num. iterations:', ctr, 'Estimater', guess
    return guess

squareRootBi(0.25, 0.0001)

#speed of convergence

#f(guess) = guess^2 - x
#try to slve the f(guess) = 0
#that is:guess ** 2 - 16: what we looking for here is when the curve is cross with x axis

#the basic idea is that you take a guess, and you find the tangent(切线） of the guess
#let's take the guess 3, and tangent of the curve at 3.  The next guess will be where the tangent crosses the x axis.
#Instead of using Bisection method, use another method to find the next guess.

#the utility of this rely upon the observation that most of time, the tangent line is a good approximation to the curve for values near the solution. 
#Therefore the x intersect of the tangent will be closer to right answer than the current guess
#How could we find the intersect of tangent?
#This is where the derivative comes in. 
#The slope of the tangent is given by the first derivative of the function f at the point of the guess.
#The derivative of i'th guess is equal to two times the i'th guess (f'(guess) = 2 * guess)

def squareRootNR(x, espilon):
    assert x >= 0, 'x must be non-negative, not ' + str(x)
    assert espilon > 0, 'epsilon must be positive, not ' + str(espilon)
    x = float(x)
    guess = x / 2.0
    diff = guess ** 2 - x
    ctr = 1
    while abs(diff) > espilon and ctr <= 100:
        guess = guess - diff / (2.0 * guess)
        diff = guess ** 2 - x
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print 'NR method. Num. iterations:', ctr, 'Estiamtion'
    return guess
print squareRootNR(16, 0.001)

#method is a fancy word for function with a different syntax
#the first arguement is always the object itself
