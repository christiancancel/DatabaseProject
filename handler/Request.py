from flask import jsonify


class RequestHandler:
    def build_REQUEST_dict(self, row):
        result = {}
        result['R_id'] = row[0]
        result['ST_id'] = row[1]
        result['PIN_id'] = row[2]
        return result

    def build_stock_dict(self, row):
        result = {}
        result['ST_id'] = row[0]
        result['S_id'] = row[1]
        result['R_id'] = row[2]
        result['ST_Res'] = row[3]
        result['ST_Qty'] = row[4]
        return result

    def build_PIN_dict(self, row):
        result = {}
        result['PIN_id'] = row[0]
        result['PIN_Name'] = row[1]
        result['PIN_Location'] = row[2]
        result['PIN_GPSC'] = row[3]
        return result

    def getRequestkByResourceNameID(self, R_id):
        return jsonify(Error="'getRequestkByResourceNameID'. FAILED Cannot connect to Database"), 404

        def getAllRequests(self):
            return jsonify(Error="'getAllRequests'. FAILED Cannot connect to Database"), 404





