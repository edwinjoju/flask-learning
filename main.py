from flask import Flask, render_template, request

app = Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    lower_letter = False
    upper_letter = False
    num_end = False

    username = request.args.get('username')

    lower_letter = any(i.islower() for i in username)
    upper_letter = any(i.isupper() for i in username)
    num_end = any(i.isnumeric() for i in username)

    return render_template('report.html',username=username,lower_letter=lower_letter,upper_letter=upper_letter,num_end=num_end)

if __name__ == '__main__':
    app.run(debug=True)