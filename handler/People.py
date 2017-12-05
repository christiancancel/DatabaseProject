from flask import jsonify


class PeopleHandler:
    def build_PIN_dict(self, row):
        result = {}
        result['PIN_id'] = row[0]
        result['PIN_Name'] = row[1]
        result['PIN_Location'] = row[2]
        result['PIN_GPSC'] = row[3]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['S_id'] = row[0]
        result['S_Name'] = row[1]
        result['S_Location'] = row[2]
        result['S_GPSC'] = row[3]
        return result

    def build_ADMIN_dict(self, row):
        result = {}
        result['A_id'] = row[0]
        result['A_Name'] = row[1]
        result['A_Location'] = row[2]
        result['A_GPSC'] = row[3]
        return result

    def RegisterAsAdmin(self):
        return jsonify(Error="'RegisterAsAdmin' FAILED. Cannot connect to Database"), 404

    def RegisterAsPersonInNeed(self):
        return jsonify(Error="'RegisterAsPersonInNeed' FAILED. Cannot connect to Database"), 404

        def registerAsSupplier(self):
            return jsonify(Error="'registerAsSupplier' FAILED. Cannot connect to Database"), 404


