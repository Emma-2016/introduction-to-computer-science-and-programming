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
#hash has some kind of technique to map any kind of subject into integer
