from flask import Flask, jsonify, request
from handler.Stock import StockHandler
from handler.People import PeopleHandler
from handler.Statistic import StatisticHandler
from handler.Transaction import TransactionHandler
from handler.Request import RequestHandler

app = Flask(__name__)


@app.route('/')
def greeting():
    return 'Hello, Welcome to: Ayuda pal Jibaro! A backend system for disaster site resources locator'


@app.route('/AyudaPalJibaro/ShowAllResources')
def getAllStock():
    return StockHandler().getAllStock()


@app.route('/AyudaPalJibaro/ShowAllResources/SortBySupplier?Sid=<int:S_id>')
def getStockBySupplierID(S_id):
    return StockHandler().getStockBySupplierID(S_id)


@app.route('/AyudaPalJibaro/ShowAllResources/SortByResource?Rid=<int:R_id>')
def getStockByResourceID(pid):
    return StockHandler().getStockByResourceID(R_id)


@app.route('/AyudaPalJibaro/RegisterAsAdmin')
def RegisterAsAdmin():
    return PeopleHandler().RegisterAsAdmin()


@app.route('/AyudaPalJibaro/RegisterAsPersonInNeed')
def RegisterAsPersonInNeed():
    return PeopleHandler().RegisterAsPersonInNeed()


@app.route('/AyudaPalJibaro/DailyStatistics/ResourcesInNeed')
def DailyResourcesInNeed():
    return StatisticHandler().DailyResourcesInNeed()


@app.route('/AyudaPalJibaro/DailyStatistics/ResourcesAvailable')
def DailyResourcesAvailable():
    return StatisticHandler().DailyResourcesAvailable()


@app.route('/AyudaPalJibaro/DailyStatistics/Matching')
def DailyMatching():
    return StatisticHandler().DailyMatching()


@app.route('/AyudaPalJibaro/WeeklyStatistics/ResourcesInNeed')
def WeeklyResourcesInNeed():
    return StatisticHandler().WeeklyResourcesInNeed()


@app.route('/AyudaPalJibaro/WeeklyStatistics/ResourcesAvailable')
def WeeklyResourcesAvailable():
    return StatisticHandler().WeeklyResourcesAvailable()


@app.route('/AyudaPalJibaro/WeeklyStatistics/Matching')
def WeeklyMatching():
    return StatisticHandler().WeeklyMatching()


@app.route('/AyudaPalJibaro/Transaction/Purchase')
def Purchase():
    return TransactionHandler().Purchase()


@app.route('/AyudaPalJibaro/Transaction/Reserve')
def Reserve():
    return TransactionHandler().Reserve()


@app.route('/AyudaPalJibaro/ShowAllRequests/SortByResourceName?Rid=<int:R_id>')
def getRequestkByResourceNameID(R_id):
    return RequestHandler().getRequestkByResourceNameID(R_id)


@app.route('/AyudaPalJibaro/RegisterAsSupplier')
def registerAsSupplier():
    return PeopleHandler().RegisterAsSupplier()


@app.route('/AyudaPalJibaro/Resource=<R_name>')
def searchGivenResource(R_name):
    return StockHandler().searchResource(R_name)


@app.route('/AyudaPalJibaro/RequestedResources')
def getAllRequests():
    return RequestHandler().getAllRequests()


@app.route('/AyudaPalJibaro/RegionStatistics/ResourcesInNeed')
def regionResourcesInNeed():
    return StatisticHandler().regionResourcesInNeed()


@app.route('/AyudaPalJibaro/RegionStatistics/ResourcesAvailable')
def regionResourcesAvailable():
    return StatisticHandler().regionResourcesAvailable()


@app.route('/AyudaPalJibaro/RegionStatistics/Matching')
def regionMatching():
    return StatisticHandler().regionMatching()


if __name__ == '__main__':
    app.run()
