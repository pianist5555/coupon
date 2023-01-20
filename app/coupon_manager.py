from db import crud
from db.database import get_db

class CouponManager(): 
    '''
    singleton pattern class for coupon

    싱글턴 패턴으로 issue_coupon 함수로 쿠폰을 발급할 때
    self._coupon_list 쿠폰 번호가 존재하면 다른 쿠폰을 사용한다
    (성능 리팩토링은 나중에)
    '''
    __instance = None

    
    def __init__(self):
        db = next(get_db())
        self._coupon_list = crud.get_coupon_info(db=db)
        self._used_coupon_list = []
        self._limit_coupon = 100

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance

    @property
    def get_coupon_list(self):
        return self._coupon_list 

    @property
    def get_limit_coupon(self):
        return self._limit_coupon

    def use_coupon(self, coupon):
        self._used_coupon_list.append(coupon)

    def pop_coupon(self):
        return self._coupon_list.pop()

    def check_duplicate_coupon(self, coupon):
        if coupon in self._used_coupon_list:
            return True
        else:
            return False

    def check_limit_coupon(self): # 현재 메모리에 올라가 있는 쿠폰 리스트로 판단하기 때문에 다음 API에서는 소용이 없음, 최초에 db에서 한번 땡겨오는 형식으로 바꿔야함
        if self._limit_coupon > len(self._coupon_list):
            return True
        else:
            return False
    
