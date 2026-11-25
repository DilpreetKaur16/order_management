from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.category import Category

def create_category(session: Session, category_data: dict):
        category = Category(**category_data)
        session.add(category)
        session.commit()
        session.refresh(category)
        return category

def get_all_categories(session: Session):
    category = select(Category).order_by(Category.id)
    return session.scalars(category).all()

def get_category_by_id(id: int, session):
    category = select(Category).where(Category.id == id)
    return session.scalar(category)

def delete_by_id(id: int, session: Session):
    category = get_category_by_id(id, session)
    if category is None:
        return None
    session.delete(category)
    session.commit()
    return id

def update_by_id(session: Session, category: Category, updated_data: dict):
    try:
        for field, value in updated_data.items():
            setattr(category,field,value)

        session.commit()
        session.refresh(category)
        return category
    except Exception:
        session.rollback()
        raise

def get_category_by_name(cateogory_name: str, session: Session):
    category = select(Category).where(Category.name == cateogory_name)
    return session.scalar(category)

def get_cateogory_by_id(category_id: int, session: Session):
    return session.get(Category, category_id)

