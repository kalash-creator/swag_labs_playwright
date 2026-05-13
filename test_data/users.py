from utils.config import (
    STANDARD_USER,
    LOCKED_USER,
    FAULTY_USERNAME,
    PASSWORD
)

VALID_USER = {
    "username": STANDARD_USER,
    "password": PASSWORD
}

INVALID_USER = {
    "username": FAULTY_USERNAME,
    "password": PASSWORD
}

LOCKED_OUT_USER = {
    "username": LOCKED_USER,
    "password": PASSWORD
}