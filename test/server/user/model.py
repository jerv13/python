from main import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def to_dict(self):
        return {
        'id': self.id,
        'username': self.username,
        'email': self.email
        }

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


def create_user(username, email):
    new_user = User('username', 'email@email.com')
    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_user(id):
    user = db.session.query(User).filter_by(id=id).one()
    db.session.refresh(user)
    print 'User GET: %s' % user.username

    return user
