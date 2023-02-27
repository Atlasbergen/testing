class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def hello(self):
    print(f"Hello {self.name} you are {self.age} years old"
          
p1 = Person("Jonas", 45)
print(p1.Hello())
