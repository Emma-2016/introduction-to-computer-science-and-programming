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

#speed of convergence
sqrt(x)
f(guess) = guess62 - x
f(guess) = 0

value near the right answer
slope of the guess of tengent?
dy/dx

f'(guess) = 2*guess 
guess' = guess - f(guess)/2guess
f(3) = 3^2 -16 = -7
guess(i+1) = 3 - (-7/6) = 4.1666 use 4.1666 as guess(i)

