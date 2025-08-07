import strawberry

# RootQuery + RootMutation
from .types import RootMutation, RootQuery

# Build...
@strawberry.type
class Query(RootQuery):
    pass

@strawberry.type
class Mutation(RootMutation):
    pass

# Schema Definition
schema = strawberry.Schema(query=Query, mutation=Mutation)