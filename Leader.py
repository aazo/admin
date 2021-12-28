from flask import Flask
from flask import request
import requests
import json
@app.route('/')
def owner():
    oii='Hi'
    return oii
@app.route('/api/tele')
def tele():
    user= request.args.get('user')
    r=requests.get(f'https://t.me/{user}')
    if 'https://telegram.org/img/t_logo.png' in r.text:
        rq='Not Taken'
    else:
        rq='Taken'
    data1={'data':rq,'status':'loaded','owner':'noelx'}
    data_x=json.dumps(data1)
    try:
        return data_x
    except:pass
@app.route('/api/ip')
def ip():
    ips=request.access_route[-1]
    data_ip={'ip':ips}
    ij=json.dumps(data_ip)
    return ij
app.run(host='0.0.0.0',port='8080')
