from enum import Enum, IntEnum


class ErrConstants(str, Enum):
    NAME_IS_BUSY = "This name is already occupied"
    NOT_FOUND = "Not Found"
    CANNOT_MODIFY_CLOSED_PROJECT = (
        "You cannot modify a project that was closed"
    )
    CANNOT_DELETE_PROJECT_WITH_INVESTMENTS = (
        "You cannot delete a project that has some investments"
    )
    FULL_AMOUNT_LT_INVESTED_AMOUNT = (
        "You cannot set full amount that is less" "than invested amount"
    )
    PASSWORD_TOO_SHORT = "Password should be at least 3 characters"
    EMAIL_IN_PASSWORD = "Password should not contain e-mail"


class DBConstants(IntEnum):
    INVESTED_AMOUNT_DEFAULT = 0
    CHARITY_PROJECT_NAME_DEFAULT = 100


class ConfigConstants(str, Enum):
    APP_TITLE = "QRKot"
    DESCRIPTION = (
        "API for the Charity application QRKot cat support fund."
    )
    DATABASE_URL = "sqlite+aiosqlite:///./fastapi.db"
    SECRET = "VeryDamnSecretSecret"


class SchemaConstants(IntEnum):

    CHARITY_PROJ_FIELD_MIN_LENGTH = 1
    CHARITY_PROJ_FIELD_MAX_LENGTH = 100
