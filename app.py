# import necessary libraries
from flask import Flask, render_template
import pymongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db

mars_data = scrape_mars.scrape_info()

# Creates a collection in the database and inserts two documents
db.mars.insert(html_data)

@app.route("/")
def echo():

    return render_template("index.html", name=name, hobby=hobby)


# Bonus add a new route
@app.route("/bonus")
def bonus():

    return render_template("bonus.html", name=name, hobby=hobby)


if __name__ == "__main__":
    app.run(debug=True)
