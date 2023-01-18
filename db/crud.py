import random
from typing import List
from sqlalchemy.orm import Session
from db import models


def get_coupon_info(
    db: Session,
):
    coupon_info = db.query(models.CouponInfo)
    return coupon_info


def get_coupon_inssuance(
    db: Session,
):
    coupon_inssuance = db.query(models.CouponIssuance)
    return coupon_inssuance


def update_get_coupon_info(
    db: Session,
    coupon_info_id_list: List,
):
    db.query(models.CouponInfo).filter(
            models.CouponInfo.id.in_(coupon_info_id_list)
        ).update(
            {
                'code': 'YYYY'
            }
        )
    db.commit()
    db.flush()


def add_coupon_info(
    db: Session,
):
    coupon_info = models.CouponInfo(
        code = 'XXXX',
    )
    db.add(coupon_info)
    db.commit()
    db.flush()


def add_coupon_issuance(
    db: Session,
):
    coupon_issuance = models.CouponIssuance(
        coupon_info_id = models.CouponInfo,
    )
    db.add(coupon_issuance)
    db.commit()
    db.flush()
