from flask import Flask, request, render_template, flash, redirect, url_for
from flask_login import login_manager,current_user, login_user, logout_user, login_fresh
from handler.people import peopleHandler
from handler.product import producthandler
from handler.request import RequestHandler
from Forms.SigninForm import LoginForm
from Forms.SignupForm import SignupForm
from Forms.user import User

app = Flask(__name__)
lm = login_manager.LoginManager()
app.secret_key = 'medalla base'
lm.init_app(app)
lm.login_view = 'SignIn'


@lm.user_loader
def load_user(id):
    return User().get_user(id)

@app.route('/')
def home():
    if current_user.is_anonymous:
        return  render_template('home.html')
    else:
        return redirect(url_for('userhome'))

@app.route('/UserHome')
def userhome():
    return render_template('userhome.html', account=current_user.user_type)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    username = form.username.data
    if form.validate_on_submit():
        password=peopleHandler().login(username)
        if password is None or not password[0]==form.password.data:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        user=User()
        user.set_user(username)
        login_user(user, remember=False)
        return render_template('userhome.html', title='logged in')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/SignUp', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        fname = form.fname.data
        lname = form.lname.data
        phone = form.phone.data
        address = form.address.data
        city = form.city.data
        country = form.country.data
        district = form.district.data
        zipcode = form.zipcode.data
        user_type = form.user_type.data
        signedup = peopleHandler().signup(username, password, fname, lname, phone, address, city, country,
                                          district, zipcode, user_type)
        if not signedup:
            flash('Signed Up Failed')
            return redirect(url_for('signup'))
        user=User()
        user.set_user(username)
        login_user(user, remember=False)
        return render_template('base.html', title='signed up')
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/products/add', methods=['GET', 'POST'])
def add_product():
    return True


@app.route('/products/announce', methods=['GET', 'POST'])
def announce_product():
    return True


@app.route('/products/ask', methods=['GET', 'POST'])
def ask_product():
    return True


@app.route('/products/buy', methods=['GET', 'POST'])
def buy_product():
    return True


@app.route('/products/viewTransactions', methods=['GET', 'POST'])
def view_transactions():
    return True


@app.route('/products/addCreditCard', methods=['GET', 'POST'])
def add_creditcard():
    return True


@app.route('/products/addBankInfo', methods=['GET', 'POST'])
def add_bank_info():
    return True


@app.route('/products/updateProduct', methods=['GET', 'POST'])
def update_product():
    return True


@app.route('/products/updateCreditCard', methods=['GET', 'POST'])
def update_creditcard():
    return True


# OK
'''GET ALL PRODUCTS'''

@app.route('/AyudaPalJibaro/products')
def getAllProducts():
    return producthandler().getAllProducts()


# OK
'''GET PRODUCT BY ID'''
6

@app.route('/AyudaPalJibaro/products/<int:p_id>')
def getProductById(p_id):
    return producthandler().getProductById(p_id)


# OK
'''GET IF AVAILABLE'''


@app.route('/AyudaPalJibaro/products/availability/<int:p_id>')
def getAvailabilityOfProduct(p_id):
    return producthandler().getAvailabilityOfProduct(p_id)


# OK
'''BROWSE RESOURCES REQUESTED'''


@app.route('/AyudaPalJibaro/products/requested')
def browseResourcesRequested():
    return RequestHandler().browseResourcesRequested()


# OK
'''SEARCH AVAILABLE PRODUCTS BY ATRIBUTE'''


@app.route('/AyudaPalJibaro/products/available')
def browseResourcesAvailable():
        return producthandler().browseResourcesAvailable()

'''CHECK PRODUCTS IN REQUESTS'''


@app.route('/AyudaPalJibaro/request')
def getAllRequest():
    if not request.args:
        return RequestHandler().getAllRequest()
    else:
        return RequestHandler().searchProductByRequests(request.args)


# OK
'''FIND PRODUCT BY DISTRICT'''


@app.route('/AyudaPalJibaro/products/district')
def findSpecificProduct():
    if not request.args:
        return producthandler().getAllProducts()
    else:
        return producthandler().findSpecificProduct(request.args)


'''GET ALL PEOPLE IN NEED'''


@app.route('/AyudaPalJibaro/ShowAllPeopleInNeed')
def getAllPIN():
    return peopleHandler().getAllPeopleInNeed()


'''GET ALL SUPPLIERS'''


@app.route('/AyudaPalJibaro/ShowAllSuppliers')
def getAllSuppliers():
    return peopleHandler().getAllSuppliers()


'''GET ALL ADMIN'''


@app.route('/AyudaPalJibaro/ShowAllAdmin')
def getAllAdmin():
    return peopleHandler().getAllAdminstrators()


'''GET PRODUCTS BY SUPPLIER'''


@app.route('/AyudaPalJibaro/GetProductsBySupplier')
def getProductsBySupplier():
    if not request.args:
        return producthandler().getAllProducts()
    else:
        return peopleHandler().getProductsBySupplier(request.args)


'''GET SUPPLIERS BY PRODUCT'''


@app.route('/AyudaPalJibaro/GetSupplierByProduct')
def getSupplierByProduct():
    if not request.args:
        return peopleHandler().getAllSuppliers()
    else:
        return peopleHandler().getSupplierByProduct(request.args)


'''GET ORDERS BY PERSON IN NEED'''


@app.route('/AyudaPalJibaro/GetOrdersByPersonInNeed')
def getOrdersByPerson():
    if not request.args:
        return peopleHandler().getAllOrders()
    else:
        return peopleHandler().getOrdersByPersonInNeed(request.args)


'''GET ORDERS BY SUPPLIER'''


@app.route('/AyudaPalJibaro/GetOrdersBySupplier')
def getOrdersBySupplier():
    if not request.args:
        return peopleHandler().getAllOrders()
    else:
        return peopleHandler().getOrdersBySupplier(request.args)

if __name__ == '__main__':
    app.run()
