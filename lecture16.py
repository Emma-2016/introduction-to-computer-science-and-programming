class Person(object):
  def __init__(self, family_name, first_name):
    self.family_name = family_name
    self.first_name = first_name
    
  def family_name(self):
    return self.family_name
  def first_name(self):
    return self.first_name
    
  def __cmp__(self, other):
    return cmp((self.family_name, self.first_name), (other.family_name(), other.first_name()))
  
  def __str__(self):
    return '<Person is %s %s>' % (self.first_name, self.family_name)
  
  def say(self, to_whom, message):
    return self.first_name + self.family_name + 'says to' + to_whom.first_name() + to_whom.family_name() + ':" + message
#when you know you are inside the instance, it is prefectable to just look up the value (just access to the value).
#however, if you are doing it with any other objects, send it a message. 
#see method say and cmp.


class MITperson(Person):
  nextIDnum = 0 #local number
  def __init__(self, family_name, first_name):
    Person.__init__(self, family_name, first_name)
    self.id_num = MITperson.nextIDnum
    MITperson.nextIDnum += 1
  
  def getIDnum(self):
    return self.id_num
  
  def __str__(self):
    return '<MITperson is %s %s>' % (self.first_name, self.family_name)
  
  def __cmp__(self, other):
    return cmp(self.id_num, others.getIDnum())
  

#In the parent class, there are methods named __str__ and __cmp__. But in class MITperson, these two methods perform different things.
#Although class MITperson donot have method family_name or first_name, it is all ok. One can call it directly. Because MITperson has inherited it from class Person.


class UG(MITperson):
  def __init__(self, family_name, first_name):
    MITperson.__init__(self, family_name, first_name)
    self.year = None
    
  def setYear(self, year):
    if self.year > 5: return OverflowError('Too many')
    self.year = year
  def getYear(self):
    return self.year
    
  def say(self, toWhom, message):
    return MITperson.say(sefl, toWhom, 'Excuse me, but' + message) 
    #this is called shadowing. It calls the function but it changes the method also. (also called overriding)
