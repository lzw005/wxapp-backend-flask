from orm import db


class UserInfo(db.Model):
    __tablename__ = 'user_info'
    __table_args__ = {'mysql_collate':'utf8_general_ci'}
    openid = db.Column(db.String(50), primary_key=True)
    nickName = db.Column(db.String(20))
    gender = db.Column(db.String(5))
    city = db.Column(db.String(20))
    province = db.Column(db.String(20))

    def __repr__(self):
        return '<UserInfo {}>'.format(self.openid)