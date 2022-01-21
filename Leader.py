from flask import Flask
app=Flask(__name__)
@app.route('/',methods=['GET'])
def owner():
    return 'Hello ! '
    
if __name__==("__main__"):
    server.run(host="0.0.0.0", port="8080"
