import strawberry

# Import Types
from .hello import HelloQuery

# Define Root Types
@strawberry.type
class RootQuery(HelloQuery):
    pass