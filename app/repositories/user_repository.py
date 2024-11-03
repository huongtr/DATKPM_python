from app.models import User
from .base_repository import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    def find_by_email(self, email):
        return self.model.query.filter_by(email=email).first()

    def find_by_username(self, username):
        return self.model.query.filter_by(username=username).first()

