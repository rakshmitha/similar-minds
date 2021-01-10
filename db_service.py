#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 

Course work: 

@author:

Source:
    https://stackoverflow.com/questions/2942889/reading-parsing-excel-xls-files-with-python

    GSheet:
    https://docs.google.com/spreadsheets/d/1YX4vLv3xj6tQC6Ou-Sx8yC1k5jT7VN4ulTWF1BldL9Y/edit#gid=39068816
'''


# Import necessary modules
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

import pandas as pd
# from sqlalchemy import update
from sqlalchemy import and_, or_

engine = create_engine('sqlite:///Dev_Recommender.db', echo = True, connect_args={'check_same_thread': False})
Base = declarative_base() 

class Dev_Recommender(Base):
   __tablename__ = 'DEV_RECOMMENDER'

   id = Column(Integer, primary_key=True)
   Name = Column(String, unique=True, nullable=False)
   LinkedIn_Content = Column(Integer, nullable=False)
   Public_Coding_Activities = Column(Integer, nullable=False)
   Github_Analysis = Column(Integer, nullable=False)
   Stackoverflow_Analysis = Column(Integer, nullable=False)
   Tech_Keys_Involved = Column(Integer, nullable=False)

Session = sessionmaker(bind = engine)
session = Session()

def insert_into_db(Name, LinkedIn_Content, Public_Coding_Activities, Github_Analysis, Stackoverflow_Analysis, Tech_Keys_Involved):

    p1 = Dev_Recommender(Name = Name, LinkedIn_Content = LinkedIn_Content, Public_Coding_Activities = Public_Coding_Activities, Github_Analysis = Github_Analysis, Stackoverflow_Analysis = Stackoverflow_Analysis, Tech_Keys_Involved = Tech_Keys_Involved)

    session.add(p1)
    session.commit()

def get_all_linkedin_url_from_db():
    url = []
    devs = session.query(Dev_Recommender).all()
    for dev in devs:
        url.append(dev.Name)
    return url

def get_all_data_from_db():
    data = []
    rows = session.query(Dev_Recommender).all()
    for row in rows:
        data.append(row)
    return data

def pd_get_data():
    table_df = pd.read_sql_table(
    "DEV_RECOMMENDER",
    con=engine
    )
    return table_df