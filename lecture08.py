#Iterative exponent
def exp1(a, b):
    ans = 1
    while (b > 0):
        ans *= a
        b -= 1
    return ans
#2 + 3b; when b =10, it is 32;when b=100, it is 302;when b=1000, it is 3002
#care about the rate of growth as size of problem grows, that is how much bigger does this get as I make the problem bigger
#Asymptotic notation - the limit as the size of the problem gets bigger
#big O is an upper limit to the growth of a function as the input get bigger
#f(x)∈O(n^2) - the f(x) is bounded above, there is upper limit on it, that this grows no faster than quadratic in n, n squared.
#x is input; n measure the size of x

#recursive exponent
def exp2(a, b):
    if b == 1:
        return a
    else:
        return a * exp2(a, b-1)
#one test, one substract, one multiplication, that is 3 steps and plus t(b-1)
#t(b) = 3 + t(b-1)
#      = 3 + 3 + t(b-2)
#      = 3k + t(b-k)
#b-k == 1; 3(b-1) + t(1) = 3b - 1 ∈O(b) linear;

#a ** b = (a * a) ** (b/2) #b is even
#a ** b = a * (a ** (b-1))  #b is odd
#  =a * ((a * a) ** ((b-1)/2))  #then b is even again
def exp3(a, b):
    if b == 1:
        return a
    if (b / 2) * 2 == b:
        return exp3(a * a, b/2)
    else:
        return a * exp3(a, b-1)
#b is even, a test(b == 1), a division, a multiplication, a test(==), and then a divide(b/2) and a square.
#6 steps; then when b is even, t(b) = 6 + t(b/2)
#b is odd, a test(b == 1), a division, a multiplication, a test(==), and a subtract, and a multiplication;
#so that is 6+t(b-1), and then b is even, so the total is 12 + t((b-1)/2)
#no matter b is even or odd, it can represent in this way: t(b) = 12 + t(b/2)
#t(b) = 12 + t(b/2) = 12 + 12 + t(b/4) = 12k + t(b/2^k) #这时b不是减1，而是一半一半地减去的；
#b/2^k #k = logb
#O(logb) #b is the changing input, not k
#reduce the complex in half

def g(n, m):
    for i in n:
        for j in m:
            x += 1
    return x
#O(m * n)

def Towers(size, fromStack, toStack, spareStack):
    if size == 1:
        print 'Move disk from ', fromStack, 'to', toStack
    else:
        Towers(size-1, fromStack, spareStack, toStack)
        Towers(1, fromStack, toStack, spareStack)
        Towers(size-1, spareStack, toStack, spareStack)
# T(n) = 1 + T(1) + 2T(n-1) = 3 + 2T(n-1) = 3 + 2 * 3 +4T(n-2) = 3 + 2 * 3 + 4 * 3 + 8T(n-3)
#     = 3*(1+2+4+ ... +2^(k-1)) + 2^n *(n-1)
#O(2^n) exponential
#this recursive call had two sub-problems

#linear algorithms tend to be things where at one pass-through, you reduce the problem by a constant amount, by 1;
#log algorithms where you cut the size of the problem down by some multiplicative factor.
#Quadratic algorithm tend to have this doubly-nested, triply-nested things are likely to be quadratic or cubic algorithms.
#exponent algorithm when reduce the problem of one size into two or more sub-problem of a smaller size.





