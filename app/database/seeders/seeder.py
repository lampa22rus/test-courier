from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionScoped,Base
from database.seeders.courierSeeder import userSeed


class seeder():
    def run(count=10):
        userSeed(coint=count,db=SessionScoped)
        

    