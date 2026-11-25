from fastapi import FastAPI

from database import Base, engine
from models import Product
from router import product_router, category_router, customer_router

app = FastAPI(title= "Order Management API", description= "Backend API for managing inventory", version="1.0.0")

Base.metadata.create_all(bind= engine)
# SQLAlchemy checks the registered models and creates any tables that don't already exist.
app.include_router(product_router.router)
app.include_router(category_router.router)
app.include_router(customer_router.router)


@app.get("/")
def home():
    return {"message": "Welcome to Inventory management API"}


