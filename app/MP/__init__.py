from flask import Blueprint , render_template ,request ,jsonify
from app.database.smdb import DataManager
from app import teachers

dm = DataManager()
users_module = Blueprint('MP' ,__name__)

@users_module.route('/user_edit' , methods=['GET' , 'POST'])
def user_edit():
    if request.method=='POST':
        records = dm.GetMP()
        print(records)
        return render_template('user_list.html', records=records)

@users_module.route('/add_user' , methods=['GET','POST'])
def add_user():
    if request.method=='POST':
        data = request.values
        dm.AddUser(data['login'],data['password'] , data['priv'])
        d = { 
            'add':True
        }
        return jsonify(d)

@users_module.route('/del_user' ,methods=['GET','POST'])
def del_user():
    if request.method=='POST':
        data = request.values['id']
        dm.DelUser(int(data))
    d = {'d':True}
    return jsonify(d)

@users_module.route('/load_teacher' , methods=['GET','POST'])
def load_teacher():
        teacher_list = teachers.query.all()
        return render_template('list_teachers.html' , teachers=teacher_list)