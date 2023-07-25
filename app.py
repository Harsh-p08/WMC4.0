from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("LP_index.html")

@app.route('/SP_index.html')
def hello_signup():
    return render_template("SP_index.html")

if __name__=="__main__":
    app.run(debug=True)