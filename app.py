# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Create connection variable
#conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
#client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
#db = client.mars_db

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route("/")
def home():

    mars_data = mongo.db.mars.find_one()
    print(mars_data)
    return render_template("index.html", mars_data = mars_data)


@app.route("/scrape")
def scrape():


    # Run the scrape function
    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars.update({}, mars_data, upsert= True)
    print(mars_data)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
