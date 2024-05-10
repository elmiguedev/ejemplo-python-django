def serialize(dog):
  return {
    "id": dog.id,
    "name": dog.name,
    "age": dog.age
  }

def serialize_list(dogs):
  return [serialize(dog) for dog in dogs]