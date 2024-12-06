from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config import Base


# Modelo de exemplo para a tabela "Item"
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
