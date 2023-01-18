import hashlib
import asyncio
from typing import List
from datetime import datetime
from db import crud
from sqlalchemy.orm import Session


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
    loop = asyncio.get_running_loop()
    coupon_issuances = await crud.get_coupon_issuance_for_issue(db)
    
    futures = []
    for coupon_issuance in coupon_issuances:
        futures.append(
            loop.run_in_executor(
                None,
                crud.issue_coupon,
                db,
                coupon_issuance
            )
        )

    result = []
    for res in await asyncio.gather(
        *futures
    ):
        result.append(res)

    print(result)
    