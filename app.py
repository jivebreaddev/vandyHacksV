from flask import Flask, render_template
import DAL.DBOps as db

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    return render_template('home.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')


if __name__ == '__main__':
    app.run(debug = True)


