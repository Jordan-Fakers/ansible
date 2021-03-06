#! usr/bin/env python

from bdd import *
from flask import *

self.cur.execute("INSERT INTO mytable (ID) VALUES (1) ")

app = Flask(__name__)

@app.route('/')
def welcome(): 
    return redirect(url_for('home'))  

@app.route('/home')
def home(): 
    return render_template("index.html")


@app.route('/inc')
def increment(): 
    self.cur.execute("UPDATE mytable SET id = id + 1")
    self.mybdd.commit()
    wait_time = 2000
    return f"<html><body><p>ID succesfully increase </br> You will be redirected in 2 seconds</p><script>var timer = setTimeout(function() {{window.location='/home'}}, { wait_time });</script></body></html>"


@app.route('/id')
def showId(): 
    self.cur.execute("SELECT id FROM mytable")
    result = self.cur.fetchall()
    return str(result[0][0]) 

if __name__ == "__main__": 
    app.run(host= "0.0.0.0", port=3000, debug = True)