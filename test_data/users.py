from utils.config import (
    STANDARD_USERNAME,
    LOCKED_USERNAME,
    INVALID_USERNAME,
    PASSWORD
)

VALID_USER = {
    "username": STANDARD_USERNAME,
    "password": PASSWORD
}

INVALID_USER = {
    "username": INVALID_USERNAME,
    "password": PASSWORD
}

LOCKED_OUT_USER = {
    "username": LOCKED_USERNAME,
    "password": PASSWORD
}