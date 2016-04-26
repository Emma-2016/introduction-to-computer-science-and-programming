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
