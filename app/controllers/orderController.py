from database.models.order import Order
from database.models.courier import Courier
from sqlalchemy import not_
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from enums.status import Status
import datetime


class orderController():

    def orderCreate(order_in, db: Session):
        """
            Создание заказа
        """
        courier: Courier = db.query(Courier).filter(
            Courier.districts.any(order_in.districts),
            not_(Courier.orders.any(Order.status == Status.works)),
        ).first()

        if not courier:
            raise HTTPException(
                status_code=404,
                detail="Сourier not found"
            )
            
        order: Order = Order(
            **order_in.model_dump(),
            created_at=datetime.datetime.utcnow()
        )
        courier.orders.append(order)
        db.commit()
        db.refresh(order)
        return order

    def orderGet(id, db: Session):
        """
            Получение заказа
        """
        order: Order = db.get(Order, id)

        if not order:
            raise HTTPException(
                status_code=404,
                detail="Order not found"
            )

        data = {
            'courier_id': order.courier_id,
            'status': Status(order.status).value
        }

        return data

    def orderUpdate(id, db: Session):
        """
            обновление заказа
        """
        order: Order = db.query(Order).options(joinedload(Order.courier)).get(id)

        if not order:
            raise HTTPException(
                status_code=404,
                detail="Order not found"
            )

        if (order.status == Status.complited):
            raise HTTPException(
                status_code=406,
                detail="The order is completed"
            )

        order.execution_time =  datetime.datetime.utcnow()-order.created_at
        order.status = Status.complited

        db.commit()

        return JSONResponse({'detail': 'success'})
