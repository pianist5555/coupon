import random
from typing import List
from sqlalchemy.orm import Session
from db import models
from app.coupon_manager import CouponManager


def get_coupon_issuance_for_issue(
    db: Session,
    coupon_manager: CouponManager,
) -> List[models.CouponIssuance]:
    coupon_info = coupon_manager.pop_coupon()
    coupon_issuance = models.CouponIssuance(
        coupon_info_id = coupon_info.id,
    )

    return coupon_issuance


def get_coupon_info(
    db: Session,
) -> models.CouponInfo:
    coupon_info = db.query(models.CouponInfo).all()
    return coupon_info


def add_coupon_info(
    db: Session,
    code: str = None,
) -> str:
    coupon_info = models.CouponInfo(
        code = code,
    )
    db.add(coupon_info)
    db.commit()
    #db.flush()

    return coupon_info.code


def add_coupon_issuance(
    db: Session,
):
    coupon_issuance = models.CouponIssuance(
        coupon_info_id = models.CouponInfo,
    )
    db.add(coupon_issuance)
    db.commit()
    db.flush()


def issue_coupon(
    db: Session,
    coupon_issuance: models.CouponIssuance,
    coupon_manager: CouponManager,
):
    if coupon_manager.check_limit_coupon():
        coupon_manager.use_coupon(coupon_issuance)

        print(f'쿠폰 발급 성공 쿠폰 ID: {coupon_issuance.coupon_info_id}')
    else:
        print(f'쿠폰 발급 실패 쿠폰 제한: {coupon_manager.get_limit_coupon}') # TODO: 태스크들 멈추게하면 좋을듯

    return coupon_issuance.coupon_info_id