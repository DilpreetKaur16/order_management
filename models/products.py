from sqlalchemy import Column, Integer, String, Text, Numeric, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Product(Base):
    __tablename__ = "products"

    __table_args__ = (
        CheckConstraint("price > 0", name="check_product_price"),
        CheckConstraint("stock >= 0", name="check_product_stock"),
    )
#Pydantic validates incoming API requests, but database constraints protect your data even if records are inserted through another application or directly through SQL.
    id = Column(Integer, primary_key = True, index=True)
    name = Column(String(100), nullable=False)
    sku = Column(String(50), nullable= False, unique = True, index=True)
    description = Column(Text, nullable=True)
    price = Column(Numeric(10,2), nullable = False)
    stock = Column(Integer, nullable= False, default= 0)

    category_id= Column(Integer, ForeignKey("categories.id"), nullable= True)

    category = relationship("Category", back_populates="products")
