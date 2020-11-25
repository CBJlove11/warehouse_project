import decimal
import numpy as np
from flask import Flask,render_template
import json
import pymysql
from datetime import timedelta
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/test', methods=['POST'])
def mytest():
    con =pymysql.connect(host='dp.yibai-it.com', user='wanjunsheng', passwd='df2932141LFDF',db='warehouse', port=20004, charset='utf8')
    cur = con.cursor()
    sql = ''
    cur.execute(sql)
    see = cur.fetchall()
if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
