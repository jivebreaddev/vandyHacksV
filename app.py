from flask import Flask, render_template,request, jsonify
import DAL.DBOps as db
import Models.Models as M
app = Flask(__name__)

@app.route('/')
def home():

    return render_template('home.html')

@app.route('/signin', methods = ['POST', 'GET'])
def signin():
    Form = request.form
    events = ['Event 1', 'Event 2', 'Event 3', 'Event 4', 'Event 5']
    if request.method == 'POST':
        auth = db.Authenticate(Form['username'], Form['password'])
        if auth:
            return render_template('profile.html', acc = db.retrieveAccount(Form['username']), event = events)
        else:
            return render_template('signin.html', Message="Invalid Username or Password. Try Again")

    return render_template('signin.html', form=Form)

@app.route('/register', methods=['POST','GET'])
def register():
    form1 = request.form


    if request.method == 'POST':
        acc = M.Models(form1['Fname'], form1['Lname'], form1['email'], form1['phone'], form1['username'],
                       form1['password'], form1['oAuth'])
        db.insertAccount(acc)
        return render_template('signin.html', form=form1)


    return render_template('register.html', form=form1)

# @app.route('/profile', methods = ['POST'])
# def profile():
#     print('I GOT HERE')
#     form2 = request.form
#     custs = [M.Customer('Bikal', 'sdf@gmail.com'), M.Customer('Saurabh', 'bhandari@gmail.com')]
#     if request.method == 'POST':
#
#         return render_template('Customers.html', custos = custs)
#     return render_template('profile.html', form = form2)

@app.route('/customers')
def customers():
    userN = request.args.get('my_var', None)
    custs = [M.Customer('Bikal', 'sdf@gmail.com'), M.Customer('Saurabh', 'bhandari@gmail.com')]
    return render_template('Customers.html', cust = custs)

if __name__ == '__main__':
    app.run(debug = True)


