"""
file storage
"""
import json


class FileStorage:
    """
    file storage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns all object in __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        add a new obj in __objects
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        save the __odject dict in a file
        """
        my_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(my_dict, file)

    def reload(self):
        """
        reload all objects from file
        """
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        myClasses = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
                     "Place": Place, "Review": Review,
                     "State": State, "User": User}
        try:
            with open(FileStorage.__file_path) as file:
                data = json.load(file)
                for k, v in data.items():
                    FileStorage.__objects[k] = myClasses[v[("__class__")]](**v)
        except Exception:
            pass
