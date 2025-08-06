import strawberry

# RootQuery + RootMutation
from .types import RootQuery

# Build...
@strawberry.type
class Query(RootQuery):
    pass

# Schema Definition
schema = strawberry.Schema(query=Query)