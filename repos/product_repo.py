from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.products import Product

def create_product(db: Session, product_data:dict):
    try:
        product = Product(**product_data)
        db.add(product)
        db.commit()
        db.refresh(product)
        return product
    except IntegrityError:
        db.rollback()
        raise

def get_products(db:Session):
    products = select(Product).order_by(Product.id)
    return db.scalars(products).all()

def get_product_by_id(session: Session, id: int):
    rawSingleProductObjectFromTuple = select(Product).where(Product.id == id)
    return session.scalar(rawSingleProductObjectFromTuple)

def delete_by_id(session: Session, id: int):
    product = get_product_by_id(session, id)

    if product is None:
        return None
    
    session.delete(product)
    session.commit()
    return id

def product_patch_put(session: Session, product: Product, update_data: dict):
    for field, value in update_data.items():
        setattr(product, field, value)

    session.commit()
    session.refresh(product)
    return product

#         product.name = update_data["name"]
#         product.description = update_data["description"]
#         product.sku = update_data["sku"]
#         product.price = update_data["price"]
#         product.stock = update_data["stock"]

def get_product_by_sku(session: Session, sku: str):
    query = select(Product).where(Product.sku == sku)
    return session.scalar(query)