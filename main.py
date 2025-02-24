from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Home Page for puppy</h1>'

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name[-1]=='y':
        return "<h1>{}iful</h1>".format(name)
    else:
        return "<h1>{}y</h1>".format(name)


if __name__=='__main__':
    app.run(debug=True)