from flask import *
from database import *
admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')





@admin.route('/managestaff',methods=['GET','POST'])
def managestaff():
    data={}
    qry2="select * from staff inner join login using(login_id)``"
    data['user']=select(qry2)
    if 'submit' in request.form:
        fname=request.form['fn']
        lname=request.form['ln']
        phone=request.form['pn']
        place=request.form['place']
        email=request.form['em']
        username=request.form['uname']
        password=request.form['pwd']
        qry="insert into login values(null,'%s','%s','staff')"%(username,password)
        res=insert(qry)
        
        qry1="insert into staff values (null,'%s','%s','%s','%s','%s','%s')"%(res,fname,lname,phone,place,email)
        insert(qry1)
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        if action=='active':
            qry3="update login set usertype='staff' where login_id='%s'"%(id)
            update(qry3)
            return ''' <script>alert("Activated successfully");window.location="/managestaff"</script>'''
        if action=='deactive':
            qry3="update login set usertype='pending'  where login_id='%s'"%(id)
            update(qry3)
            return ''' <script>alert("Deactivated successfully");window.location="/managestaff"</script>'''
        if action=='update':
            qry4="select * from staff where staff_id='%s'"%(id)
            data['up']=select(qry4)
            if 'update' in request.form:
                fname=request.form['fn']
                lname=request.form['ln']
                phone=request.form['pn']
                place=request.form['place']
                email=request.form['em']
                q="update staff set fname='%s',lname='%s',phone='%s',place='%s',email='%s' where staff_id='%s'"%(fname,lname,phone,place,email,id)
                update(q)
                return ''' <script>alert("updated successfully");window.location="/managestaff"</script>'''
    return render_template('managestaff.html',data=data)




@admin.route('/manageclient',methods=['GET','POST'])
def manageclient():
    data={}
    qry2="select * from client inner join login using(login_id)"
    data['user']=select(qry2)
    if 'submit' in request.form:
        companyname=request.form['cn']
        place=request.form['pl']
        phone=request.form['pn']
        email=request.form['em']
        latitude=request.form['lat']
        longitude=request.form['lon']
        username=request.form['uname']
        password=request.form['pwd']
        qry="insert into login values(null,'%s','%s','pending')"%(username,password)
        res=insert(qry)
        qry1="insert into client values (null,'%s','%s','%s','%s','%s','%s','%s','pending')"%(res,companyname,place,phone,email,latitude,longitude)
        insert(qry1)
        return ''' <script>alert("ADD successfully");window.location="/manageclient"</script>'''


    if 'action' in request.args:
         action=request.args['action']
         id=request.args['id']
         if action=='active':
            qry3="update login set usertype='client'  where login_id='%s'"%(id)
            update(qry3)

            qry3="update client set  status='Active' where login_id='%s'"%(id)
            update(qry3)

            return '''<script>alert("Activated");window.location="/manageclient"</script>'''
         if action=='deactive':

            qry3="update login set usertype='pending'  where login_id='%s'"%(id)
            update(qry3)

            qry3="update client set status='pending' where login_id='%s'"%(id)
            update(qry3)
       
            return '''<script>alert("Deactivated");window.location="/manageclient"</script>'''
         if action=='update':
            qry4="select * from client where client_id='%s'"%(id)
            data['up']=select(qry4)
            if 'update' in request.form:
                companyname=request.form['cn']
                place=request.form['pl']
                phone=request.form['pn']
                email=request.form['em']
                latitude=request.form['lat']
                longitude=request.form['lon']
                q="update client set companyname='%s',place='%s',phone='%s',email='%s',latitude='%s' ,longitude='%s' where client_id='%s'"%(companyname,place,phone,email,latitude,longitude,id)
                update(q)
                return ''' <script>alert("updated successfully");window.location="/manageclient"</script>'''
    return render_template('manageclient.html',data=data)







@admin.route("/addwork",methods=['get','post'])
def addwork():
    data={}
    qry8="select * from client"
    qry9="select * from works inner join client using(client_id) "
    data['user']=select(qry9)
    data['client']=select(qry8)
    if 'send' in request.form:
        title=request.form['noti']
        description=request.form['des']
        client=request.form['client']
        qry="insert into works values(null,'%s','%s','%s','pending',CURDATE())"%(client,title,description)
        res=insert(qry)
        return ''' <script>alert("work added successfully");window.location="/addwork"</script>'''
   

    return render_template("addwork.html",data=data)




@admin.route("/viewtickets",methods=['get','post'])
def viewtickets():
    data={}
    qry9="select * from tickets"
    data['user']=select(qry9)
   

    return render_template("viewtickets.html",data=data)





@admin.route("/viewcomplaints",methods=['get','post'])
def viewcomplaints():
    data={}
    qry9="select * from complaints"
    data['user']=select(qry9)
   

    return render_template("viewcomplaints.html",data=data)




@admin.route("/sendnotifications",methods=['get','post'])
def viewnotifications():
    data={}
    qry6="select * from notification"
    data['user']=select(qry6)
    if 'send' in request.form:
        title=request.form['noti']
        description=request.form['des']
        qry="insert into notification values(null,'%s','%s',CURDATE())"%(title,description)
        res=insert(qry)
        return ''' <script>alert("Notification sended successfully");window.location="/sendnotifications"</script>'''
    if 'action' in request.args:
         action=request.args['action']
         id=request.args['id']
         if action=='delete':
            qry3="delete from notification where notification_id='%s'"%(id)
            delete(qry3)
            return ''' <script>alert("Deleted successfully");window.location="/sendnotifications"</script>'''
         if action=='update':
            qry4="select * from notification where notification_id='%s'"%(id)
            data['up']=select(qry4)
            if 'update' in request.form:
                 title=request.form['noti']
                 description=request.form['des']
                 q="update notification set title='%s',description='%s' where notification_id='%s'"%(title,description,id)
                 update(q)
                 return ''' <script>alert("Edited successfully");window.location="/sendnotifications"</script>'''
   

    return render_template("sendnotifications.html",data=data)






@admin.route("/chatwclient",methods=['get','post'])
def chatwclient():
    data={}
    qry6="select * from chat"
    data['user']=select(qry6)
   

    return render_template("chatwclient.html",data=data)

@admin.route("/adminsendreply",methods=['get','post'])
def adminsendreply():
    id=request.args['id']
    if 'send' in request.form:
        reply=request.form['rep']
       

        qry="update complaints set reply ='%s' where complaint_id='%s'"%(reply,id)
        update(qry)
        return ''' <script>alert("send successfully");window.location="/viewcomplaints"</script>'''
   
   
   

    return render_template("adminsendreply.html")

