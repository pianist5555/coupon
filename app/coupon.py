from db import crud
from sqlalchemy.orm import Session


def get_coupon_info(
    db: Session,
):
    return crud.get_coupon_info(db)


def get_coupon_inssuance(
    db: Session,
):
    return crud.get_coupon_inssuance(db)


def update_get_coupon_info(
    db: Session,
):
    return crud.update_get_coupon_info(db)


def add_coupon_info(
    db: Session,
):
    return crud.add_coupon_info(db)