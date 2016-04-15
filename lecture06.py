def squareRootBi(x, epsilon):
    assert x >= 0, 'x must be non-negative, not ' + str(x)
    assert epsilon > 0, 'epsilon must be postive, not ' + str(epsilon)
    low = 0
    high = max(x, 1)  #this sovle previous problem
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

f(guess) = guess^2 - x
f(guess) = 0
guess ** 2 - 16: what we looking for here is when the curve is cross with x axis
the basic idea is that you take a guess, and you find the tangent(切线） of the guess
let's take the guess 3, and tangent of the curve at 3.  The next guess will be where the tangent crosses the x axis.
the utility of this rely upon the observation that most of time, the tangent line is a good approximation to the curve for values near the solution. 
Therefore the x intersect of the tangent will be closer to right answer than the current guess
How could we find the intersect of tangent?
This is where the derivative comes in. 
The slope of the tangent is given by the first derivative of the function f at the point of the guess.
The derivative of i'th guess is equal to two times the i'th guess (f'(guess) = 2 * guess)
Guess i+1 to be equal to guess i minus the new guess of the old guess divided by twice the old guess
