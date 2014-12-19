#!/usr/bin/env python
#coding=utf8
from sqlalchemy import Column, Integer, String, DATETIME

from myapp.models import Base, Session, db_engine

class User(Base):
    """
    用户身份
    """
    __tablename__ = "user"
    __table_args__ = {"mysql_engine": "InnoDB", "mysql_charset": "utf8"}

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    age = Column(Integer, default=1)



if __name__ == '__main__':
    Base.metadata.create_all(bind=db_engine)
