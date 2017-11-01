from flask import Flask,session
from datetime import datetime
app = Flask(__name__)
app.secret_key='SET_ME_BEFORE_USE_SESSION'
@app.route('/write_session')
def write_session():
    session['key_time']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return session['key_time']

@app.route('/read_session')
def read_session():
    return session.get('key_time')

if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=8001,debug=False)
    app.run()