# importing Flask and other modules
from flask import Flask, request, render_template
from datetime import date
prj = {}
vend = {}
comp = {}

# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       projectid = request.form.get("ProjectID")
              
       # getting input with name = lname in HTML form
       # last_name = request.form.get("lname")
       
       print(projectid)

       prj['ID'] = projectid
       prj['comp'] = comp
       
       print(prj)

    return render_template("student.html")


@app.route('/vendor', methods = ["GET", "POST"])
def vendor():

   # return render_template("vendor.html")
   print(request.form.get)

   vdate = request.form.get("vdate")
   bdate = request.form.get("bdate")
   cdate = date.today()
   vend = {
         "vdate" : vdate,
         "bdate" : bdate,
         "cdate" : cdate
      }

   print(vend)

   return render_template("vendor.html")



@app.route('/comp', methods = ["GET", "POST"])
def comp():

   print(request.form.get)

   compn = request.form.get("compn")
   comp = {
      "compn" : compn,
      "vend1" : vend
   }

   print(comp)

   # return render_template("vendor.html")


   return render_template("comp.html")


if __name__=='__main__':
   app.run(debug = "TRUE")