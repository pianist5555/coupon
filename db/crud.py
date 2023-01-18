import random
from typing import List
from sqlalchemy.orm import Session
from db import models
from app.coupon_manager import CouponManager


def get_coupon_issuance_for_issue(
    db: Session,
) -> List[models.CouponIssuance]:
    coupon_infos = db.query(
        models.CouponInfo
    ).filter(
        models.CouponInfo.issuances == None
    ).all()

    coupon_issuances = [
        models.CouponIssuance(
            coupon_info_id = coupon_info.id,
        ) for coupon_info in coupon_infos
    ]
    return coupon_issuances


def get_coupon_inssuance(
    db: Session,
) -> models.CouponIssuance:
    coupon_inssuance = db.query(models.CouponIssuance).all()
    return coupon_inssuance


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
    while coupon_manager.check_duplicate_coupon(coupon_issuance): # 이미 존재하면 true를 리턴
        coupon_issuance = get_coupon_issuance_for_issue(db)

    if coupon_manager.check_limit_coupon():
        db.add(coupon_issuance)
        db.commit()
        db.flush()
        coupon_manager.add_coupon(coupon_issuance)

        print(f'쿠폰 발급 성공 쿠폰 ID: {coupon_issuance.coupon_info_id}')
    else:
        print(f'쿠폰 발급 실패 쿠폰 제한: {coupon_manager.get_limit_coupon}') # 태스크들 멈추게하면 좋을듯

    return coupon_issuance.coupon_info_id