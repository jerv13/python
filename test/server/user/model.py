from main import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    # @todo Extractor
    def to_dict(self):
        return {
        'id': self.id,
        'username': self.username,
        'email': self.email
        }

    # def __init__(self, username, email):
    #     self.username = username
    #     self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


def create_user(properties):
    # @todo Validate properties
    new_user = User()
    new_user = hydrate(new_user, properties)
    db.session.add(new_user)
    db.session.commit()
    print 'User created: %s' % new_user.id
    return new_user


def get_user(id):
    db.session.commit()
    user = db.session.query(User).filter_by(id=id).first()
    print 'User get: %s' % user

    return user


def update_user(id, properties):
    
    user = get_user(id)

    if user is None:
        return None

    user = hydrate(user, properties)

    db.session.commit()

    print 'User update: %s' % user.username

    return user


def hydrate(user, properties):
    if type(user) is not User:
        # @todo Throw error
        return user

    if properties.has_key('username'):
        user.username = properties['username']

    if properties.has_key('email'):
        user.email = properties['email']

    return user
