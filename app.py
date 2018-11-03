from flask import Flask, render_template,request
import DAL.DBOps as db
import Models.Account as M
app = Flask(__name__)

@app.route('/')
def home():

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

@app.route('/register', methods=['POST','GET'])
def register():
    form1 = request.form
    print(form1)

    if request.method == 'POST':
        acc = M.Account(form1['Fname'], form1['Lname'], form1['email'], form1['phone'], form1['username'],
                        form1['password'], form1['oAuth'])
        db.insertAccount(acc)
        return render_template('signin.html', form=form1)


    return render_template('register.html', form=form1)



if __name__ == '__main__':
    app.run(debug = True)


