import uvicorn
from fastapi import FastAPI
from routers import client
from db.database import Base
from db.database import postgres_engine

Base.metadata.create_all(bind=postgres_engine)

app = FastAPI(title="coupon",description="Coupon",version="0.1.0",redoc_url=None)
app.include_router(client.router,prefix="/coupon", tags=["쿠폰 API"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, loop='asyncio')