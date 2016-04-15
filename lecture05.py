# python perform arbitrary precision, once you are 'L', you stick to 'L'('L' means long, long int)
#>>> a = 2 ** 1000
#>>> b = 2 ** 999
#>>> a / b
#2L
#>>> a
#10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376L
#>>> b
#5357543035931336604742125245300009052807024058527668037218751941851755255624680612465991894078479290637973364587765734125935726428461570217992288787349287401967283887412115492710537302531185570938977091076523237491790970633699383779582771973038531457285598238843271083830214915826312193418602834034688L
#>>> a / b
#2L

#in python, float type mean the real number; IEEE 754 floating point
#scientific notation mantissa exponent , significant; 1 <= mantissa < 2
#most computer nowday is 64bits, 1 bit for sign(+, -), 11 bit for exp, 52 mantissa, that is equal to 17 decimal digits
# So if we want a number that is 17 precision, we would not be able to get it from python (and most language)
#1/8 = 0.125
#base 10: 1.25 * 10^(-1)
#base 2: 1.0 * 2^(-3)
#1/10
#base 10: 1 * 10 ^(-1)
#base 2: ?

#repr() - built in function, short for representation
#convert the internal representation (in this case, a number) to string and display it on the screen
#for float, it rounds it to 17 digits, hence, when it rounds it to 17 digits, you get what you see here.
#>>> s = 0
#>>> for i in range(10): s += 0.1
#... 
#>>> s
#0.9999999999999999
#>>> print s #it have done automatic round
#1.0

#Most of the time we do not have to worry about float, but we do have to worry about '==' on float, since ambiguity and inaccuracy will accumulate
#>>> import math
#>>> a = math.sqrt(2)
#>>> a
#1.4142135623730951
#>>> a * a == 2
#False
#>>> a * a
#2.0000000000000004
#so you can not do equality but whether is it close enough, like: abs(a * a -2.0) < epsilon
reasons:
#1.might not be the exact answer   #use similar to epsilon
#2.can't enumerate all guesses -uncountable
#Guess, check, improve #the current guess is better than the previous guess -- successive approximation

#start with intial guess
#for inter in range(100) # here chose 100
# if f(guess) close enough then return the guess
# else: guess = better guess
#Error

#This is so called Bisection method
#take a guess is too big or too small


#Below is an example, that use bisection method: an initial guess, whether good enough(close enough to the result)
#since the we might not get the exact answer, we use epsilon to represent if it is a good enough answer.
#if it is not (bigger than epsilon), a way to produce a better guess, and iterate
def squareRootBi(x, epsilon):
    assert x >= 0, 'x must be non-negative, not ' + str(x)
    assert epsilon > 0, 'epsilon must be postive, not ' + str(epsilon)
    low = 0
    high = x
    guess = (low + high) / 2.0  #this is the initial guess
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 1000:  #whether it is close enough? #if is not, a better guess
        if guess ** 2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0  #another better guess
        ctr += 1
    assert ctr <= 1000, 'Iteration count exceeded'
    print 'Bi method. Num. iterations:', ctr, 'Estimater', guess
    return guess

squareRootBi(9, 0.0001)
# however, this method can not deal with numbers that less than 1
