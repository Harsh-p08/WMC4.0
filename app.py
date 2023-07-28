from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        entry_username = request.form.get("username")
        entry_password= request.form.get("password")
        print(entry_username , entry_password )
    return render_template("LP_index.html")

@app.route('/SP_index.html', methods=["GET","POST"])
def hello_signup():
    return render_template("SP_index.html")

if __name__=="__main__":
    app.run(debug=True)