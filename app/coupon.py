import hashlib
from typing import List
from datetime import datetime
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
) -> List:
    coupons = []
    for _ in range(150):
        test_password = datetime.now()
        after_password = str(test_password.timestamp()).encode('utf-8')
        password_hash = hashlib.new('sha256')
        password_hash.update(after_password)
        code = password_hash.hexdigest()
        coupons.append(
            crud.add_coupon_info(
                db=db,
                code=code
            )
        )
    return coupons