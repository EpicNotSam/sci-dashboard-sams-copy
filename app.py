from datetime import datetime

from flask import Flask
from flask import render_template, request, redirect 
from flask_mysqldb import MySQL
# we need render_template to use the jinja templates
# we need request to handle get and post requests

app = Flask(__name__)

app.config['MYSQL_HOST'] = "cs-mysql-01.cs.pitt.edu"
app.config['MYSQL_USER'] = "sci-inventory"
app.config['MYSQL_PASSWORD'] = "7WdtfEBnUKx2xKcX"
app.config['MYSQL_DB'] = "sci-inventory"

mysql = MySQL(app)


@app.route("/dbconnect/")
def dbconnect():
    print(mysql.connection)
    return "hello"


#if it is a get request they want the login page
#if it is a post request they are trying to send their credentials
@app.route("/", methods = ["GET", "POST"])
def login():
    ## if request.method == "GET":
        ## return render_template("loginPage.html") # for get request (for post we should redirect to the homepage)
    ## else: #post request so we need to log this user into their home
        ## name = request.form["username"]
        ## return redirect("/home/" + name)
        return redirect("/home/")

@app.route("/home/<name>")
@app.route("/home/")
def home(name = None):
    return render_template("HomePage.html", name = name)
    

@app.route("/Equipment/", methods = ["GET","POST"])
def equipment():
    if request.method == "GET":
        return render_template("Equipment.html")
    if request.method == "POST": #later implement the search conditions that were submitted
        building = request.form["building"] #later we will use these to show the actual search results
        room = request.form["room"]
        sort = request.form["sort"]
        #when doing the script for this results page, we should consider that equipment managers may select no building
        #as well as select no room, if they would like to see a full list of equipment
        return render_template("EquipmentResults.html", building = building, room = room, sort = sort )
    

@app.route("/RoomReservation/",  methods = ["GET","POST"])
def roomReservation():
    if request.method == "GET":
        return render_template("RoomReservation.html")
    if request.method == "POST":
        time = request.form["time"]
        date = request.form["date"]
        roomType = request.form["roomType"]
        building = request.form["building"]
        return render_template("RoomReservationResults.html", building = building, roomType = roomType, date = date, time = time)

@app.route("/ClassroomFinder/",  methods = ["GET","POST"])
def classroomFinder():
     if request.method == "GET":
        return render_template("ClassroomFinder.html")
     if request.method == "POST":
         building = request.form["building"]
         return render_template("ClassroomFinderResults.html", building = building, room = None)
        #I have to rework this because the java script needs the building in order to populate the room dropdown

@app.route("/MyRentals/")
def myRentals():
     return render_template("MyRentals.html")

#we can use this format for the routes for the individual item pages
#This page is useless to our project but I am going to leave it for now so you can see how the hello_there template
#interacts with this
@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None): #I think this sets name to none if they didnt put one
    return render_template(
        "hello_there.html",
        name = name, #setting up so that name var here is passed to the template where we had {{name}}
        date = datetime.now() #passing the current date as the date
    )