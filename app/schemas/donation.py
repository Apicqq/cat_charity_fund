from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, Field, PositiveInt, StrictInt, Extra


class DonationBase(BaseModel):
    full_amount: Union[PositiveInt, StrictInt] = Field(...)
    comment: Optional[str] = Field(...)

    class Config:
        extra = Extra.forbid


class DonationCreate(BaseModel):
    pass


class DonationDBShort(DonationBase):
    id: int
    create_date: datetime = Field(...)

    class Config:
        orm_mode = True


class DonationDBFull(DonationBase):

    id: int
    create_date: datetime = Field(...)
    user_id: int = Field(...)
    invested_amount: StrictInt = Field(...)
    fully_invested: bool = Field(...)
    close_date: Optional[datetime] = Field(...)

    class Config:
        orm_mode = True
