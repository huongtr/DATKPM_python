import jwt
from app import APP
from app.models import User
from app.repositories import UserRepository


class ServiceException(Exception):
    pass

def register_user(user_data, user_repo: UserRepository):
    username = user_data['username']
    user = user_repo.find_by_username(username)
    if user:
        raise ValueError(f"User '{username}' already exists")

    user = User(**user_data)
    user_repo.add(user)
    return user

def login_user(username, password, user_repo: UserRepository):
    user = user_repo.find_by_username(username)
    if user and user.check_password(password):
        return user
    raise ServiceException("Invalid username or password")

def generate_jwt(user):
    token = jwt.encode({"id": user.id}, APP.config["JWT_SECRET_KEY"], algorithm="HS256")
    return token
