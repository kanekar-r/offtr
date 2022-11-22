# importing Flask and other modules
from flask import Flask, request, render_template
 
prj = {}

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
       
       print(prj)

       return "Your Project is "+ projectid
    return render_template("student.html")

if __name__=='__main__':
   app.run()