import hashlib
from datetime import datetime


class User:
    def __init__(self, 
                id : int, 
                username : str, 
                password : str, 
                first_name : str,
                last_name : str, 
                phone : str, 
                birth_date : str, 
                created_at : str, 
                role : str = "Passenger"):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.birth_date = birth_date
        self.created_at = created_at
        self.role = role

    def hash_password(self, raw_password):
        return hashlib.sha256(raw_password.encode()).hexdigest()

    def set_password(self, raw_password):
        self.password = self.hash_password(raw_password)

    def check_password(self, raw_password):
        return self.password == self.hash_password(raw_password)

    def to_dict(self):
        
        role_value = "Admin" if str(self.role).lower() == "admin" else "Passenger"
        created_at_value = self.created_at or str(datetime.now())

        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "birth_date": self.birth_date,
            "created_at": created_at_value,
            "role": role_value
        }