#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, url_for, request
import requests
import random
import os.path
import os
import random

# Local import
import euc_developers_5_criteria as s2
import db_service as dbs
#----------------------------------------------------------------------------#
# DB Config.
#----------------------------------------------------------------------------#


app = Flask(__name__)
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#



#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/', methods=['GET'])
def index():
     
    sample_list = s2.get_all_dev()
    
    result = {
        'sample_dev' : sample_list
    }

    return render_template('index.html', result = result)

@app.route('/insert',methods=['GET','POST'])
def insert():
    if request.method == 'POST':
        url = request.values.get('url')
        linkedin = request.values.get('linkedin')
        public_coding = request.values.get('public_coding')
        github_analysis = request.values.get('github_analysis')
        stack_overflow = request.values.get('stack_overflow')
        tech_keys = request.values.get('tech_keys')
        print(url)
        dbs.insert_into_db(url, linkedin, public_coding, github_analysis, stack_overflow, tech_keys)
        print("Successfully inserted")
    return render_template('insert.html')

@app.route('/result', methods=['POST'])
def result():

    dev_name = request.values.get('entry')

    print("DEV_NAME FROM INPUT :::: ", dev_name)

    rec_list = s2.find_similar_dev_auto(dev_name)

    sample_list = s2.get_all_dev()

    result = {
        'rec_list' : rec_list,
        'sample_dev' : sample_list
    }
    print("INSIDE REsult Route :::: ",rec_list[0])

    return render_template('index.html', result = result)


# @app.route('/api/db/insert',methods = ['GET', 'POST'])
# def api_db_insert():
#     if request.method == 'POST':
#         #id = request.form['id']
        
#         # name = request.form['name']
#         # dept = request.form['dept']
#         # item_list = None
#         # with sqlite3.connect("test.db") as conn:
#         #     id = get_last_record(conn)
#         #     print("LAST RECORD ID ::: ",id)
#         #     insert_obj = {
#         #         "id": id,
#         #         "name": name,
#         #         "dept": dept
#         #     }
#         # item_list = insert_into_db(conn,insert_obj)
#         # result = {
#         # 'users' : item_list
#         # }
        

#         return render_template("insert_into_db.html", result=result)
    
#     item_list = None
#     with sqlite3.connect("test.db") as conn:
#         item_list = select_all(conn)

#     result = {
#         'users' : item_list
#     }
    
#     return render_template("insert_into_db.html", result=result)


#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    #app.debug = True;1
    app.run('127.0.0.1', 4000, True)
