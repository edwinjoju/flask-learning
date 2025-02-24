from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hey guys...</h1>'

@app.route('/home')
def home():
    return 'you are home'

@app.route('/user/<username>')
def username(username):
    return '<h1>You are {}</h1>'.format(username)

if __name__ == '__main__':
    app.run()

