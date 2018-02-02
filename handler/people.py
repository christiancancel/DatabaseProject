from flask import jsonify
from dao.people import peopledao
from dao.product import ProductDAO


class peopleHandler:
    def build_admin_dict(self, row):
        result = {}
        result['ad_id'] = row[0]
        result['ad_fname'] = row[1]
        result['ad_lname'] = row[2]
        result['ada_id'] = row[3]
        result['adaddress_id'] = row[4]
        result['ad_phone'] = row[5]
        result['addressline1'] = row[6]
        result['city'] = row[7]
        result['zipcode'] = row[8]
        result['country'] = row[9]
        result['district'] = row[10]
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

    def build_new_product(self, row):
        result = {}
        result['p_id'] = row[0]
        result['ct_id'] = row[1]
        result['s_id'] = row[2]
        result['p_name'] = row[3]
        result['p_qty'] = row[4]
        result['p_unit'] = row[5]
        result['p_priceperunit'] = row[6]
        result['s_fname'] = row[7]
        result['s_lname'] = row[8]
        result['ct_type'] = row[9]
        return result

    def build_new_product_declared(self, row, input):
        result = {}
        result['p_id'] = row[0]
        result['ct_id'] = row[1]
        result['s_id'] = row[2]
        result['p_name'] = row[3]
        result['p_qty'] = row[4]
        result['p_unit'] = row[5]
        result['p_priceperunit'] = row[6]
        result['s_fname'] = row[7]
        result['s_lname'] = row[8]
        result['ct_type'] = row[9]
        result[input] = row[10]
        return result


    def build_order_dict(self, row):
        result = {}
        result['o_id'] = row[0]
        result['od_id'] = row[1]
        result['od_qty'] = row[2]
        result['od_pprice'] = row[3]
        result['s_id'] = row[4]
        result['ba_id'] = row[5]
        result['p_id'] = row[6]
        result['p_name'] = row[7]
        result['pin_id'] = row[8]
        result['pin_fname'] = row[9]
        result['pin_lname'] = row[10]
        result['c_id'] = row[11]
        result['o_date'] = row[12]
        result['s_fname'] = row[13]
        result['s_lname'] = row[14]
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

    def getAllAdmin(self):
        dao = peopledao()
        admin_list = dao.getAllAdmin()
        result_list = []
        for row in admin_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
        return jsonify(Admins=result_list)

    '''Get All Orders'''

    def getAllOrders(self):
        dao = peopledao()
        orders_list = dao.getAllOrders()
        result_list = []
        for row in orders_list:
            result = self.build_order_dict(row)
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
            product_list = dao.getProductsBySupplierId(s_id)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in product_list:
            result = self.build_new_product(row)
            result_list.append(result)
        return jsonify(ProductsBySupplier=result_list)

    '''encontrar supplidor por producto'''

    def getSupplierByProduct(self, p_id):
        dao = peopledao()
        if not ProductDAO().getProductById(p_id):
            return jsonify(Error="Product Not Found"), 404
        product_list = dao.getSupplierByProductId(p_id)
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
            result = self.build_order_dict(row)
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
            order_list = dao.getOrdersBySupplierByFullName(s_fname, s_lname)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in order_list:
            print(row)
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(OrdersBySupplier=result_list)

    def get_all_products_by_supplier(self):
        dao = peopledao()
        product_list = dao.get_all_products_by_supplier()
        result_list = []
        for row in product_list:
            result = self.build_new_product(row)
            result_list.append(result)
        return jsonify(Product=result_list)

    def get_all_products_by_city(self, args):
        dao = peopledao()
        city = args.get('city')
        if not city:
            product_list = dao.get_all_products_by_city()
        else:
            product_list = dao.get_all_products_by_city_declared(city)
        result_list = []
        for row in product_list:
            result = self.build_new_product_declared(row, 'city')
            result_list.append(result)
        return jsonify(ProductByCity=result_list)

    def get_all_products_by_zipcode(self, args):
        dao = peopledao()
        zipcode= args.get('zipcode')
        if not zipcode:
            product_list = dao.get_all_products_by_zipcode()
        else:
            product_list = dao.get_all_products_by_zipcode_declared(zipcode)
        result_list = []
        for row in product_list:
            result = self.build_new_product_declared(row, 'zipcode')
            result_list.append(result)
        return jsonify(ProductByZipcode=result_list)

    def get_all_products_by_country(self, args):
        dao = peopledao()
        country = args.get('country')
        if not country:
            product_list = dao.get_all_products_by_country()
        else:
            product_list = dao.get_all_products_by_country_declared(country)
        result_list = []
        for row in product_list:
            result = self.build_new_product_declared(row, 'country')
            result_list.append(result)
        return jsonify(ProductByCountry=result_list)

    def getPINByFirstName(self, args):
        pin_fname = args.get("pin_fname")
        dao = peopledao()
        pin_list = []
        if ((len(args)) == 1) and pin_fname:
            pin_list = dao.getPINByFirstName(pin_fname)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in pin_list:
            result = self.build_pin_dict(row)
            result_list.append(result)
        return jsonify(SupplierByProduct=result_list)

    def get_all_orders(self):
        dao = peopledao()
        orders_list = dao.getAllOrders()
        result_list = []
        for row in orders_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    def search_orders(self, args):
        dao = peopledao()
        o_id = args.get("o_id")
        c_id = args.get("c_id")
        o_date = args.get("o_date")
        od_qty = args.get("od_qty")
        od_id = args.get("od_id")
        od_pprice = args.get("od_pprice")
        s_id = args.get("s_id")
        ba_id = args.get("ba_id")
        p_id = args.get("p_id")
        pin_id = args.get("pin_id")
        orders_list = []
        if len(args) == 1 and o_id:
            orders_list = dao.filter_orders(o_id, 1)
        elif len(args) == 1 and o_date:
            orders_list = dao.filter_orders(o_date, 2)
        elif len(args) == 1 and c_id:
            orders_list = dao.filter_orders(c_id, 3)
        elif len(args) == 1 and od_qty:
            orders_list = dao.filter_orders(od_qty, 4)
        elif len(args) == 1 and od_id:
            orders_list = dao.filter_orders(od_id, 5)
        elif len(args) == 1 and od_pprice:
            orders_list = dao.filter_orders(od_pprice, 6)
        elif len(args) == 1 and s_id:
            orders_list = dao.filter_orders(s_id, 7)
        elif len(args) == 1 and ba_id:
            orders_list = dao.filter_orders(ba_id, 8)
        elif len(args) == 1 and p_id:
            orders_list = dao.filter_orders(p_id, 9)
        elif len(args) == 1 and pin_id:
            orders_list = dao.filter_orders(pin_id, 10)
        else:
            return jsonify(Error="Malformed query string")
        result_list = []
        for row in orders_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)