from ..model.dog import Dog
from mysql import connector
from .base_repository import BaseRepository

class DogRepository(BaseRepository):

  def get_all(self):
    dogs = []
    rows = self.execute_query("SELECT * FROM dog")
    for row in rows:
      dogs.append(Dog(row[0], row[1], row[2]))

    return dogs

  def get_by_id(self, id):
    query = "select * from dog where id = %s"
    rows = self.execute_query_with_params(query, [id])
    if len(rows) == 0:
      return None
    
    return Dog(rows[0][0], rows[0][1], rows[0][2])
  
  def add(self, dog):
    query = "insert into dog (name, age) values (%s, %s)"
    params = [dog.name, dog.age]
    id = self.execute_non_query_with_params(query, params)
    dog.id = id

    return dog