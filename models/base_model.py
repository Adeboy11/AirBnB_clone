#!/usr/bin/python3
"""Base models
"""
import uuid
from datetime import datetime

class BaseModel:
    """Base Model init"""
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, time_format))
                else:
                    setattr(self, k, v)

        models.storage.new(self)

    def safe(self):
        """update the created time"""
        self.updated_at = datetime.utcnow()
        models.storage.save

    def to_dict(self):
        """returns dictionary containing all keys and values"""
        instance_dictionary = self.__dict__.copy()
        instance_dictionary["__class__"] = self.__class__.__name__
        instance_dictionary["created_at"] = self.created_at.isoformat()
        instance_dictionary["updated_at"] = self.updated_at.isoformat()
        return instance_dictionary
    
    def __str__(self):
        """prints all string representation of dict"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

