from flask import jsonify
from dao.people import peopledao
from dao.product import ProductDAO


class PeopleHandler:
    def build_bankinfo_dict(self, row):
        result = {}
        result['ba_id'] = row[0]
        result['s_id'] = row[1]
        result['ba_accnumber '] = row[2]
        result['ba_routingnumber '] = row[3]
        return result

    def build_bankinfo_attributes(self, a, b, c, d):
        result = {}
        result['ba_id'] = a
        result['s_id'] = b
        result['ba_accnumber '] = c
        result['ba_routingnumber '] = d
        return result

    def build_creditcard_dict(self, row):
        result = {}
        result['c_id'] = row[0]
        result['c_cardtype '] = row[1]
        result['c_cardnumber '] = row[2]
        result['c_cardname '] = row[3]
        result['pin_id '] = row[4]
        result['addressid '] = row[5]
        return result

    def build_creditcard_attributes(self, a, b, c, d, e, f):
        result = {}
        result['c_id'] = a
        result['c_cardtype '] = b
        result['c_cardnumber '] = c
        result['c_cardname '] = d
        result['pin_id '] = e
        result['addressid '] = f
        return result

    def build_account_dict(self, row):
        result = {}
        result['a_id'] = row[0]
        result['a_username  '] = row[1]
        result['a_password  '] = row[2]
        return result

    def build_user_dict(self, row):
        result = {}
        result['a_id'] = row[0]
        result['a_username'] = row[1]
        result['a_password'] = row[2]
        return result

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

    def build_adminINS_dict(self, ad_id, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone, addressline1, city,
                            zipcode, country, district):
        result = {}
        result['ad_id'] = ad_id
        result['ad_fname'] = ad_fname
        result['ad_lname'] = ad_lname
        result['ada_id'] = ada_id
        result['adaddress_id'] = adaddress_id
        result['ad_phone'] = ad_phone
        result['addressline1'] = addressline1
        result['city'] = city
        result['zipcode'] = zipcode
        result['country'] = country
        result['district'] = district
        return result

    def build_pin_dict(self, row):
        result = {}
        result['pin_id'] = row[0]
        result['pin_fname'] = row[1]
        result['pin_lname'] = row[2]
        result['pina_id'] = row[3]
        result['pinaddress_id'] = row[4]
        result['pin_phone'] = row[5]
        result['addressline1'] = row[6]
        result['city'] = row[7]
        result['zipcode'] = row[8]
        result['country'] = row[9]
        result['district'] = row[10]
        return result

    def build_pinINS_dict(self, pin_id, pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone, addressline1, city,
                          zipcode, country, district):
        result = {}
        result['pin_id'] = pin_id
        result['pin_fname'] = pin_fname
        result['pin_lname'] = pin_lname
        result['pina_id'] = pina_id
        result['pinaddress_id'] = pinaddress_id
        result['pin_phone'] = pin_phone
        result['addressline1'] = addressline1
        result['city'] = city
        result['zipcode'] = zipcode
        result['country'] = country
        result['district'] = district

        return result

    def build_supplier_dict(self, row):
        result = {}
        result['s_id'] = row[0]
        result['s_fname'] = row[1]
        result['s_lname'] = row[2]
        result['sa_id'] = row[3]
        result['adressid'] = row[4]
        result['s_phone'] = row[5]
        result['addressline1'] = row[6]
        result['city'] = row[7]
        result['zipcode'] = row[8]
        result['country'] = row[9]
        result['district'] = row[10]
        return result

    def build_supplierINS_dict(self, s_id, s_fname, s_lname, sa_id, adressid, s_phone, addressline1, city, zipcode,
                               country, district):
        result = {}
        result['s_id'] = s_id
        result['s_fname'] = s_fname
        result['s_lname'] = s_lname
        result['sa_id'] = sa_id
        result['adressid'] = adressid
        result['s_phone'] = s_phone
        result['addressline1'] = addressline1
        result['city'] = city
        result['zipcode'] = zipcode
        result['country'] = country
        result['district'] = district
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

    def getAllPeopleInNeed(self):
        dao = peopledao()
        pin_list = dao.getAllPeopleInNeed()
        result_list = []
        for row in pin_list:
            result = self.build_pin_dict(row)
            result_list.append(result)
        return jsonify(PeopleInNeed=result_list)

    '''return everyone registered as administrator'''

    def getAllAdmin(self):
        dao = peopledao()
        suppliers_list = dao.getAllAdmin()
        result_list = []
        for row in suppliers_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
        return jsonify(Admins=result_list)

    '''Get All Orders'''



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

    def getSupplierByProduct(self, args):
        p_id = args
        dao = peopledao()
        product_list = []
        if p_id:
            product_list = dao.getSupplierByProductId(args)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in product_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(SupplierByProduct=result_list)



    '''Encontrar las ordenes de una supplier'''

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
        zipcode = args.get('zipcode')
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

    def get_all_products_by_district(self, args):
        dao = peopledao()
        district = args.get('district')
        if not district:
            product_list = dao.get_all_products_by_district()
        else:
            product_list = dao.get_all_products_by_district_declared(district)
        result_list = []
        for row in product_list:
            result = self.build_new_product_declared(row, 'district')
            result_list.append(result)
        return jsonify(ProductByDistrict=result_list)

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

    def insert_admin(self, form):
        if len(form) != 10:
            return jsonify(Error="Malformed post request"), 400
        else:
            ad_fname = form['ad_fname']
            ad_lname = form['ad_lname']
            a_username = form['a_username']
            a_password = form['a_password']
            ad_phone = form['ad_phone']
            addressline1 = form['addressline1']
            city = form['city']
            zipcode = form['zipcode']
            country = form['country']
            district = form['district']
            if ad_fname and ad_lname and ad_phone and addressline1 and city and zipcode and country \
                    and district and a_username and a_password:
                dao = peopledao()
                adaddress_id = dao.insert_new_address(addressline1, city, zipcode, country, district)
                ada_id = dao.insert_new_user(a_username, a_password)
                ad_id = dao.insert_new_admin(ad_fname, ad_lname, ada_id, adaddress_id, ad_phone)
                result = self.build_adminINS_dict(ad_id, ad_fname, ad_lname, ada_id, adaddress_id, ad_phone,
                                                  addressline1, city, zipcode, country, district)
                return jsonify(NewRequest=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getAllUsers(self):
        dao = peopledao()
        user_list = dao.getAllUsers()
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def get_bankinfo_by_SID(self, s_id):
        dao = peopledao()
        row = dao.get_bankaccount_by_s_id(s_id)
        if not row:
            return jsonify(Error="Bank Info Not Found"), 404
        else:
            result = self.build_bankinfo_dict(row)
            return jsonify(Bank_info_by_SID=result)

    def view_creditcard_by_PIN(self, pin_id):
        dao = peopledao()
        row = dao.view_creditcard_by_PIN(pin_id)
        if not row:
            return jsonify(Error="Bank Info Not Found"), 404
        else:
            result = self.build_creditcard_dict(row)
            return jsonify(Bank_info_by_SID=result)

    def search_account_by_a_id(self, a_id):
        dao = peopledao()
        row = dao.search_account_by_a_id(a_id)
        if not row:
            return jsonify(Error="Account Not Found"), 404
        else:
            result = self.build_account_dict(row)
            return jsonify(Account_By_a_id=result)

    def get_all_accounts(self):
        dao = peopledao()
        accounts_list = dao.get_all_accounts()
        result_list = []
        for row in accounts_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Accounts=result_list)

    def get_all_bank_info(self):
        dao = peopledao()
        ba_list = dao.get_all_bank_info()
        result_list = []
        for row in ba_list:
            result = self.build_bankinfo_dict(row)
            result_list.append(result)
        return jsonify(Accounts=result_list)

    def insert_bankinfo(self, form):
        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            s_id = form['s_id']
            ba_accnumber = form['ba_accnumber']
            ba_routingnumber = form['ba_routingnumber']

            if s_id and ba_accnumber and ba_accnumber:
                dao = peopledao()
                ba_id = dao.insert_bankinfo(s_id, ba_accnumber, ba_routingnumber)
                result = self.build_bankinfo_attributes(ba_id, s_id, ba_accnumber, ba_routingnumber)
                return jsonify(New_Bank_info=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insert_creditcard(self, form):
        if len(form) != 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            s_id = form['s_id']
            c_cardtype = form['c_cardtype']
            c_cardnumber = form['c_cardnumber']
            c_cardname = form['c_cardname']
            pin_id = form['pin_id']
            addressid = form['addressid']
            if s_id and c_cardtype and c_cardnumber and c_cardname and pin_id and addressid:
                dao = peopledao()
                c_id = dao.insert_creditcard(s_id, c_cardtype, c_cardnumber, c_cardname, pin_id, addressid)
                result = self.build_creditcard_attributes(c_id, c_cardtype, c_cardnumber, c_cardname, pin_id, addressid)
                return jsonify(New_CreditCard=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def update_creditcard(self, c_id, form):
        dao = peopledao()
        if not dao.get_creditcard(c_id):
            return jsonify(Error="Credit Card not found."), 404
        else:
            if len(form) != 6:
                return jsonify(Error="Malformed update request"), 400
            else:
                s_id = form['s_id']
                c_cardtype = form['c_cardtype']
                c_cardnumber = form['c_cardnumber']
                c_cardname = form['c_cardname']
                pin_id = form['pin_id']
                addressid = form['addressid']
                if s_id and c_cardtype and c_cardnumber and c_cardname and pin_id and addressid:
                    dao.update_creditcard(c_id, s_id, c_cardtype, c_cardnumber, c_cardname, pin_id, addressid)
                    result = self.build_creditcard_attributes(c_id, c_cardtype, c_cardnumber, c_cardname, pin_id,
                                                              addressid)
                    return jsonify(Updated_CreditCard=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400

    def update_bankinfo(self, s_id, form):
        dao = peopledao()
        ba_id = dao.check_bankinfo(s_id)
        if not ba_id:
            return jsonify(Error="CBank Info not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                ba_accnumber = form['ba_accnumber']
                ba_routingnumber = form['ba_routingnumber']
                if s_id and ba_accnumber and ba_accnumber:
                    dao.update_bankinfo(ba_id, s_id, ba_accnumber, ba_routingnumber)
                    result = self.build_bankinfo_attributes(ba_id, s_id, ba_accnumber, ba_routingnumber)
                    return jsonify(New_CreditCard=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400

                    ##SEARCH ADMIN BY REQUESTS##

    def searchADMINByRequests(self, args):
        ad_id = args.get("ad_id")
        ad_fname = args.get("ad_fname")
        ad_lname = args.get("ad_lname")
        ad_phone = args.get("ad_phone")
        city = args.get("city")
        country = args.get("country")
        district = args.get("district")
        dao = peopledao()
        request_list = []
        if (len(args) == 1) and ad_id:
            request_list = dao.GetADMINByID(ad_id)
        elif (len(args) == 1) and ad_fname:
            request_list = dao.GetADMINByFNAME(ad_fname)
        elif (len(args) == 1) and ad_phone:
            request_list = dao.GetADMINByPHONE(ad_phone)
        elif (len(args) == 1) and city:
            request_list = dao.GetADMINByCITY(city)
        elif (len(args) == 1) and country:
            request_list = dao.GetADMINByCOUNTRY(country)
        elif (len(args) == 1) and district:
            request_list = dao.GetADMINByDISTRICT(district)
        elif (len(args) == 2) and ad_fname and ad_lname:
            request_list = dao.GeADMINByFULLNAME(ad_fname, ad_lname)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in request_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
            print(row)
        return jsonify(Request=result_list)

    def insert_pin(self, form):
        if len(form) != 10:
            return jsonify(Error="Malformed post request"), 400
        else:
            pin_fname = form['pin_fname']
            pin_lname = form['pin_lname']
            a_username = form['a_username']
            a_password = form['a_password']
            pin_phone = form['pin_phone']
            addressline1 = form['addressline1']
            city = form['city']
            zipcode = form['zipcode']
            country = form['country']
            district = form['district']
            if pin_fname and pin_lname and pin_phone and addressline1 and city and zipcode and country \
                    and district and a_username and a_password:
                dao = peopledao()
                pinaddress_id = dao.insert_new_address(addressline1, city, zipcode, country, district)
                pina_id = dao.insert_new_user(a_username, a_password)
                pin_id = dao.insert_new_pin(pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone)
                result = self.build_adminINS_dict(pin_id, pin_fname, pin_lname, pina_id, pinaddress_id, pin_phone,
                                                  addressline1, city, zipcode, country, district)
                return jsonify(NewRequest=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def get_specific_pin(self, pin_id):
        dao = peopledao()
        result_list = []
        pin = dao.get_pin(pin_id)
        print(pin)
        result_list = self.build_pin_dict(pin)
        return jsonify(PIN=result_list)

    def update_pin(self, pin_id, form):
        dao = peopledao()
        if not dao.get_pin(pin_id):
            return jsonify(Error="Product not found."), 404
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                fname = form['pin_fname']
                lname = form['pin_lname']
                phone = form['pin_phone']
            if fname and lname and phone:
                check = dao.update_pin(pin_id, fname, lname, phone)
                profile = dao.get_pin(pin_id)
                print(profile)
                result = self.build_pin_dict(profile)
                return jsonify(PersonInNeed=result), 200
            else:
                return jsonify(Error="Unexpected attributes in update request"), 400

    def getAllpin(self):
        dao = peopledao()
        pin_list = dao.getAllpin()
        result_list = []
        for row in pin_list:
            result = self.build_pin_dict(row)
            result_list.append(result)
        return jsonify(PIN=result_list)

    ##SEARCH PIN BY REQUESTS##
    def searchPINByRequests(self, args):
        pin_id = args.get("pin_id")
        pin_fname = args.get("pin_fname")
        pin_lname = args.get("pin_lname")
        pin_phone = args.get("pin_phone")
        city = args.get("city")
        country = args.get("country")
        district = args.get("district")
        dao = peopledao()
        request_list = []

        if (len(args) == 1) and pin_id:
            request_list = dao.GetPINByID(pin_id)
        elif (len(args) == 1) and pin_fname:
            request_list = dao.GetPINByFNAME(pin_fname)
        elif (len(args) == 1) and pin_phone:
            request_list = dao.GetPINByPHONE(pin_phone)
        elif (len(args) == 1) and city:
            request_list = dao.GetPINByCITY(city)
        elif (len(args) == 1) and country:
            request_list = dao.GetPINByCOUNTRY(country)
        elif (len(args) == 1) and district:
            request_list = dao.GetPINByDISTRICT(district)
        elif (len(args) == 2) and pin_fname and pin_lname:
            request_list = dao.GetPINByFULLNAME(pin_fname, pin_lname)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in request_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
            print(row)

        return jsonify(Request=result_list)

    ####################################################################################################################
    ####### S U P P L I E R ############################################################################################

    def insert_sup(self, form):
        if len(form) != 10:
            return jsonify(Error="Malformed post request"), 400
        else:
            s_fname = form['s_fname']
            s_lname = form['s_lname']
            a_username = form['a_username']
            a_password = form['a_password']
            s_phone = form['s_phone']
            addressline1 = form['addressline1']
            city = form['city']
            zipcode = form['zipcode']
            country = form['country']
            district = form['district']
            if s_fname and s_lname and s_phone and addressline1 and city and zipcode and country \
                    and district and a_username and a_password:
                dao = peopledao()
                saddress_id = dao.insert_new_address(addressline1, city, zipcode, country, district)
                sa_id = dao.insert_new_user(a_username, a_password)
                s_id = dao.insert_new_sup(s_fname, s_lname, sa_id, saddress_id, s_phone)
                result = self.build_supplierINS_dict(s_id, s_fname, s_lname, sa_id, saddress_id, s_phone,
                                                     addressline1, city, zipcode, country, district)
                return jsonify(NewRequest=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getAllsup(self):
        dao = peopledao()
        sup_list = dao.getAllSUP()
        result_list = []
        for row in sup_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(PIN=result_list)

    ##SEARCH SUP BY REQUESTS##
    def searchSUPByRequests(self, args):
        s_id = args.get("s_id")
        s_fname = args.get("s_fname")
        s_lname = args.get("s_lname")
        s_phone = args.get("s_phone")
        city = args.get("city")
        country = args.get("country")
        district = args.get("district")
        dao = peopledao()
        request_list = []

        if (len(args) == 1) and s_id:
            request_list = dao.GetSUPByID(s_id)
        elif (len(args) == 1) and s_fname:
            request_list = dao.GetSUPByFNAME(s_fname)
        elif (len(args) == 1) and s_phone:
            request_list = dao.GetSUPByPHONE(s_phone)
        elif (len(args) == 1) and city:
            request_list = dao.GetSUPByCITY(city)
        elif (len(args) == 1) and country:
            request_list = dao.GetSUPByCOUNTRY(country)
        elif (len(args) == 1) and district:
            request_list = dao.GetSUPByDISTRICT(district)
        elif (len(args) == 2) and s_fname and s_lname:
            request_list = dao.GetSUPByFULLNAME(s_fname, s_lname)
        else:
            return jsonify(error="malformed query string"), 400
        result_list = []
        for row in request_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
            print(row)

        return jsonify(Request=result_list)
