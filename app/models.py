from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(20), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_activated(self):
        return True

    def is_anonymous(self):
        return True

    def getid(self):
        try:
            return unicode(self.id)
        except NameError:

            return str(self.id)
    def __repr__(self):
        return '<User %r>' %(self.nickname)
 
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
