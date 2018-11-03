from flask import Flask, render_template,request
import DAL.DBOps as db
import Models.Account as M
app = Flask(__name__)

@app.route('/')
def home():
    b = db.retrieveAccount('la96bikal')
    return render_template('home.html')

@app.route('/signin', methods = ['POST', 'GET'])
def signin():
    Form = request.form
    if request.method == 'POST':
        auth = db.Authenticate(Form['username'], Form['password'])
        print(auth)
        if auth:
            return render_template('profile.html')
        else:
            return render_template('signin.html', Message="Invalid Username or Password. Try Again")

    return render_template('signin.html', form=Form)



if __name__ == '__main__':
    app.run(debug = True)


