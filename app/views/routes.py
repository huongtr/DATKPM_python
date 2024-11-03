from flask import render_template, jsonify, request
from marshmallow import ValidationError
from app import APP, db
from flask import jsonify, request
from marshmallow import ValidationError
from app import APP, db
from app.repositories import UserRepository
from app.schemas import UserSchema
from app.service_layer import services

user_schema = UserSchema()

@APP.route('/')
@APP.route('/index')
def index():
    user = {'user_name': 'User01', 'email': 'test01@eh.com', 'password': 'secret123'}
    return render_template('index.html', title='Home', user=user)


# POST http://127.0.0.1:5000/signup
# {
#     "user": {
#     "username": "test03",
#     "email": "test03@eh.com",
#     "password": "123456"
#     }
# }
# Response:
# 201, {
#        "data": {
#                "user_id": 3
#            },
#            "message": "User created successfully"
#        }
@APP.route('/signup', methods=['POST'])
def signup():
    try:
        # Validate and load user data from the request
        user_data = user_schema.load(request.json.get('user'))
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400

    try:
        user_repo = UserRepository()
        user = services.register_user(user_data, user_repo)
        return jsonify({
            'message': 'User created successfully',
            'data': {'user_id': user.id}
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


# POST http://127.0.0.1:5000/login
# {
#     "username": "test01",
#     "password": "123456"
# }
# Response:
# 201, {
#     "data": {
#         "email": "test01@eh.com",
#         "id": 1,
#         "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MX0.jp4LgLHFDaQes0hVQMulCGxWLadOsNG0DPArlaWeFs0",
#         "username": "test01"
#     },
#     "message": "Logged in successfully"
# }
@APP.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user_repo = UserRepository()
    try:
        user = services.login_user(username, password, user_repo)
        return jsonify({
            'message': 'Logged in successfully',
            'data': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'token': services.generate_jwt(user)
            }
        }), 200
    except services.ServiceException as e:
        return jsonify({'error': str(e)}), 401
