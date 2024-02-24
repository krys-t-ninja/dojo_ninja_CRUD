from flask_app.config.mysqlconnection import connectToMySQL

db= "dojo_ninja_schema4"


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls,data):
        query ="INSERT INTO ninjas (first_name,last_name,age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s,%(dojo_id)s);"
        ninja_id = connectToMySQL(db).query_db(query,data)
        return ninja_id       
    
    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(db).query_db(query)
        ninjas = []
        for ninja in results:
           ninjas.append(cls(ninja)) 
        return  ninjas
    # this took me a while , i kept getting an empty table.
    # I knew the save to add a new ninja links and method worked 
    # because it showed in the terminal and mysql database. 
    # The list  did not have anything to append to until i then added the 
    # name of list to equal the results
    # so  when i called the function in the route ,
    # it finally showed the table on the web page
    
    @classmethod
    def get_one(cls, ninja_id):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        data = { 'id': ninja_id}
        results = connectToMySQL(db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s WHERE id=%(id)s;"
        return connectToMySQL(db).query_db(query,data)
        
    
    @classmethod
    def delete(cls, ninja_id):
        query = "DELETE FROM ninjas WHERE id=%(id)s;"
        data = { 'id': ninja_id}
        return connectToMySQL(db).query_db(query,data)
