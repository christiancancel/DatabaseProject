from flask import jsonify
from dao.people import peopledao

class peopleHandler:
    def build_admin_dict(self, row):
        result = {}
        result['ad_id'] = row[0]
        result['ad_fname'] = row[1]
        result['ad_lname'] = row[2]
        result['a_id'] = row[3]
        result['adressid'] = row[4]
        result['ad_phone'] = row[5]
        return result

    def build_pin_dict(self, row):
        result = {}
        result['pin_id'] = row[0]
        result['pin_fname'] = row[1]
        result['pin_lname'] = row[2]
        result['a_id'] = row[3]
        result['adressid'] = row[4]
        result['pin_phone'] = row[5]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['ad_id'] = row[0]
        result['ad_fname'] = row[1]
        result['ad_lname'] = row[2]
        result['a_id'] = row[3]
        result['adressid'] = row[4]
        result['s_phone'] = row[5]
        return result

    def build_product_dict(self, row):
        result = {}
        result['p_id'] = row[0]
        result['ct_id'] = row[1]
        result['s_id'] = row[2]
        result['p_name'] = row[3]
        result['p_qty'] = row[4]
        result['p_unit'] = row[5]
        result['p_priceperunit'] = row[6]
        return result

    def build_orderinfo_dict(self, row):
        result = {}
        result['o_id'] = row[0]
        result['od_id'] = row[1]
        result['od_qty'] = row[2]
        result['od_pprice'] = row[3]
        result['s_id'] = row[4]
        result['ba_id'] = row[5]
        result['p_id'] = row[6]
        result['pin_id'] = row[7]
        result['c_id'] = row[8]
        result['o_date'] = row[9]
        return result

    '''return everyone registered as person in need'''

    def getAllPeopleInNeed(self):
        dao = peopledao()
        pin_list = dao.getAllPeopleInNeed()
        result_list = []
        for row in pin_list:
            result = self.build_pin_dict(row)
            result_list.append(result)
        return jsonify(PeopleInNeed=result_list)

    '''return everyone registered as supplier'''

    def getAllSuppliers(self):
        dao = peopledao()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    '''return everyone registered as administrator'''

    def getAllAdminstrators(self):
        dao = peopledao()
        suppliers_list = dao.getAllAdmin()
        result_list = []
        for row in suppliers_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
        return jsonify(Admins=result_list)

    '''Get All Orders'''

    def getAllOrders(self):
        dao = peopledao()
        orders_list = dao.getAllOrders()
        result_list = []
        for row in orders_list:
            result = self.build_orderinfo_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    '''encontrar productos por supplidor '''

    def getProductsBySupplier(self, args):
        s_id = args.get("s_id")
        s_fname = args.get("s_fname")
        s_lname = args.get("s_lname")
        dao = peopledao()
        product_list = []
        if (len(args) == 2) and s_fname and s_lname:
            product_list = dao.getProductsBySupplierFullName(s_fname, s_lname)
        elif (len(args) == 1) and s_fname:
            product_list = dao.getProductsBySupplierName(s_fname)
        elif (len(args) == 1) and s_id:
            product_list = dao.getProductsBySupplierId()
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in product_list:
            result = self.build_product_dict(row)
            result_list.append(result)
        return jsonify(ProductsBySupplier=result_list)

    '''encontrar supplidor por producto'''

    def getSupplierByProduct(self, args):
        p_id = args.get("p_id")
        p_name = args.get("p_name")
        dao = peopledao()
        product_list = []
        if (len(args) == 1) and p_id:
            product_list = dao.getSupplierByProductId(p_id)
        elif (len(args) == 1) and p_name:
            product_list = dao.getSupplierByProductName(p_name)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in product_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(SupplierByProduct=result_list)

    '''Encontrar las ordenes de una persona'''

    def getOrdersByPersonInNeed(self, args):
        pin_id = args.get("pin_id")
        pin_fname = args.get("pin_fname")
        pin_lname = args.get("pin_lname")
        dao = peopledao()
        order_list = []
        if (len(args) == 1) and pin_id:
            order_list = dao.getOrdersByPersonInNeedById(pin_id)
        elif (len(args) == 1) and pin_fname:
            order_list = dao.getOrdersByPersonInNeedByFirstName(pin_fname)
        elif (len(args) == 2) and pin_fname and pin_lname:
            order_list = dao.getOrdersByPersonInNeedByFullName(pin_fname, pin_lname)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in order_list:
            result = self.build_orderinfo_dict(row)
            result_list.append(result)
        return jsonify(OrdersByPersonInNeed=result_list)

    '''Encontrar las ordenes de una supplier'''

    def getOrdersBySupplier(self, args):
        s_id = args.get("s_id")
        s_fname = args.get("s_fname")
        s_lname = args.get("s_lname")
        dao = peopledao()
        order_list = []
        if (len(args) == 1) and s_id:
            order_list = dao.getOrdersBySupplierById(s_id)
        elif (len(args) == 1) and s_fname:
            order_list = dao.getOrdersBySuppplierByFirstName(s_fname)
        elif (len(args) == 2) and s_fname and s_lname:
            order_list = dao.getProductsBySupplierFullName(s_fname, s_lname)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in order_list:
            result = self.build_orderinfo_dict(row)
            result_list.append(result)
        return jsonify(OrdersBySupplier=result_list)


