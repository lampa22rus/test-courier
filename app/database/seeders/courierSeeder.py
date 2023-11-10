import random
from faker import Faker
from fastapi import Depends
from sqlalchemy.orm import Session
from enums.status import Status
from database import session_dependency

from database.models.courier import Courier
from database.models.order import Order

def userSeed(coint:int,db:Session):
    responce = db.query(Courier).first()
    if not responce: 
        fake:Faker = Faker()
        
        for _ in range(coint):   
            courierData = {
                'name' : fake.first_name(),
                'districts' : [fake.city() for _ in range(random.randint(1, 5))]
            }
            
            orderData = {
                'name' : fake.bothify(text='????????'),
                'districts' : random.choice(courierData['districts']),
            }
            
            courier:Courier = Courier(**courierData)
            courier.orders.append(Order(**orderData))
            db.add(courier)
            
        db.commit()
        db.close()