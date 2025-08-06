import strawberry

from .types import Hello
from .resolvers import say_hello

@strawberry.type
class HelloQuery:
    hello: str = strawberry.field(resolver=say_hello)
    