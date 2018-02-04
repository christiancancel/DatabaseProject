from flask import Flask, jsonify, request
from handler.people import PeopleHandler
from handler.product import producthandler
from handler.request import RequestHandler

app = Flask(__name__)


@app.route('/')
def greeting():
    return 'Hello'


#########PRODUCTS########
@app.route('/products', methods=['GET', 'POST'])
def get_all_products():
    if request.method == 'POST':
        return producthandler().insert_product(request.form)  # insert a product
    else:
        if not request.args:
            return producthandler().get_all_products()  # gets all products by product name
        else:
            return producthandler().search_products(request.args)  # filter products by product attributes


@app.route('/products/<int:p_id>', methods=['GET', 'PUT', 'DELETE'])
def get_specific_product(p_id):
    if request.method == 'GET':
        return producthandler().getProductById(p_id)
    elif request.method == 'PUT':
        return producthandler().update_product(p_id, request.form)
    elif request.method == 'DELETE':
        return producthandler().delete_product(p_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/products/<int:p_id>/suppliers')
def get_supplier_by_product_id(p_id):
    return PeopleHandler().getSupplierByProduct(p_id)


@app.route('/products/supplier')
def get_products_by_supplier():
    if not request.args:
        return PeopleHandler().get_all_products_by_supplier()  # gets all products by name, grouped by supplier id
    else:
        return PeopleHandler().getProductsBySupplier(request.args)  # filters products by sup id, first name, full name


@app.route('/products/city')
def get_products_by_city():
    if not request.args:
        return PeopleHandler().get_all_products_by_city(request.args)  # gets all products by p_name, grouped by city
    else:
        return PeopleHandler().get_all_products_by_city(request.args)  # filters products by city


@app.route('/products/zipcode')
def get_products_by_zipcode():
    if not request.args:
        return PeopleHandler().get_all_products_by_zipcode(request.args)  # gets all products by p_name, grouped by city
    else:
        return PeopleHandler().get_all_products_by_zipcode(request.args)  # filters products by city


@app.route('/products/country')
def get_products_by_country():
    if not request.args:
        return PeopleHandler().get_all_products_by_country(request.args)  # gets all products by p_name, grouped by city
    else:
        return PeopleHandler().get_all_products_by_country(request.args)  # filters products by city


@app.route('/products/district')
def get_products_by_district():
    if not request.args:
        return PeopleHandler().get_all_products_by_district(request.args)  # gets all products by p_name, grouped by city
    else:
        return PeopleHandler().get_all_products_by_district(request.args)  # filters products by city


############Transactions##################
@app.route('/transactions')
def get_all_orders():
    if not request.args:
        return PeopleHandler().get_all_orders()  # gets all products by product name
    else:
        return PeopleHandler().search_orders(request.args)  # filter products by product attributes


@app.route('/products/buy', methods=['GET', 'POST'])
def buy_product():
    if request.method == 'POST':
        return producthandler().buy_product(request.form)  # insert a product
    else:
        return producthandler().getPurchasableProduct()


@app.route('/products/reserve', methods=['GET', 'POST'])
def reserve_product():
    if request.method == 'POST':
        return producthandler().buy_product(request.form)  # insert a product
    else:
        return producthandler().getFreeProduct()


# # #  A D M I N I S T R A T O R  # # #

@app.route('/admins', methods=['GET', 'POST'])
def get_all_admin():
    if request.method == 'POST':
        return PeopleHandler().insert_admin(request.form)
    else:
        if not request.args:
            return PeopleHandler().getAllAdmin()
        else:
            return PeopleHandler().searchADMINByRequests(request.args)


########################## U S E R S ######################
@app.route('/users')
def get_all_users():
    return PeopleHandler().getAllUsers()


# # #  P E O P L E  I N  N E E D  # # #

@app.route('/pin', methods=['GET', 'POST'])
def get_all_pin():
    if request.method == 'POST':
        return PeopleHandler().insert_pin(request.form)
    else:
        if not request.args:
            return PeopleHandler().getAllpin()
        else:
            return PeopleHandler().searchPINByRequests(request.args)


@app.route('/pin/<int:pin_id>', methods=['GET', 'PUT'])
def get_specific_pin(pin_id):
    if request.method == 'GET':
        return PeopleHandler().get_specific_pin(pin_id)
    elif request.method == 'PUT':
        return PeopleHandler().update_pin(pin_id, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/pin/FirstName')
def get_pin_by_first_name():
    if not request.args:
        return PeopleHandler().getAllPeopleInNeed()
    else:
        return PeopleHandler().getPINByFirstName(request.args)


# # #  S U P P L I E R  # # #

@app.route('/suppliers', methods=['GET', 'POST'])
def getAllSUP():
    if request.method == 'POST':
        return PeopleHandler().insert_sup(request.form)
    else:
        if not request.args:
            return PeopleHandler().getAllsup()
        else:
            return PeopleHandler().searchSUPByRequests(request.args)


# # #  R E Q U E S T S # # #

@app.route('/request', methods=['GET', 'POST'])
def get_all_request():
    if request.method == 'POST':
        return RequestHandler().insert_request(request.form)
    else:
        if not request.args:
            return RequestHandler().getAllRequest()
        else:
            return RequestHandler().searchProductByRequests(request.args)


@app.route('/request/change/<int:r_id>', methods=['PUT', 'DELETE'])
def request_change(r_id):
    if request.method == 'PUT':
        return RequestHandler().updateRequest(r_id, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/supplier/bankinfo', methods=['GET', 'PUT', 'POST'])
def get_all_bank_info():
    if request.method == 'GET':
        return PeopleHandler().get_all_bank_info()
    elif request.method == 'POST':
        return PeopleHandler().insert_bankinfo(request.form)


@app.route('/supplier/bankinfo/<int:s_id>', methods=['GET', 'PUT', 'POST'])
def view_bankinfo_by_sid(s_id):
    if request.method == 'GET':
        return PeopleHandler().get_bankinfo_by_SID(s_id)
    elif request.method == 'PUT':
        return PeopleHandler().update_bankinfo(s_id, request.form)


@app.route('/pin/creditcard/<int:pin_id>', methods=['GET', 'PUT', 'POST'])
def view_creditcard_by_pin(pin_id):
    if request.method == 'GET':
        return PeopleHandler().view_creditcard_by_PIN(pin_id)
    elif request.method == 'PUT':
        return PeopleHandler().update_creditcard(pin_id, request.form)
    elif request.method == 'POST':
        return PeopleHandler().insert_creditcard(request.form)


@app.route('/accounts')
def get_account_by_username():
    return PeopleHandler().get_all_accounts()


@app.route('/account/<int:a_id>')
def search_account_by_username(a_id):
    return PeopleHandler().search_account_by_a_id(a_id)


if __name__ == '__main__':
    app.run()
