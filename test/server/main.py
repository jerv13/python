from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:p@localhost/python'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/user', methods=['POST'])
def create_user():
    import user.model as model

    content = request.get_json()
    # request.method
    # @todo Validation??
    user = model.create_user(content['username'], content['email'])

    return 'User created: %s' % user.id


@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    import user.model as model
    user = model.get_user(id)
    return jsonify(user.to_dict())


if __name__ == "__main__":
    app.run()
