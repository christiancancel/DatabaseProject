from flask import jsonify
from dao.product import ProductDAO
from dao.people import peopledao
import time

class producthandler:
    def build_product(self, row):
        result = {}
        result['p_id'] = row[0]
        result['p_ct'] = row[1]
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

    def build_product_attributes(self, p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit):
        result = {}
        result['p_id'] = p_id
        result['ct_id'] = ct_id
        result['s_id'] = s_id
        result['p_name'] = p_name
        result['p_qty'] = p_qty
        result['p_unit'] = p_unit
        result['p_priceperunit'] = p_priceperunit
        return result


    def build_category(self, row):
        result = {}
        result['ct_Id'] = row[0]
        result['ct_type'] = row[1]
        result['ct_description'] = row[2]
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

    def build_addresses_dict(self, row):
        result = {}
        result['addressId'] = row[0]
        result['addressline1'] = row[1]
        result['zipcode'] = row[2]
        result['country'] = row[3]
        result['district'] = row[4]
        return result

    def build_order_attributes(self, oid, odid, qty, pprice, sup, ba, pid, pin, cid, date, supfn, supln, pinfn, pinln,
                                pname):
        result = {}
        result['o_id'] = oid
        result['od_id'] = odid
        result['od_qty'] = qty
        result['od_pprice'] = pprice
        result['s_id'] = sup
        result['ba_id'] = ba
        result['p_id'] = pid
        result['Product Name'] = pname
        result['pin_id'] = pin
        result['c_id'] = cid
        result['o_date'] = date
        result['Supplier Name'] = supfn + " " + supln
        result['Customer Name'] = pinfn + " " + pinln
        return result


    def get_all_products(self):
        dao = ProductDAO()
        product_list = dao.get_all_products()
        result_list = []
        for row in product_list:
            result = self.build_new_product(row)
            result_list.append(result)
        return jsonify(Product=result_list)



    def getProductById(self, p_id):
        dao = ProductDAO()
        row = dao.getProductById(p_id)
        if not row:
            return jsonify(error="product not found"), 404
        else:
            product = self.build_product(row)
            return jsonify(Product=product)


    def insert_product(self, form):
        if len(form) != 6:
            return jsonify(Error="Malformed post request"), 400
        else:
            ct_id = form['ct_id']
            s_id = form['s_id']
            p_name = form['p_name']
            p_qty = form['p_qty']
            p_unit = form['p_unit']
            p_priceperunit = form['p_priceperunit']
            if  s_id and p_name and p_qty and p_unit and p_priceperunit and ct_id:
                dao = ProductDAO()
                p_id = dao.insert_product(ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit)
                result = self.build_product_attributes(p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit)
                return jsonify(Product=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def search_products(self, args):
        dao = ProductDAO()
        ct_id = args.get("ct_id")
        s_id = args.get("s_id")
        p_name = args.get("p_name")
        p_qty = args.get("p_qty")
        p_unit = args.get("p_unit")
        p_priceperunit = args.get("p_priceperunit")
        product_list = []
        if len(args) == 1 and ct_id:
            product_list = dao.filter_products(ct_id, 1)
        elif  len(args) == 1 and s_id:
            product_list  =dao.filter_products(s_id, 2)
        elif len(args) == 1 and p_name:
            product_list = dao.filter_products(p_name, 3)
        elif len(args) == 1 and p_qty:
            product_list = dao.filter_products(p_qty, 4)
        elif len(args) == 1 and p_unit:
            product_list = dao.filter_products(p_unit, 5)
        elif len(args) == 1 and p_priceperunit:
            product_list = dao.filter_products(p_priceperunit, 6)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in product_list:
            result = self.build_new_product(row)
            result_list.append(result)
        return jsonify(Products=result_list)

    def update_product(self, p_id, form):
        dao = ProductDAO()
        if not dao.getProductById(p_id):
            return jsonify(Error="Product not found."), 404
        else:
            if len(form) != 6:
                return jsonify(Error="Malformed update request"), 400
            else:
                ct_id = form['ct_id']
                s_id = form['s_id']
                p_name = form['p_name']
                p_qty = form['p_qty']
                p_unit = form['p_unit']
                p_priceperunit = form['p_priceperunit']
            if s_id and p_name and p_qty and p_unit and p_priceperunit and ct_id:
                dao.update_product(p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit)
                result = self.build_product_attributes(p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit)
                return jsonify(Product=result), 200
            else:
                return jsonify(Error="Unexpected attributes in update request"), 400

    def delete_product(self, pid):
        dao = ProductDAO()
        if not dao.getProductById(pid):
            return jsonify(Error="Product not found."), 404
        else:
            dao.delete_product(pid)
        return jsonify(DeleteStatus="OK"), 200

    def getFreeProduct(self):
        dao = ProductDAO()
        product_list = dao.getFreeProduct()
        result_list = []
        for row in product_list:
            result = self.build_product(row)
            result_list.append(result)
        max_order = int(dao.get_max_order_id()) + 1
        message = "For a new order please use order id: " + str(max_order) + ", if not please reuse your order id."
        return jsonify(Message=message, PurchasableProduct=result_list)

    def getPurchasableProduct(self):
        dao = ProductDAO()
        product_list = dao.getPurchasableProduct()
        result_list = []
        for row in product_list:
            result = self.build_product(row)
            result_list.append(result)
        max_order = int(dao.get_max_order_id()) + 1
        message = "For a new order please use order id: " + str(max_order) + ", if not please reuse your order id."
        return jsonify(Message=message,PurchasableProduct=result_list)

    def buy_product(self, form):
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            o_id = int(form['o_id'])
            pin_id = int(form['pin_id'])
            qty = int(form['od_qty'])
            p_id = int(form['p_id'])
            s_id = int(form['s_id'])
            if o_id and pin_id and qty and p_id and s_id:
                if qty <= 0 or o_id <= 0 or pin_id <=0 or p_id <= 0 or s_id <= 0:
                    return jsonify(Error="Invalid inputs o_id and/or pin_id and/or s_id and/or p_id and/or od_qty")
                else:
                    dao = ProductDAO()
                    pdao = peopledao()
                    date = time.strftime("%d%m%Y")
                    verify_o_id = pdao.check_o_id(o_id)  # returns true if o_id is less or equal max o_id, else false
                    verify_pin_id = pdao.check_pin(pin_id)  # return c_id if pin_id is valid, false otherwise
                    verify_sup = pdao.check_sup(s_id)  # returns ba_id if valid s_id, false otherwise
                    verify_product = dao.check_product(p_id, qty)  # return true if valid p_id & qty is less than db qty
                    if not(verify_o_id and verify_pin_id and verify_product and verify_sup):
                        return jsonify(Error="Invalid inputs o_id and/or pin_id and/or s_id and/or p_id and/or od_qty")
                    else:
                        c_id = verify_pin_id[2]
                        ba_id = verify_sup[2]
                        p_priceperunit = verify_product[2]
                        pname = verify_product[3]
                        pin_fname = verify_pin_id[0]
                        pin_lname = verify_pin_id[1]
                        sup_fname = verify_sup[0]
                        sup_lname = verify_sup[1]
                        real_o_id = pdao.check_or_create_o_id(o_id, c_id, date)
                        order = dao.insert_product_to_OrderDetails(qty, p_priceperunit, real_o_id, pin_id, s_id,
                                                                    ba_id, p_id)
                        if not order:
                            return jsonify(Error="Purchase did not go through")
                        else:
                            order_details = self.build_order_attributes(real_o_id, order, qty, p_priceperunit, s_id,
                                                                        ba_id, p_id, pin_id, c_id, date, sup_fname,
                                                                        sup_lname, pin_fname, pin_lname, pname)
                            return jsonify(OrderDetails=order_details)
            else:
                return jsonify(Error="Invalid Inputs")


