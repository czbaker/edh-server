import strawberry

# Import Types
from .user import UserMutation, UserQuery

# Define Root Types
@strawberry.type
class RootQuery(UserQuery):
    pass

@strawberry.type
class RootMutation(UserMutation):
    pass