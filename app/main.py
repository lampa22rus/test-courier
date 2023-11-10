from fastapi import FastAPI
from database.seeders.seeder import seeder
from routers.couriers import router as couriers_router
from routers.orders import router as orders_router
import uvicorn
import argparse

# args
parser = argparse.ArgumentParser()
parser.add_argument('--server')

# fastapi
app = FastAPI()

app.include_router(
    router=couriers_router,
    prefix='/courier',
)
app.include_router(
    router=orders_router,
    prefix='/order',
)

if __name__ == "__main__":
    args = parser.parse_args()
    if(args.server == "seed"):
        seeder.run()