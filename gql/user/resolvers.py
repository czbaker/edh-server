# User/Profile Resolvers
from datetime import datetime
from .models import UserDocument

def create_user(self, username: str, password: str, email: str) -> UserDocument:
    print(f'Calling create_user!')
    try:
        newUser = UserDocument(
            username=username,
            password=password,
            email=email,
            verified=False,
            createdAt=datetime.now()
        )
        newUser.save()
        return newUser
    except Exception as e:
        raise e
    


def user_test(self, username: str, password: str, email: str) -> str:
    newUser = UserDocument(
        username=username,
        password=password,
        email=email,
        verified=False,
        createdAt=datetime.now()
    )
    return newUser