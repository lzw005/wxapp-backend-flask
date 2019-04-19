from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
import pymysql
import methods
from orm import db
from db_models import *
from flask_cors import *
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

# app.config[
#     'SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://mysql_user:mysql_user@wowsg.top:3306/wxapp?uft8mb4"
#
# app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config.from_object('settings.Config')
db.init_app(app)

migrate = Migrate(app, db)

manage = Manager(app)
manage.add_command('db', MigrateCommand)
manage.add_command('runserver', Server(host='0.0.0.0'))

CORS(app, support_credentials=True)     #跨域


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test_db')
def test_db():
    # methods.test_db()
    return 'success'

@app.route('/login',methods=['POST'])
def login():
    if request.method=='POST':
        openid = request.form.get('openid')
        nickName = request.form.get('nickName')
        gender = request.form.get('gender')
        city = request.form.get('city')
        province = request.form.get('province')
        print(openid,nickName,gender,city,province)
        if not UserInfo.query.get(openid):
            user_info = UserInfo(openid=openid, nickName=nickName, gender=gender, city=city, province=province)
            db.session.add(user_info)
            db.session.commit()
            return 'success'
        else:
            return 'already have'



if __name__ == '__main__':
    app.run()
    # manage.run()