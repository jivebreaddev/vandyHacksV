from flask import Flask, render_template,request, jsonify
import DAL.DBOps as db
import Models.Models as M
import coAPI.evenbritedata as SP
import coAPI.fetchData as SB
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signin', methods = ['POST', 'GET'])
def signin():
    Form = request.form



    if request.method == 'POST':
        auth = db.Authenticate(Form['username'], Form['password'])
        if auth:
            acc = db.retrieveAccount('Spark')
            data = SP.dataloader(acc.oAuth)
            data.load_algo(5000, 1000)
            events = data.load_list()
            events = list(set(events))
            return render_template('profile.html', acc = acc, event = events)
        else:
            return render_template('signin.html', Message="Invalid Username or Password. Try Again")

    return render_template('signin.html', form=Form)

@app.route('/register', methods=['POST', 'GET'])
def register():
    form1 = request.form


    if request.method == 'POST':
        acc = M.Account(form1['Fname'], form1['Lname'], form1['email'], form1['phone'], form1['username'],
                       form1['password'], form1['oAuth'])
        db.insertAccount(acc)
        return render_template('signin.html', form=form1)


    return render_template('register.html', form=form1)

@app.route('/profile', methods = ['POST', 'GET'])
def profile():
    print("HEREE")
    form2 = request.form
    for key, value in form2:
        print(key, value)
    if request.method == 'POST':
        return render_template('pricing.html', price = form2['price'])
    return render_template('profile.html', form = form2)

@app.route('/customers')
def customers():
    # if request.method == 'POST':
    #     form2 = request.form
    #     jsonO = request.get_json()
    #     print(jsonO)
    #     return "trying things out"

    userN = request.args.get('my_var', None)
    print(userN)
    custs = SB.merchant_data()

    # [M.Customer('Bikal', 'sdf@gmail.com'), M.Customer('Saurabh', 'bhandari@gmail.com')]
    return render_template('Customers.html', cust = custs)


@app.route('/pricing')
def pricing():
    obj = request.get_json()
    print(obj)
    return "Hello"

if __name__ == '__main__':
    app.run(debug = True)


