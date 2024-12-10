from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from config import Base
from datetime import date
from enum import Enum as PyEnum


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)


class PeriodoEnum(PyEnum):
    M = "M"  # Primeiro valor
    V = "V"  # Segundo valor
    N = "N"  # Terceiro valor


class Alunos(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    idade = Column(Integer, index=True)  # Correção: use Integer ao invés de int
    periodo = Column(Enum(PeriodoEnum), index=True)
