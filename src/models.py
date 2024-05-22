from pydantic import BaseModel

class Job(BaseModel):
    title: str
    location: str


# We will attempt to extract the location from the bio (None otherwise)
class Member(BaseModel):
    name: str
    bio: str
    location: str = None
