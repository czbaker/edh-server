import strawberry
from datetime import datetime

@strawberry.type(name="Profile")
class Profile:
    city: str | None = None
    state: str | None = None
    zip: int | None = None
    facebook: str | None = None
    twitter: str | None = None
    bluesky: str | None = None
    twitch: str | None = None

@strawberry.type(name="User")
class User:
    username: str
    password: str
    email: str
    verified: bool
    createdAt: datetime
    profile: Profile | None = None    # Optional!

@strawberry.type(name="Hello")
class Hello:
    name: str
