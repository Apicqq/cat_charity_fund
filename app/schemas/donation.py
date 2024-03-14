from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt, StrictInt, Extra


class DonationBase(BaseModel):
    full_amount: PositiveInt = Field(...)
    comment: Optional[str]

    class Config:
        extra = Extra.forbid


class DonationCreate(DonationBase):
    pass


class DonationDBShort(DonationBase):
    id: int
    full_amount: PositiveInt = Field(...)
    create_date: datetime = Field(...)

    class Config:
        orm_mode = True


class DonationDBFull(DonationDBShort):

    user_id: int = Field(...)
    invested_amount: StrictInt = Field(...)
    fully_invested: bool = Field(...)
    close_date: Optional[datetime] = Field(...)
