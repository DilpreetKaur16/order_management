from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field

class ProductCreate(BaseModel):
    name: str = Field(min_length=3, max_length= 100)
    sku: str = Field(min_length=3, max_length= 50)
    description:str | None = None
    price: Decimal = Field(gt=0, max_digits=10, decimal_places= 2)
    stock: int = Field(ge=0, default=0)
    category_id: int

class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes= True)

    id: int
    name: str
    sku: str
    description: str | None
    price: Decimal
    stock: int
    category_id: int | None

class ProductUpdate(BaseModel):
    #PUT- all fields are required
    name: str = Field(min_length=3, max_length=100)
    sku: str = Field(min_length=3, max_length= 50)
    description:str | None = None
    price: Decimal = Field(ge=0, max_digits=10, decimal_places= 2)
    stock: int = Field(ge=0)
    category_id: int

class ProductPatch(BaseModel):
   # PATCH: every field is optional
    name: str | None = Field(default=None, min_length=3, max_length=100)
    sku: str | None = Field(default=None, min_length=3, max_length=50)
    description: str | None = None
    price: Decimal | None = Field(
        default=None, gt=0, max_digits=10, decimal_places=2
    )
    stock: int | None = Field(default=None, ge=0)
    category_id: int | None
 


