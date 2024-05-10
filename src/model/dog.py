class Dog: 

  def __init__(self, id, name, age):
    self.id = id
    self.name = name
    self.age = age

  def serialize(self):
    return self.__dict__