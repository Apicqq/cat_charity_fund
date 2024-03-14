from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user, current_superuser
from app.crud import donation_crud, charity_crud
from app.models import Donation, User
from app.schemas.donation import DonationDBShort, DonationDBFull, \
    DonationCreate
from app.services.investments import do_run_investments

router = APIRouter()


@router.get(
    "/",
    response_model=list[DonationDBFull],
    dependencies=[Depends(current_superuser)]
)
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session)
):
    return await donation_crud.get_all(session)


@router.post(
    "/",
    response_model=DonationDBShort,
    response_model_exclude={"user_id"},
    response_model_exclude_none=True
)
async def create_donation(
        donation: DonationCreate,
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session)
) -> Donation:
    donation = await donation_crud.post(donation, session, user)
    await do_run_investments(donation, charity_crud, session)
    return donation


@router.get(
    "/my",
    response_model=list[DonationDBShort],
    response_model_exclude={"user_id"}
)
async def get_own_donations(
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session)
) -> list[Donation]:
    return await donation_crud.get_own_donations(user, session)
