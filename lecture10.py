#divide and conquer
#split the problem into simple version
#slove indepently
#combine the solution
#mergesort
#-divide list in half
#-continue until we ave singlet lists
#-merge of the sublist

def merSort(s):
    if len(s) < 2: return s[:]
    else:
        middle = len(s)/2
        #print 'middle is', middle
        right = merSort(s[:middle])
        left = merSort(s[middle:])
        together = merge(right, left)
        print 'merged', together
    return together

def merge(right, left):
    result = []
    i, j = 0, 0
    while i < len(right) and j < len(left):
        if right[i] <= left[j]:
            result.append(right[i])
            i += 1
        else:
            result.append(left[j])
            j += 1
    if i < len(right):
        result.extend(right[i:])
    if j < len(left):
        result.extend(left[j:])
    return result
s = [1, 8, 6, 4, 2, 3, 9, 5]
print merSort(s)

#when the problem can be handled in divide and conquer,
#the first question to ask is: how much dividision should I do, may be it is two, like the example, 
#but there may be other cases where you want to divide it into three
#the second question to ask is: what is the basic case? When can I get down to a problem that is small enough that it's basically trivial to solve
#the third question is: how can I combine?
#easy to divide and not complicated in combination

#hashing
#hash has some kind of technique to map any kind of data into integer
def hashChar(e):
    return ord(e)   #only single character; hash map any charater into a rage zero to 255, that is why the length of cSet is 256.

def cSetCreate():
    cSet = []
    for i in range(0, 255): cSet.append(None)
    return cSet

def cSetInsert(cSet, e):
    cSet[hashChar(e)] = 1   

def cSetMember(cSet, e):
    return cSet[hashChar(e)] == 1

cSet = cSetCreate()
cSetInsert(cSet, 'c')
print cSetMember(cSet, 'c')

#python built-in function ord() map any character into interget.
#if you want other type of data map to character, you need other function that function as ord()
#If you want to represent set of strings, well you basically just generalize the hash function.
#It is simply the same idea that you have a mapping from your input into a set of integers.
#This is a trade off between time and space. constant time access when doing search is great.
#how to grantee(?) a hash function takes any input into exactly one spot in the store space. The answer is we can not do that.
#It is hard to design a hash function that has completely even distribution meaning that it takes any input into exactly one output spot.
#try to use a function that spread things out pretty evenly. But the place you store into in those lists may have to themselves have a small list in it.
#hash function is hard to create

#Assert indicates here are some conditions to test. If they're true, I'm going to let the rest of the code run. If not, I'm going to throw an error. 
#So the assertion is basically saying we got some pre-conditions, those are the clauses inside the assert that have to be true, and there's a post condition.
#What the assert is saying, or rather the programmer is saying, if you give me input that satisfies the preconditions, I'm guaranteering to you that my code is going to give you something that meets th epost condition.
#Asserts in fact are nice in the sense that they let you check conditions at debugging time or testing time.
#So you can use them to see where your code is going.
#An exception, when you use an exception, you are basically saying, you can do anything you want with my code, and you can be sure that I am going to tell you if something is going wrong.
#And I am going to handle it myself as much as possible. Exceptions are going to handle unexpected things.
