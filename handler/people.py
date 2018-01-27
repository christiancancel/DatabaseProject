from flask import jsonify, render_template
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
        result['p_name'] = row[7]
        result['pin_id'] = row[8]
        result['pin_fname']= row[9]
        result['pin_lname']= row[10]
        result['c_id'] = row[11]
        result['o_date'] = row[12]
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
        s_id = args
        dao = peopledao()
        product_list = []
        if s_id:
            product_list = dao.getProductsBySupplierId(s_id)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in product_list:
            result = self.build_product_dict(row)
            result_list.append(result)
        return result_list

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
        pin_id = args
        dao = peopledao()
        order_list = []
        if pin_id:
            order_list = dao.getOrdersByPersonInNeedById(pin_id)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in order_list:
            result = self.build_orderinfo_dict(row)
            result_list.append(result)
        return result_list

    '''Encontrar las ordenes de una supplier'''

    def getOrdersBySupplier(self, args):
        s_id = args
        dao = peopledao()
        order_list = []
        if s_id:
            order_list = dao.getOrdersBySupplierById(s_id)
        else:
            return order_list
        result_list = []
        for row in order_list:
            print(row)
            result = self.build_orderinfo_dict(row)
            result_list.append(result)
        return result_list

    def signin(self, us, pw):
        username = us
        password = pw
        dao = peopledao()
        result = dao.checkusername(username)
        if result == None:
            return jsonify(error="Username does not exist.")
        if password== result[0]:
            return render_template('signinsuccess.html', title='Home', user=us)
        else:
            return jsonify(error="Incorrect Password.")

    def login(self, us):
        return peopledao().checkusername(us)

    def get_person_id(self, username):
        dao = peopledao()
        account=dao.get_account_id(username)
        print("account id ", account[0])
        if account==None:
            return False
        result=dao.get_person_id(account[0])
        print("person id ", result)
        if result==None:
            return False
        return result[0]

    def signup(self, username, password, fname, lname, phone, address, city, country,
                                          district, zipcode, user_type):
        dao = peopledao()
        ac_id = dao.create_account(username, password)
        address_id = dao.create_address(address, city, country, district, zipcode)
        if user_type=="supplier":
            sup = dao.create_supplier(fname, lname, phone, ac_id, address_id)
            print("sup sign up", sup)
            return sup
        pin = dao.create_pin(fname, lname, phone, ac_id, address_id)
        print("pin sign up", pin)
        return pin

    def Verify_PaymentMethod(self, pin_id):
        dao = peopledao()
        row = dao.getCreditCardByPinID(pin_id)
        if not row:
           return True
        else:
            return False

    def insert_new_cc(self, c_cardtype, c_number, c_name, pin_id, addressid):
        dao = peopledao()
        c_id = dao.insert_new_cc(c_cardtype, c_name, pin_id, addressid, c_number)
        result = {}
        result['Card ID'] = c_id
        result['Card Type'] = c_cardtype
        result['Card Number'] = c_number
        result['Name on the Card'] = c_name
        result['Person Id'] = pin_id
        result['Address Id'] = addressid
        return result

    def update_cc(self, c_id, c_cardtype, c_number, c_name, pin_id, addressid):
        dao = peopledao()
        c_id = dao.update_cc(c_id, c_cardtype, c_name, pin_id, addressid, c_number)
        result = {}
        result['Card ID'] = c_id
        result['Card Type'] = c_cardtype
        result['Card Number'] = c_number
        result['Name on the Card'] = c_name
        result['Person Id'] = pin_id
        result['Address Id'] = addressid
        return result

    def Verify_CCExists(self, pin_id):
        dao = peopledao()
        row = dao.getCreditCardByPinIDandC_ID(pin_id)
        result = {}
        result['Card ID'] = row[0]
        result['Card Type'] = row[1]
        result['Name on the Card'] = row[2]
        result['Person Id'] = row[3]
        result['Address Id'] = row[4]
        result['Card Number'] = row[5]
        return result


    def create_order(self, cid, date):
        dao = peopledao()
        row = dao.create_order(cid, date)
        return row