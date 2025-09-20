from pydantic import BaseModel


class UserRequest(BaseModel):
    Username: str
