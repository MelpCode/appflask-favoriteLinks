from flask import Flask,redirect,render_template,Response,request,flash,url_for
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
import json
import config
import datetime

# Initialization app:
app = Flask(__name__)

# DDBB Settings:
app.config['MONGO_URI']=config.MONGODB_URI
mongo = PyMongo(app)

# SETTINGS:
app.secret_key = 'mysecretkey'

#Routes:
#Route to show all the data:
@app.route('/linkspages',methods=['GET'])
def get_links():
    links = mongo.db.links.find()
    response = json_util.dumps(links) # return a string
    respLinks = json.loads(response)  # Convert string to JSON
    return render_template("index.html",urls=respLinks)

#Route to create a favorite page
@app.route('/linkspages',methods=['POST'])
def create_links():
    if request.method == "POST":
        link = request.form['link']
        fecha = datetime.datetime.now()
        links = mongo.db.links.insert(
            {'link':link,'date':fecha}
        )
        flash('Link saved successfully')
        return redirect(url_for('get_links'))

@app.route('/delete/<id>',methods=['GET'])
def delete_link(id):
    mongo.db.links.delete_one({'_id':ObjectId(id)})
    flash('Link deleted successfully')
    return redirect(url_for('get_links'))
# Initialize Server:
if __name__=="__main__":
    app.run(port=3000,debug=True)