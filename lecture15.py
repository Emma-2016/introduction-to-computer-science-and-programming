# Class - template to create instance of object.
# Instance has some internal attributes.

class cartesianPoint:
  pass
  
cp1 = cartesianPoint()
cp2 = cartesianPoint()
cp1.x = 1.0
cp2.x = 1.0
cp1.y = 2.0
cp2.y = 3.0

def samePoint(p1, p2):
  return (p1.x == p2.x) and (p1.y == p2.y)
  
def printPoint(p):
  print '(' + str(p.x) + ', ' + str(p.y) + ')'
  
  
# shallow equality -- 'is': given two things, do they point to exactly the same reference? (object)
# deep equality -- we can define. (value)


class cPoint():
  #def __init__(self, x, y): create an instance, use 'self' to refer to that instance
  #when call a class, it create an instance with all those internal attributes. __init__ create a pointer to that instance.
  #You need access to that, so it calls it, passing in self as the pointer to the instance.
  #That says, it has access to that piece of memory and now inside of that piece of memory, I can do thing like:
  #define self.x to be the value passed in for x. That is create a variable name x and a value associated with it.
  #self will always point to a particular instance
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.radius = math.sqrt(self.x * self.x + self.y * self.y)
    self. angle = math.atan2(self.y, self.x)
  def cartesian(self):
    return (self.x, self.y)
  def polar(self):
    return (self.radius, self.angle)
  def __str__(self): #print repretation
    return '(' + str(self.x) + ', ' + str(self.y) + ')'
  def __cmp__(self, other):
    return cmp(self.x, other.x) and cmp(self.y, other.y)
    
#data hidding - one can only access instance values through defined methods. Python does not do this.
# operator overloading


class Segment():
  def __init__(self, start, end):
    self.start = start
    self.end = end
  def length(self):
    return ((self.start.x - self.end.x) ** 2 + (self.start.y - self.end.y) ** 2) ** 0.5
    #in fact, one should access the value through a defined method.
