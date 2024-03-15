from datetime import datetime

from app.core.base import Base


def run_investments(
    target: Base,
    sources: list[Base],
) -> set[Base]:
    """
    Perform investment operations by distributing available funds.

    :param target: Base: The
        project or donation object to invest in.
    :param sources: list[Base]: The
        list of project or donation objects to distribute funds from.
    :returns: set[Base]: The set of project or donation objects.
    """
    changed_db_objects = set()
    if target.invested_amount is None:
        target.invested_amount = 0
    for source in sources:
        investment_amount = min(
            source.full_amount - source.invested_amount,
            target.full_amount - target.invested_amount,
        )
        for changed_object in (source, target):
            changed_object.invested_amount += investment_amount
            if changed_object.full_amount == changed_object.invested_amount:
                changed_object.fully_invested = True
                changed_object.close_date = datetime.now()
        changed_db_objects.add(source)
        if target.fully_invested:
            break
    return changed_db_objects
