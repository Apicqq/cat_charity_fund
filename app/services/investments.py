from datetime import datetime
from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation
from crud.base import CRUDBase


async def do_run_investments(obj_in: Union[CharityProject, Donation],
                             crud_class: CRUDBase,
                             session: AsyncSession) -> None:
    """
    Perform investment operations by distributing available funds to projects.

    :param obj_in:  (Union[CharityProject, Donation]): The
        project or donation object to invest in.
    :param crud_class: (CRUDBase): The CRUD class for interacting
        with the database.
    :param session: (AsyncSession): The async session to use for
        the database operations.
    :returns: None
    """
    receptions = await crud_class.get_not_closed_projects(session)
    for reception in receptions:
        available_to_invest = obj_in.full_amount - obj_in.invested_amount
        if not available_to_invest:
            break
        available = reception.full_amount - reception.invested_amount
        to_add = min(available_to_invest, available)
        reception.invested_amount += to_add
        obj_in.invested_amount += to_add
        close_object(reception)
    close_object(obj_in)
    await crud_class.push_to_db(obj_in, session)


def close_object(obj: Union[CharityProject, Donation]) -> None:
    """
    Close object if fully invested.
    :param obj: Incoming object of type CharityProject or Donation
    :returns: None
    """

    obj.fully_invested = (obj.full_amount == obj.invested_amount)
    if obj.fully_invested:
        obj.close_date = datetime.now()
