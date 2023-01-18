from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text, BigInteger
from sqlalchemy.orm import relationship

from db.database import Base


class CouponInfo(Base):
    __tablename__ = "coupon_info"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Text(), comment = '발급 코드')

    issuances  = relationship("CouponIssuance")


class CouponIssuance(Base):
    __tablename__ = "coupon_issuance"

    id = Column(Integer, primary_key=True, index=True)
    coupon_info_id = Column(Integer, ForeignKey('coupon_info.id'))
    add_date = Column(DateTime, default = datetime.now(), comment = '발급일')
    use_date = Column(DateTime, default = None, comment = '사용일')
    
