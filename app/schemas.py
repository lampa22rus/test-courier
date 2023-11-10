from typing import List, Optional, Dict,Union
from pydantic import BaseModel, Field
from datetime import time

class courierBase(BaseModel):
    id: int
    name: str
    
class orderInfoResponce(BaseModel):
    courier_id: int
    status: int
    
class infoOrderResponce(BaseModel):
    order_id: int = Field(alias='id')
    order_name: str = Field(alias='name')
    
class infoCourierResponce(BaseModel):
    active_order: Optional[Union[infoOrderResponce, None]]
    avg_order_complete_time: time
    avg_day_orders: int

class orderResponce(BaseModel):
    id:int 
    courier_id:int
  
    class Config:
        allow_population_by_field_name = True
    

class orderCreateValidate(BaseModel):
    name: str
    districts: str

class courierCreateValidate(BaseModel):
    name: str 
    districts: List[str]
    
class showAll(BaseModel):
    Dict[str,courierBase]
    class Config:
        orm_mode = True
        
courierCreate = courierCreateValidate