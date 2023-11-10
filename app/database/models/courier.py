from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.orm import relationship
from database import Base

class Courier(Base):
    __tablename__ = 'couriers'
    
    id = Column(Integer,autoincrement=True ,primary_key=True, index=True)
    name = Column(String(20), unique=True,nullable=False)
    districts = Column(ARRAY(String(20)), index=True,nullable=False)

    orders = relationship("Order", back_populates="courier")