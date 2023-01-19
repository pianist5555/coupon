from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from app import coupon
from common import utils


router = APIRouter()

@router.get("/create", name="쿠폰 생성")
def create(
    db: Session = Depends(get_db),
) -> List:
    response = coupon.add_coupon_info(db)
    return response


@router.get("/issue_coupon", name="쿠폰 발급 (선착순)")
async def issuance(
    db: Session = Depends(get_db),
):
    return await coupon.issue_coupon(db)


@router.get("/call/api", name="API 콜")
async def call_api():
    result = await coupon.call_api()
    return result


@router.get("/test", name="테스트")
def test(
    db: Session = Depends(get_db),
):
    coupon_info = coupon.get_coupon_info(db)
    coupon_inssuance = coupon.get_coupon_inssuance(db)