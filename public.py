from flask import*
from database import *
public=Blueprint('public',__name__)

@public.route('/')
def homepage():
    return render_template("homepage.html")
@public.route('/login',methods=['post','get'])
def loginpage():
    if 'btn' in request.form:
        username=request.form['uname']
        password=request.form['pwd']
        qry="select * from login where username='%s' and password='%s'"%(username,password)
        login=select(qry)

        if login[0]['usertype']=='admin':
            return redirect(url_for('admin.adminhome'))
       


        

    return render_template("login.html")