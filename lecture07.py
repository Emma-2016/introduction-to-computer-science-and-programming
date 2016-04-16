#list is mutatble
#>>> L1 = [1, 2, 3]
#>>> L2 = L1  #both L1 and L2 refer to the list object; it means that there are two paths to the list object
#>>> L1[1] = 'P'  #this change did not change the path that L1 will refer to the list object
#>>> L1
#[1, 'P', 3]
#>>> L2
#[1, 'P', 3]
#>>> L1 = 'ui'
#>>> L2
#[1, 'P', 3]
#>>> L1
#'ui'

#pseudocode: a description of the steps, not really the code
import math
#inputOK = False
#while not inputOK:
    #base = input('Enter bases: ')
    #if type(base) == type(1.0): inputOK = True
    #else: print 'Error. Base must be a floating point number'

#inputOK = False
#while not inputOK:
    #height = input('Enter height: ')
    #if type(height) == type(1.0): inputOK = True
    #else: print 'Error. Base must be a floating point number'

#hyp = math.sqrt(base * base + height * height)
#print 'Base: ' + str(base) + ',height: ' + str(height) + ', hpy: ' + str(hyp)

#create a function whenever you can
def checkFloat(name):
    inputOK = False
    while not inputOK:
        words = 'Enter ' + name + ': '
        output = input(words)
        if type(output) == type(1.0): inputOK = True
        else: print 'Error. ' + name.capitalize() + ' must be a floating point nubmer'
    return output

base = checkFloat('base')
height = checkFloat('height')
hyp = math.sqrt(base * base + height * height)
print 'Base: ' + str(base) + ',height: ' + str(height) + ', hpy: ' + str(hyp)


#Efficiency: choice of algorithm, map a problem into class of algorithms
#space and time
#space: how much computer memory it take to complete the computation of a particular problem
#not how much memory to store the input, it is how much the internal memory do I use up as I go through the computation(what kind of thing do I need to keep track with)
#this class focus on time
#time:
#what is the number of basic step needed as a function of the input size?
#random access model - assume the length of time it takes me to get to any location of the memory is constant
#the basic primitive step take constant time to compute
#best case - the minim
#worse case - the max
#the expected case - the avg
