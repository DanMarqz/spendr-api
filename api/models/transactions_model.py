from pydantic import BaseModel, Field
from datetime import datetime

class TransactionModel(BaseModel):
    description: str
    price: float
    date: str
    category: str
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)


    def is_valid(self):
        if self.description is None:
            raise ValueError("No description is provided")
        if self.price is None:
            raise ValueError("No price is provided")
        if self.date is None:
            raise ValueError("No date is provided")
        if self.category is None:
            raise ValueError("No category is provided")
        return True
