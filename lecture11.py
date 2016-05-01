#validation -- the process uncover problems & increase confidence (but never be sure we got it nailed)
#two processes -- testing and reasoning

#debug -- process of ascertaining why the program fails, how to find out why
#function & performance debug(why it is not fast)

#defesive programming
#testing and debugging are not the same things
#testing exames input / output pair
#Unit testing -- Functions and classes
#Integration testing -- overall program
#always start with unit testing
#testing always challenge
#test suit -- small enough to test and large enough to give us confidence

#good programmer -- learn debug
#debugging -- a process of engineering
#goal of debugging is not to eliminate one bug, but bug-free
#print statement & reading -- tools to debugging
#be systematic when debugging, redcued the search space, to localize the source of problem
#how to be systematic when debugging
#study program text and ask how could it produce this result, when you understand how it did what it had did, you are half way there.
#the next question is: it is part of family?
#final question is: how to fix it?
#scientifical method -- you first study the available data, test data (input, maybe it works on some data but not others)
#the second available data is program text
#second step of scientifical method is: form hypothesis consistent with all the data
#third step of scientifical method is: design and run repectable experiment
#the experiment must have the potential to refute the hypothesis, typically it has useful intermediate results, and you must know what the result it suppose to be
#design the experiment -- 1. find simplest input that will produce the problem
#2.binary search -- not a lucky guess

#exmaple show how to debug
#it is a classical mistake
#list is mutatble, so instead of using ListA = ListB, use ListA = ListB[:]
