from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.customer import Customer

def create_customer(customer_data:dict, session: Session):
    customer = Customer(**customer_data)
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

def get_all_customers(session: Session):
    customers = select(Customer).order_by(Customer.id)
    return session.scalars(customers).all()   

def get_customers_by_id(id: int, session: Session):
    customer = select(Customer).where(Customer.id == id)
    return session.scalar(customer)

def delete_customer_by_id(id: int, session: Session):
    customer = get_customers_by_id(id, session)
    if customer is None:
        return None
    session.delete(customer)
    session.commit()

    return id

def update_customer_by_id(customer: Customer,updated_data: dict, session:Session):
    try:
        for field, value in updated_data.items():
            setattr(customer, field, value)
        session.commit()
        session.refresh(customer)

    except IntegrityError: 
        session.rollback()
        raise
