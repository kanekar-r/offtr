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
       projectid = request.form.get("projectid")
       projecten = request.form.get("projecten")
              
       # getting input with name = lname in HTML form
       # last_name = request.form.get("lname")
       
       print(projectid)

       prj['ID'] = projectid
       prj['comp'] = comp
       prj['projecten'] = projecten       
       print(prj)

    return render_template("student.html")


@app.route('/vendor', methods = ["GET", "POST"])
def vendor():

   # return render_template("vendor.html")
   print(request.form.get)

   vname = request.form.get("vname")
   vdate = request.form.get("vdate")
   bdate = request.form.get("bdate")
   cdate = date.today()
   vend = {
         "vname" : vname,
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
   pdate = request.form.get("pdate")
   comp = {
      "compn" : compn,
      "vend1" : vend,
      "pdate" : pdate
   }

   print(comp)

   # return render_template("vendor.html")


   return render_template("comp.html")


if __name__=='__main__':
   app.run(debug = "TRUE")