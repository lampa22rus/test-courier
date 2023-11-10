from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import session_dependency

from controllers.courierController import courierController

import schemas

from typing import List

router = APIRouter()

@router.post("/",status_code=201)
def courier_create(courier_in: schemas.courierCreate,db:Session= Depends(session_dependency)):
    return courierController.Create(courier_in=courier_in,db=db)

@router.get("/" , response_model=List[schemas.courierBase] , status_code=200)
def show_all(db:Session= Depends(session_dependency)):
    return courierController.showAll(db=db)


@router.get("/{id}",response_model=schemas.infoCourierResponce,status_code=200)
def show_Id(id: int,db:Session= Depends(session_dependency)):
    return courierController.showId(id=id,db=db)


