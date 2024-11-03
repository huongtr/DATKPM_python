from sqlalchemy.exc import SQLAlchemyError
from app import db

class BaseRepository:
    def __init__(self, model):
        self.model = model  # Model is passed in when initializing the repository

    def add(self, entity):
        """Add a new entity to the database."""
        try:
            db.session.add(entity)
            db.session.commit()
            return entity
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error adding entity: {e}")
            return None

    def get_by_id(self, id):
        """Retrieve an entity by its ID."""
        return self.model.query.get(id)

    def list(self):
        """List all entities in the model's table."""
        return self.model.query.all()

    def delete(self, entity):
        """Delete an entity from the database."""
        try:
            db.session.delete(entity)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error deleting entity: {e}")

    def update(self):
        """Commit changes to an existing entity."""
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error updating entity: {e}")
