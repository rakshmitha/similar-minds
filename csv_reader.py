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
#import pandas as pd
import csv

#Local import
import db_service as dbs


def read_csv_and_store_in_db():

    with open('developer_score_5_criteria.csv','r') as fin: 
        dr = csv.DictReader(fin) 
        to_db = [(i['name'], i['LinkedIn content'], i['Public coding activities'], i['Github Analysis'], i['Stackoverflow Analysis'], i['Tech Keys involved']) for i in dr]
        for person in to_db:
            dbs.insert_into_db(person[0], person[1], person[2], person[3], person[4], person[5])
  

def start():
    read_csv_and_store_in_db()

if __name__ == '__main__':
    start()        