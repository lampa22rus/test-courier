
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from database.models.courier import Courier
from sqlalchemy import  func    
from database.models.order import Order
from enums.status import Status
from controllers.helper import get_time
from datetime import timedelta

class courierController():

    def Create(db:Session, courier_in):
        """
            Получение всех курьеров
        """
        result: Result = db.query(Courier).where(Courier.name == courier_in.name).first()
        
        if result:
            raise HTTPException(
                status_code=409,
                detail="The courier already exists"
            )

        courier: Courier = Courier(**courier_in.model_dump())

        db.add(courier)
        db.commit()
        return JSONResponse({'detail': 'success'})

    def showAll(db:Session):
        """
            Получение всех курьеров
        """
        return db.query(Courier).all()

    def showId(id, db: Session):
        """
            Получение курьера по id
        """
        courier: Courier = db.get(Courier,id)
        if not courier:
            raise HTTPException(
                status_code=404,
                detail="Courier not found"
            )
            
        avg_time:timedelta = db.query(func.avg(Order.execution_time)).join(Courier).filter(Courier.id == id).scalar()   
        
        subquery = db.query(func.count(Order.id)).filter(
            Order.courier_id == id, 
            Order.status == Status.complited
        ).group_by(func.date(Order.created_at)).subquery()
        
        avg_day:float = db.query(func.avg(subquery.c.count)).scalar()
        
        active_order:Order = db.query(Order).filter(
            Order.courier_id == id,
            Order.status == Status.works
        ).first() 
        
        response = {
            'active_order': active_order,
            'avg_order_complete_time':  get_time(avg_time),
            'avg_day_orders': int(avg_day) 
        }
        return response
