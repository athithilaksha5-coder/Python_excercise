from flask import *
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add")                  
def add():   
    return render_template("add.html")

@app.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            author = request.form["author"]
            publisher = request.form["publisher"]
            nob=request.form["nob"]
                        
            with sqlite3.connect("library.db") as con:
                cur = con.cursor()   
                cur.execute("INSERT into librarybooks (BOOK_NAME, BOOK_AUTHOR, BOOK_PUBLISHER,NO_OF_BOOKS) values (?,?,?,?)",(name,author,publisher,nob))
                con.commit()
                msg = "Your donation books successfully Added"   
        except:
            con.rollback()
            msg = "We can not add books to the library"
        finally:
            return render_template("success.html",msg = msg)
            con.close()   
            
@app.route("/view")
def view():
    con = sqlite3.connect("library.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from librarybooks")   
    rows = cur.fetchall()
    return render_template("view.html",rows = rows)

@app.route("/lend")                                     
def lend():                                   
    return render_template("lend.html")

@app.route("/deleterecord",methods = ["POST"])   
def deleterecord():
    name = request.form["name"]
    with sqlite3.connect("library.db") as con:
        try:
            cur = con.cursor()     
            cur.execute("update librarybooks set NO_OF_BOOKS = NO_OF_BOOKS-1 where BOOK_NAME=?",(name,))
            msg = "you'd requested book successfully borrow"   
        except:
            msg = "you'd requested book not available in library"
        finally:
            return render_template("delete_record.html",msg = msg)                    
                    
@app.route("/return")                   
def book():                 
    return render_template("return.html")

@app.route("/returnrecord",methods = ["POST"])   
def returnrecord():
    name = request.form["name"]
    with sqlite3.connect("library.db") as con:
        try:
            cur = con.cursor()
            cur.execute("update librarybooks set NO_OF_BOOKS = NO_OF_BOOKS+1 where BOOK_NAME=?",(name,))
            msg = "book return successfully"                 
        except:
                msg = "book  return not successfully"
        finally:
            return render_template("delete_record.html",msg = msg)            

if __name__ == "__main__":              
    app.run(debug = True)               
