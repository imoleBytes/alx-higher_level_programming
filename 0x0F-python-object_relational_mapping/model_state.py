#!/usr/bin/python3
"""
module contains the State class, Base: an instance of declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData


# mymetadata = MetaData()
Base = declarative_base()  # (metadata=mymetadata)


class State(Base):
    """A class with id and name map to table 'states'"""
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
