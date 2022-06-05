
from flask import Flask, render_template,request,redirect
# import the class from user.py
from user import User
app = Flask(__name__)
#display the create user html which has the form of first name , last name and email //just render html file
@app.route('/')
def index():
    return render_template('create_user.html')
# this will display all useres inside database plus the users added by form 
@app.route('/show_user')
def show_all():
    # userList is the empty array that we created  usersList = []
    #and then  Iterate over the db results and append the data that came from database to it plus the data that will come from form
    usersList = User.show_all_users()
    return render_template("read_all_user.html",all_users=usersList)

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "eml" : request.form["eml"]
    }
    # We pass the data dictionary into the save method from the User class.
    User.save(data)
    # direct the result to the show user route which has read all user html template.
    return redirect('/show_user')

if __name__ == "__main__":
    app.run(debug=True)
