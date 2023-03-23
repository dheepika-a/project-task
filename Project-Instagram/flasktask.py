from flask import Flask,render_template,request,redirect,redirect,url_for,flash
import sqlite3 as sql

app=Flask(__name__)

@app.route("/log",methods=["POST","GET"])
def add():

    username=request.form.get("name")
    password=request.form.get("password")
    print(username)
    print(password)
    conn = sql.connect("signup.db")
    cur =conn.cursor()
    cur.execute("SELECT username,password FROM sign")
    data=cur.fetchall()
    print(data)
    for i in data:
        if i[0]==username and i[1]==password:
           return render_template("home.html")
    else:
            
        return render_template("indexfile.html")

@app.route("/hello",methods=["POST","GET"])
def dep():
    return render_template("home.html")


@app.route("/",methods=["POST","GET"])
def signup():
    if request.method == "POST":
        email=request.form["name"]
        fullname=request.form["fullname"]
        username=request.form["username"]
        password=request.form["password"]
        conn = sql.connect("signup.db")
        cur =conn.cursor()
        cur.execute("insert into sign(EMAIL,FULLNAME,USERNAME,PASSWORD) values (?,?,?,?)",( email,fullname,username,password))
        conn.commit()
      

    return render_template("index.html")

@app.route("/showsign", methods=["POST","GET"])
def signup_data():
        
                conn=sql.connect("signup.db")
                conn.row_factory=sql.Row
                cur=conn.cursor()
                cur.execute("select * from sign")
                data=cur.fetchall()
                conn.commit()
                return render_template("show.html",data2=data)

@app.route("/page")
def pag():
      return render_template("profile.html")


if __name__=="__main__":
    app.run(debug=True)