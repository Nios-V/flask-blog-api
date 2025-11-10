from app.models import db

class Service:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        """Get all records of the model."""
        return self.model.query.all()
    
    def get_by_id(self, id):
        """Get a single record by ID."""
        return self.model.query.get(id)
    
    def create(self, data):
        """Create a new record."""
        record = self.model(**data)
        db.session.add(record)
        db.session.commit()
        return record
    
    def update(self, id, data):
        """Update an existing record by ID."""
        record = self.get_by_id(id)
        if not record:
            return None
        
        for key, value in data.items():
            setattr(record, key, value)
        db.session.commit()
        return record
    
    def delete(self, id):
        """Delete a record by ID."""
        record = self.get_by_id(id)
        if not record:
            return None
        
        db.session.delete(record)
        db.session.commit()
        return record
