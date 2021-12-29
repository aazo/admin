from flask import Flask
app=Flask(__name__)
@app.route('/')
def owner():
    return 'Hello ! '

app.run()


