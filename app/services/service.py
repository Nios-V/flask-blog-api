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
    
    def before_create(self, data):
        """Hook method to modify data or validate before creation."""
        return data
    
    def create(self, data):
        """Create a new record."""
        data = self.before_create(data)
        record = self.model(**data)
        db.session.add(record)
        db.session.commit()
        self.after_create(record)
        return record
    
    def after_create(self, record):
        """Hook method to perform actions after creation."""
        pass

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
