from fastapi import APIRouter,Depends
from database import session_dependency
from sqlalchemy.orm import Session
from controllers.orderController import orderController
import schemas

router = APIRouter()

@router.post("/", status_code=201,response_model=schemas.orderResponce)
def create_order(order_in:schemas.orderCreateValidate,db:Session= Depends(session_dependency)):
    return orderController.orderCreate(order_in=order_in,db=db)


@router.get("/{id}", response_model=schemas.orderInfoResponce,status_code=200)
def get_order(id: int,db:Session= Depends(session_dependency)):
    return orderController.orderGet(id=id,db=db)


@router.post("/{id}", status_code=204)
def update_order(id: int,db:Session= Depends(session_dependency)):
    return orderController.orderUpdate(id=id,db=db)