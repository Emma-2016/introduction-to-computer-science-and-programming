int
arbitrary precision
L -> long long int
float - floating point - real
IEEE 754 floating point
scientific notation mantissa exponent
significant
1 <= mantissa < 2
64bits
1bit sign + -
11 exp
52 mantissa
17 decimal digits
if we want a number that is 17 precision, we would not be able to get it
1/8 = 0.125
base 10: 1.25 * 10^(-1)
base 2: 1.0 * 2^(-3)
1/10
base 10: 1 * 10 ^(-1)
base 2: ?

repr() - built in function, short for representation
convert the internal representation (in this case, a number) to string and display it on the screen
for float, it rounds it to 17 digits, hence, when it rounds it to 17 digits, you get what you see here.
>>> for i in range(10): s += 0.1
... 
>>> s
0.9999999999999999
>>> print s #it have done automatic round
1.0

worry about == on float
>>> import math
>>> a = math.sqrt(2)
>>> a
1.4142135623730951
>>> a * a == 2
False
>>> a * a
2.0000000000000004
so you can do equality but if is it close enough
abs(a * a -2.0) < epsilon

1.might not be the exact answer   #use similar to epsilon
2.can't enumerate all guesses -uncountable
Guess, check, improve #the current guess is better than the previous guess -- successive approximation

start with intial guess
for inter in range(100) # here chose 100
  if f(guess) close enough then return the guess
  else: guess = better guess
Error

Bisection method
take a guess is too big or too small


def squareRootBi(x, epsilon):
    assert x >= 0, 'x must be non-negative, not ' + str(x)
    assert epsilon > 0, 'epsilon must be postive, not ' + str(epsilon)
    low = 0
    high = x
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

squareRootBi(9, 0.0001)
