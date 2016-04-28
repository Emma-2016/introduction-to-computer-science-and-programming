#linked list - store here is how far you have to jump to get to the next element, and then use the next sequence of things to represent the first element
#linked list - linear access time --LISP
#python -- two things; the first box is a pointer to the memory where contain the actual value, which itself maybe a brunch of pointers
# the second part is the pointer to the next element
#bisearch pattern:
#pick the midpoint
#check to see if this is answer
#If not, reduce to samller problem
#repeat

#Should we sort before search?
#how far can we sort a list? n * log(n)
#unsorted list and search: n
#sorted and search n*log(n) + log(n)
#depend on how many times you want to search the list
#kn VS. n*log(n) + k*log(n), therefore if search onece, use unsort and search; otherwise use the second one
#Amortize the cost

#select sort  #O(n^2)
#loop invariant: list is split, prefix and suffix; the first part is sorted, the second part is not.
#the loop begins with the prefix being nothing and it keeps increasing the size of prefix by 1 until it gets through the entire list, at which point there's nothing in the suffix and the entire prefix is sorted.

#Devide conquer algorithm



#selection algorithm:
def selection(s):
    for i in range(len(s)):
        minIndex = i
        minValue = s[i]
        tmp = s[i]
        for j in range(i, len(s)):
            if minValue > s[j]:
                minIndex = j
                minValue = s[j]
                tmp = s[i]
        s[i] = s[minIndex]
        s[minIndex] = tmp
        print s #To see how it actually work
    return s
s = [1, 8, 6, 4, 2, 3, 9, 5]
print'Now print', selection(s)

#bubble
def bubble(s):
    for i in range(len(s)): #each loop send the biggest element to the last
        for j in range(len(s) - 1): #some element may get suck in the middle, cause the elelment is bigger than it; however the bigger element will continue to be sent to latter part. And the sucked element may be sent at the next loop i
            if s[j] > s[j+1]:
                tmp = s[j]
                s[j] = s[j+1]
                s[j+1] = tmp
        #print s
    return s
s = [1, 8, 6, 4, 2, 3, 9, 5]
print 'The original list is ', s
print'Now print', bubble(s)

#the complexity of both algorithm is n^2, while n is the length of the list.
#However, the bubble algorithm swap every time
#the selection algorithm swap only once each loop

#Another version of bubble:
def bubble(s):
    swap = True
    while swap:
        swap = False
        for j in range(len(s) - 1): 
            if s[j] > s[j+1]:
                tmp = s[j]
                s[j] = s[j+1]
                s[j+1] = tmp
                swap = True
        print s
    return s
s = [1, 8, 6, 4, 2, 3, 9, 5]
print 'The original list is ', s
print'Now print', bubble(s)

#Even with this version, the complexity is n^2, because we are looking for the worst case.
