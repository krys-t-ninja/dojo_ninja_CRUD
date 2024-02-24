
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja import Ninja



db='dojo_ninja_schema4'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name) VALUE (%(name)s);'
        return connectToMySQL(db).query_db(query, data)
        
    
    @classmethod
    def get_all_dojos(cls):
        query= 'SELECT * FROM dojos;'
        results= connectToMySQL(db).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_one_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojo_ninja_schema4').query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            ninja = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
            }
            dojo.ninjas.append( Ninja(ninja))
        return dojo
    
    @classmethod
    def delete_dojo(cls,dojo_id):
        query = "DELETE FROM dojos WHERE id=%(id)s;"
        data = { 'id': dojo_id}

        return connectToMySQL(db).query_db(query,data)
