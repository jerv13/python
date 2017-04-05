from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:p@localhost/python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/user', methods=['POST'])
def create_user():
    import user.model as model

    properties = request.get_json()
    # @todo Validate properties

    user = model.create_user(properties)
    return jsonify(user.to_dict())

@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    import user.model as model

    properties = request.get_json()
    # @todo Validate properties

    user = model.update_user(id, properties)
    return jsonify(user.to_dict())

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    import user.model as model
    user = model.get_user(id)

    if user is None:
        return 'null', 404

    return jsonify(user.to_dict())


if __name__ == "__main__":
    app.run()
