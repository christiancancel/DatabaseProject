from flask import Flask, jsonify, request, render_template
from flask_login import login_manager
from handler.people import peopleHandler
from handler.product import producthandler
from handler.request import RequestHandler

app = Flask(__name__)
lm = login_manager.LoginManager()
app.secret_key = 'medalla base'
lm.init_app(app)
lm.login_view = 'SignIn'

@app.route('/')
def greeting():
    #return 'Hello, Welcome to: Ayuda pal Jibaro! A backend system for disaster site resources locator'
    return  render_template('home.html')


# OK
'''GET ALL PRODUCTS'''

@app.route('/SignIn', methods=['GET', 'POST'])
def SignIn():
    if request.method == 'POST':
        print(request.form["Password"])
        return peopleHandler().signin(request.form["Username"], request.form["Password"])
    else:
        return render_template('signin.html')

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
