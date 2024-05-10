from mysql import connector

class BaseRepository:

  def get_db_connection(self):
    db = connector.connect(
      host = "localhost",
      user = "root",
      password = "root",
      database = "prueba"
    )
    return db

  def execute_query(self, query):
    db = self.get_db_connection()
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    db.close()
    return rows

  def execute_query_with_params(self, query, params):
    db = self.get_db_connection()
    cursor = db.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    db.close()
    return rows

  def execute_non_query(self, query):
    db = self.get_db_connection()
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    id = cursor.lastrowid
    db.close()
    return id

  def execute_non_query_with_params(self, query, params):
    db = self.get_db_connection()
    cursor = db.cursor()
    cursor.execute(query, params)
    db.commit()
    id = cursor.lastrowid
    db.close()
    return id