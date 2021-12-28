""" 
-------------------------------------------------------------------------
- Cod BY : SidraELEzz
- Github : https://github.com/SidraELEzz
- Telegram: https://t.me/SidraTools
- Telegram: https://t.me/tt_rq
-------------------------------------------------------------------------
     
""" 
try:
	import os,sys,json,requests,flask
	from flask import *
	from requests.auth import HTTPBasicAuth
except ImportError as error :
    os.system('pip install requests')
    os.system('pip install Flask==2.0.2')
	





	
app = Flask(__name__)

@app.route('/')
def massage_welcome():
    return "<h1>Welcome to the API for checking the SK key</h1>\n<h1>----------------------------------------</h1>\n<h1>- Cod BY : SidraELEzz</h1>\n<h1>- Github : https://github.com/SidraELEzz</h1>\n<h1>- Telegram: https://t.me/SidraTools</h1>\n<h1>- Telegram: https://t.me/SidraTools</h1>\n<h1>- Telegram: https://t.me/tt_rq</h1>\n<h1>----------------------------------------</h1>"



@app.route('/API/SidraELEzz/Sk/', methods=['GET'])
def sk_check():
    key = str(request.args.get('sk'))
    if len(key) == 0:
        result = {"result": "Empty sk", "key": None, "checker " : "sk" , "Telegram": "@SidraTools"}
        return result, 404
    else:
        sk = str(key)
        y = sk[:12]
        x = sk[-6:]
        z = ('x' * 9)
        encsk = y + z + x
        
        
        r = requests.post('https://api.stripe.com/v1/tokens',
        data="card[number]=4766644568716428&card[exp_month]=08&card[exp_year]=2022&card[cvc]=001",
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        auth=HTTPBasicAuth(sk, ''))
        respo = r.json()
        if 'error' in str(respo):
            if "code" in respo['error']:
                code = respo['error']['code']
                res = code.replace('_', ' ')
                reason = res.title()
                result = {"result": str(reason), "key": str(encsk), "checker " : "sk" , "Telegram": "@SidraTools"}
                return json.dumps(result)
            else:
                result = {"result": "error sk", "key": None, "checker " : "sk" , "Telegram": "@SidraTools"}
                return json.dumps(result)
        else:
            result = {"result": "successful", "key": str(encsk), "checker " : "sk" , "Telegram": "@SidraTools"}
            return json.dumps(result)
        

    
    
if __name__ == '__main__':
    app.run()
