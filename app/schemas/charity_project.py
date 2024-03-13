from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, Extra, Field, StrictInt, PositiveInt


class CharityProjectBase(BaseModel):
    name: str = Field(
        ..., min_length=1, max_length=100
    )
    description: str = Field(
        ..., min_length=1
    )
    full_amount: Union[StrictInt, PositiveInt] = Field(...)

    class Config:
        extra = Extra.forbid


class CharityProjectCreate(CharityProjectBase):
    pass


class CharityProjectUpdate(CharityProjectBase):
    pass


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: PositiveInt = Field(...)
    fully_invested: bool = Field(...)
    create_date: datetime = Field(...)
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
