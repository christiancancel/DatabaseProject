from flask import Flask, jsonify, request
from handler.people import peopleHandler
from handler.product import producthandler

app = Flask(__name__)


@app.route('/')
def greeting():
    return 'Give Us An A Dammit'


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
    return peopleHandler().getSupplierByProduct(p_id)


@app.route('/products/supplier')
def get_products_by_supplier():
    if not request.args:
        return peopleHandler().get_all_products_by_supplier()  # gets all products by name, grouped by supplier id
    else:
        return peopleHandler().getProductsBySupplier(request.args)  # filters products by sup id, first name, full name


@app.route('/products/city')
def get_products_by_city():
    if not request.args:
        return peopleHandler().get_all_products_by_city(request.args)  # gets all products by p_name, grouped by city
    else:
        return peopleHandler().get_all_products_by_city(request.args)  # filters products by city


@app.route('/products/zipcode')
def get_products_by_zipcode():
    if not request.args:
        return peopleHandler().get_all_products_by_zipcode(request.args)  # gets all products by p_name, grouped by city
    else:
        return peopleHandler().get_all_products_by_zipcode(request.args)  # filters products by city


@app.route('/products/country')
def get_products_by_country():
    if not request.args:
        return peopleHandler().get_all_products_by_country(request.args)  # gets all products by p_name, grouped by city
    else:
        return peopleHandler().get_all_products_by_country(request.args)  # filters products by city


@app.route('/transactions')
def get_all_orders():
    if not request.args:
        return peopleHandler().get_all_orders()  # gets all products by product name
    else:
        return peopleHandler().search_orders(request.args)  # filter products by product attributes


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



@app.route('/admins', methods=['GET', 'POST'])
def getAllAdmin():
    if not request.args:
        return peopleHandler().getAllAdmin()
    else:
        return peopleHandler().searchADMINByRequests(request.args)

if __name__ == '__main__':
    app.run()
