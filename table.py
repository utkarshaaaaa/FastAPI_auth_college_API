from .model import Base
from sqlalchemy import Column,Integer,String

class post(Base):
    __tablename__="posts"
    id=Column(Integer ,primary_key=True, nullable=False)
    name=Column(String,nullable=False)
    content=Column(String , nullable=False)