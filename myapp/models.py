#!/usr/bin/env python
#coding=utf8

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from myapp.configs import settings

db_engine = create_engine(settings.DB_URI, encoding='utf8', 
                          convert_unicode=True, echo=settings.DB_ECHO)       

Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, 
                                      bind=db_engine))

Base = declarative_base()