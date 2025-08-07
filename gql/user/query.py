import strawberry

from .resolvers import user_test
from .types import User

@strawberry.type
class UserQuery:
    userTest: User = strawberry.field(resolver=user_test)