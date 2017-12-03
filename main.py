from flask import Flask, jsonify, request
from handler.Stock import StockHandler

app = Flask(__name__)


@app.route('/')
def greeting():
    return 'Hello, Welcome to: AyudapalJibaro! A backend systemfor disaster site resources locator'


@app.route('/AyudaPalJibaro/ShowAllResources')
def getAllStock():
    return StockHandler().getAllStock()


@app.route('/AyudaPalJibaro/ShowAllResources/SortBySupplier=<int:S_id>')
def getStockBySupplierID(S_id):
      return StockHandler().getStockBySupplierID(S_id)


@app.route('/AyudaPalJibaro/ShowAllResources/SortByResource=<int:R_id>')
def getStockByResourceID(R_id):
    return StockHandler().getStockByResourceID(R_id)


if __name__ == '__main__':
    app.run()
