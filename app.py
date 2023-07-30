from flask import Flask, render_template,request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://harshp8:Harsh6204@wmc4-0.efyrnjc.mongodb.net/")
app.db = client.WMC4

entries=[]

@app.route('/', methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        entry_username = request.form.get("username")
        entry_password= request.form.get("password")
        app.db.entries.insert_one({"username1" : entry_username , "password1" : entry_password })
    return render_template("LP_index.html")


@app.route('/SP_index.html', methods=["GET","POST"])
def hello_signup():
    return render_template("SP_index.html")

if __name__=="__main__":
    app.run(debug=True)