from flask import jsonify


class StockHandler:
    def build_stock_dict(self, row):
        result = {}
        result['ST_id'] = row[0]
        result['S_id'] = row[1]
        result['R_id'] = row[2]
        result['ST_Res'] = row[3]
        result['ST_Qty'] = row[4]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['S_id'] = row[0]
        result['S_Name'] = row[1]
        result['S_Location'] = row[2]
        result['S_GPSC'] = row[3]
        return result

    def build_resources_dict(self, row):
        result = {}
        result['R_id'] = row[0]
        result['C_id'] = row[1]
        result['R_Name'] = row[2]
        return result

    def build_category_dict(self, row):
        result = {}
        result['C_id'] = row[0]
        result['C_Name'] = row[1]
        return result

    def getAllStock(self):
        return jsonify(Error="'getAllStock'. FAILED Cannot connect to Database"), 404

    def getStockBySupplierID(self, S_id):
        return jsonify(Error="'getStockBySupplierID'. FAILED Cannot connect to Database"), 404

    def getStockByResourceID(self, R_id):
        return jsonify(Error="'getStockByResourceID'. FAILED Cannot connect to Database"), 404

    def searchResource(self, R_name):
        return jsonify(Error="'searchResource'. FAILED Cannot connect to Database"), 404

    def getAllResources(self):
        return jsonify(Error="'getAllResources'. FAILED Cannot connect to Database"), 404


