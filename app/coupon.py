import hashlib
import asyncio
import requests
from typing import List
from datetime import datetime
from db import crud
from sqlalchemy.orm import Session
from app.coupon_manager import CouponManager


async def get_coupon_info(
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
    '''
        쿠폰 150개 생성
    '''
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


async def issue_coupon(
    db: Session,
):
    coupon_manager = CouponManager.instance()
    coupon_issuance = crud.get_coupon_issuance_for_issue(db, coupon_manager)
    result = crud.issue_coupon(db, coupon_issuance, coupon_manager)
    
    return result

async def api_routine():
    res = requests.get(f'http://127.0.0.1:8001/coupon/issue_coupon')
    return res.text

async def call_api():
    futures = []
    for _ in range(0,150):
        futures.append(api_routine())

    result = []
    for res in  await asyncio.gather(*futures):
        result.append(res)

    return result