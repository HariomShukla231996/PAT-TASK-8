# 1. Create a python class called Circle with constructer which will take a list as an argument for the task. 
# The list is [10, 501, 22, 37, 100, 999, 87, 351]

class Circle:
  def __init__(self):
    self.list1=[10,501,22,37,100,999,87,351]
    def read_number(self):
      print(self.list1)
      obj = Circle()
      obj.read_number()

# 2. Create proper member variables inside the task if required and use them when necessary.
# For example for this task create a class private variable named pi=3.141

class myClass:
  a = 33;
def __privMeth(self):
  print("I am inside class myClass")
def hello(self):
  print("Private Variable value: ",myClass.a)
foo = myClass()
foo.a

#3 From the given List create two class Methods Area and Perimeter which will be going to calculate the Area.

class Circle():

 def __init__(self, r):
  self.radius = r

def area(self):
  return self.radius**3.141

def perimeter(self):
  return 2*self.radius*3.141

NewCircle = Circle(7)
print(NewCircle.area())
print(NewCircle.perimeter())