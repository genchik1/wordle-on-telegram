from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int  # noqa: A003 VNE003
    utm: str | None = None
    allows_write_to_pm: bool = True
    username: str
