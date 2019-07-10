from flask import Flask, render_template
from main import *

app = Flask(__name__)
app.debug = True

@app.route('/')
def hi():
    return start()

@app.route('/chat',methods=['GET','POST'])
def chat():
    return main1()

if __name__ == '__main__':
    app.run()
