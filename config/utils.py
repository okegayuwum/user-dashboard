import os
import logging
from typing import List, Optional
from pydantic import BaseModel

def get_project_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class User(BaseModel):
    id: int
    name: str
    email: str

def get_users() -> List[User]:
    users_file = os.path.join(get_project_root(), 'data', 'users.json')
    if os.path.exists(users_file):
        with open(users_file, 'r') as f:
            return [User(**user) for user in f.read()]
    else:
        return []

def get_user(user_id: int) -> Optional[User]:
    users = get_users()
    for user in users:
        if user.id == user_id:
            return user
    return None

def log_error(message: str):
    logging.error(message)