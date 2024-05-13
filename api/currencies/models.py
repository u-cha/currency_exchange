from pydantic import BaseModel, Field


class Currency(BaseModel):
    code: str = Field(min_length=3, max_length=3)
    fullname: str = Field(min_length=1)
