import strawberry

from .resolvers import create_user
from .types import User

@strawberry.type
class UserMutation:
    createUser: User = strawberry.mutation(resolver=create_user)
