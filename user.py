# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the user table from our database.
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
#this class method responsible for retreiving all the users from the database
    @classmethod
    def show_all_users(cls):
        query="SELECT * FROM users;"
        results = connectToMySQL('users').query_db(query)
        usersList = []
# Iterate over the db results and create instances of users with cls.
        for user in results:
            usersList.append( cls(user))
        return usersList
#this class method will add new users to the data base
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email ) VALUES ( %(fname)s , %(lname)s , %(eml)s );"
# data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users').query_db( query, data )

