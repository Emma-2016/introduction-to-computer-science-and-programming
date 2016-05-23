class Person(object):
	def __init__(self, family_name, first_name):
		self.family_name = family_name
		self. first_name = first_name
	def familyName(self):
		return self.family_name
	def firstName(self):
		return self.first_name
	def __cmp__(self, other):
		return cmp((self.family_name, self.first_name),  (other.faimly_name, other.first_name))
	def __str__(self):
		return '<Person: %s %s' % (self.family_name, self.first_name)
	def say(self, toWhom, something):
		return self.first_name + ' ' + self.family_name + ' ' + toWhom.familyName() + ' ' + toWhom.firstName() + ': ' + something
	def sing(self, toWhom, something):
		return self.say(toWhom, something + ' tra la la')

# when you know you are inside the instance, it is prefectable to just look up the value (just access to the value).
# however, if you are doing it with any other objects, send it a message. 
# see method say.
# when you call a method inside another method, the first argument is not necessary. Just call it normally. see method sing calls method say.

class MITperson(Person):
	nextIdNum = 0
	def __init__(self, family_name, first_name):
		Person.__init__(self, family_name, first_name)
		self.idNum = MITperson.nextIdNum
		MITperson.nextIdNum += 1
	def getIdNum(self):
		return self.idNum
	def __str__(self):
		return '<MIT Person: %s %s>' % (self.first_name, self.family_name)
	def __cmp__(self, other):
		return cmp(self.idNum, other.idNum)

# In the parent class, there are methods named __str__ and __cmp__. But in class MITperson, these two methods perform different things.
# Although class MITperson donot have method family_name or first_name, it is all ok. One can call it directly. Because MITperson has inherited it from class Person.
# nextIdNum is a local variable. Not inside the __init__ method.

class UG(MITperson):
	def __init__(self, family_name, first_name):
		MITperson.__init__(self, family_name, first_name)
		self.year = None
	def setYear(self, year):
		return self.year
	def say(self, toWhom, something):
		return MITperson.say(self, toWhom, 'Excuse me, but ' + something)
# Method say in this class is called shadowing. It calls the function but it changes the method also. (also called overriding)
# Method say in this class. When calling MITperson.say(), 'MITperson' is not an instance, the 'self' parameter is needed.
# Method say in Person class, 'toWhom' is an instance, the 'self' parameter is not needed.

class PROF(MITperson):
	def __init__(self, familyName, firstName, rank):
		MITperson.__init__(self, familyName, firstName)
		self.rank = rank
		self.teaching = {}
	def addTeaching(self, term, subj):
		try:
			self.teaching[term].append(subj)
		except KeyError:
			self.teaching[term] = subj
	def getTeaching(self, term):
		try:
			return self.teaching[term]
		except KeyError:
			return None
	def lecture(self, toWhom, something):
		return self.say(toWhom, something + ' as it is obvious')
	def say(self, toWhom, something):
		if type(toWhom) == UG:
			return MITperson.say(self, toWhom, 'I donot understand why you say ' + something)
		elif type(toWhom) == Prof:
			return MITperson.say(self, toWhom, 'I really liked your paper on ' + something)
		else:
			return self.lecture(something)

class Faculty(object):
	def __init__(self):
		self.name = []
		self.IDs = []
		self.place = None
	def add(self, who):
		if type(who) != Prof: raise TypeError('Not a professor')
		if who.getIdNum() in self.IDs: raise ValueError('Duplicate ID')
		self.names.append(who.getIdNum())
		self.members.append(who)
	def __iter__(self):
		self.place = 0
		return self
	def next(self):
		if self.place >= len(self.names):
			raise StopIteration
		self.place += 1
		return self.members[self.place - 1]
# Everytime call a "for in" structure, it call a 'iterator', which calls the method __iter__() and next().
# Faculty is list. __iter__() places the pointer at the beginning of the list and return self, that is a pointer to the instance.
# Iter and next work together. Iter creates this method, that's going to give you a pointer to the place in the structure, and then next literally walks along the structure giving you the next element and returning elements in turn.

# the idea of encapsulation
# the idea of inheritance
# by inheritance, one can shadow or override methods, so that he or she can specialise.
# Object-oriented system are great when you're trying to model systems that consist of a large number of units that interact in very specific ways.
# Modeling a system of people is a great idea. Modeling a system of molecules is probably a great idea. Modeling a system where it is natural to associate things together and where the number of interactions between them is very controlled.
