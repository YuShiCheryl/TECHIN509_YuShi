class Dog:
  def __init__(self,name):
    self.name = name

class Cat:
  def __init__(self,name):
    self.name = name

dog = Dog('Fido')
cat = Cat('Fluffy')

print(dog.name,'and',cat.name)

print(isinstance(dog,Dog))

def speak(animal):
  if isinstance(animal, Dog):
    print('Woof!')
  elif isinstance(animal,Cat):
    print('meow')
  else:
    assert False, 'Unexpected type of animal'

speak(dog)
speak(cat)