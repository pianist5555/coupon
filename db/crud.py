import random
from typing import List
from sqlalchemy.orm import Session
from db import models


async def get_coupon_issuance_for_issue(
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
    code: str = None,
) -> str:
    coupon_info = models.CouponInfo(
        code = code,
    )
    db.add(coupon_info)
    db.commit()
    db.flush()

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
    coupon_issuance: models.CouponIssuance
):
    print(f'쿠폰 발급: {coupon_issuance.coupon_info_id}')
    db.add(coupon_issuance)
    db.commit()
    # db.flush()
    return coupon_issuance.coupon_info_id