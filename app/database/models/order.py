import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP,Time,Enum
from sqlalchemy.orm import relationship
from enums.status import Status
from database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer ,autoincrement=True ,primary_key=True, index=True)
    name = Column(String(20),nullable=False)
    districts = Column(String(20),nullable=False)
    status = Column(Enum(Status,create_type=False),default=Status.works,nullable=True)
    created_at = Column(TIMESTAMP,default=datetime.datetime.utcnow(),nullable=False)
    execution_time = Column(Time, default=None, index=True)
    courier_id = Column(Integer, ForeignKey("couriers.id"),index=True,nullable=False)
    
    courier = relationship("Courier", back_populates="orders")