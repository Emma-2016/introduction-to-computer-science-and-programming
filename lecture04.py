# Decomposition and abstraction through functions; introduction to recursion

#decomposition
#abstract

#functions
#block up into modules
#suppress details
#create new primitives

#-def keyword
#-FunctionName (x)   #x represent foraml parameters
#-return keyword
#-none special value
#-invoke a fuctiong by passing a value to parameters
#-local parameter do not affect gobal parameter (not in the case of mutatble variable)

#solve a problem by enumerate and check ------ brute force algorithm

def solve1(numLegs, numHeads):
    for numC in range (0, numHeads+1):
        numP = numHeads - numC
        Legs = 4 * numP + 2 * numC
        if Legs == numLegs:
            return (numP, numC)
    return (None, None)

def harnTard1():
    heads = int(raw_input('Please enter number of Heads:'))
    legs = int(raw_input('Please enter number of legs:'))
    pigs, chickens = solve1(legs, heads)
    if pigs == None:
        print 'There is no solution!'
    else:
        print 'Number of pigs:', pigs
        print 'Number of chickens:', chickens
        
def solve2(numLegs, numHeads):
    for numC in range(0, numHeads+1):
        for numP in range(numC, numHeads-numC+1):
            numS = numHeads - numC - numP
            Legs = 8 * numS + 4 * numP + 2 * numC
            if Legs == numLegs:
                return (numP, numC, numS)
    return (None, None, None)

def harTard2():
    heads = int(raw_input('Please enter number of Heads:'))
    legs = int(raw_input('Please enter number of legs:'))
    pigs, chickens, spiders = solve2(legs, heads)
    if pigs == None:
        print 'There is no solution!'
    else:
        print 'Number of pigs:', pigs
        print 'Number of chickens:', chickens
        print 'Number of spiders:', spiders

def solve3(numLegs, numHeads):
    isSolved = False
    for numC in range(0, numHeads+1):
        for numP in range(numC, numHeads-numC+1):
            numS = numHeads - numC - numP
            Legs = 8 * numS + 4 * numP + 2 * numC
            if Legs == numLegs:
                print 'Number of pigs:', numP
                print 'Number of chickens:', numC
                print 'Number of spiders:', numS
                isSolved = True
    if not isSolved: return 'There is no solution!'

def harTard3():
    heads = int(raw_input('Please enter number of Heads:'))
    legs = int(raw_input('Please enter number of legs:'))
    pigs, chickens, spiders = solve3(legs, heads)


#recursion:
#base case - simplest possible solution
#inductive step - break problem into a simple vesion of same problem pluse some other steps
def isPalindrome(s):
    if len(s) <= 1: return True
    else: return s[0] == s[-1] and isPalindrome(s[1:-1])

def isPalindrome1(s, indent):
    print indent, 'isPalindrome1 is called with', s
    if len(s) <= 1:
        print indent, 'About to return True from base case'
        return True
    else:
        ans = s[0] == s[-1] and isPalindrome1(s[1:-1], indent + indent)
        print indent, 'About to return True from', ans
        return ans

print isPalindrome1('abcddcba','    ' )
#     isPalindrome1 is called with abcddcba
#         isPalindrome1 is called with bcddcb
#                 isPalindrome1 is called with cddc
#                                 isPalindrome1 is called with dd
#                                                                 isPalindrome1 is called with 
#                                                                 About to return True from base case
#                                 About to return True from True
#                 About to return True from True
#         About to return True from True
#     About to return True from True
#True
