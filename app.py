from flask import Flask,render_template,url_for,redirect,request,jsonify,Response
from config import config



app=Flask(__name__)


@app.route("/login", methods=["GET", 'POST'])
def login():

    return render_template("index.html")










if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run( )
