from flask import jsonify
from dao.product import ProductDAO

class producthandler:
    def build_product(self, row):
        result = {}
        result['p_id'] = row[0]
        result['p_ct'] = row[1]
        result['p_s'] = row[2]
        result['p_name'] = row[3]
        result['p_qty'] = row[4]
        result['p_unit'] = row[5]
        result['p_priceperunit'] = row[6]
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

    def getAllProducts(self):
        dao = ProductDAO()
        product_list = dao.getAllProducts()
        result_list = []
        for row in product_list:
            result = self.build_product(row)
            result_list.append(result)
        return jsonify(Product=result_list)

    def getAvailabilityOfProduct(self, p_id):
        dao = ProductDAO()
        row = dao.getAvailabilityOfProduct(p_id)
        if not row:
            return jsonify(error="product not found"), 404
        else:
            product = self.build_product(row)
            return jsonify(Product=product)

    def getProductById(self, p_id):
        dao = ProductDAO()
        row = dao.getProductById(p_id)
        if not row:
            return jsonify(error="product not found"), 404
        else:
            product = self.build_product(row)
            return jsonify(Product=product)

    def getProductByName(self, p_name):
        dao = ProductDAO()
        row = dao.getProductByName(p_name)
        if not row:
            return jsonify(error="product not found"), 404
        else:
            product = self.build_product(row)
            return jsonify(Product=product)

    def getProductsByQuantity(self, p_qty):
        dao = ProductDAO()
        product_list = dao.getProductByQty(p_qty)
        result_list = []
        for row in product_list:
            result = self.build_product(row)
            result_list.append(result)
        return jsonify(Product=result_list)

    def findSpecificProduct(self, args):
        p_id = args.get("p_id")
        district = args.get("district")
        dao = ProductDAO()
        product_list = []
        if (len(args) == 2) and p_id and district:
            product_list = dao.findSpecificProduct(p_id, district)
        else:
            return jsonify(error="Malformed query string"), 400
        result_list = []
        for row in product_list:
            result = self.build_product(row)
            result_list.append(result)
        return jsonify(Product=result_list)

    # def searchProductByAvailability(self, args):
    #     p_id = args.get("p_id")
    #     p_name = args.get("p_name")
    #     p_qty = args.get("p_qty")
    #     p_priceperunit = args.get("p_priceperunit")
    #     ct_type = args.get("ct_type")
    #     dao = ProductDAO()
    #     product_list = []
    #     if (len(args) == 1) and p_id and p_qty > 0:
    #         product_list = dao.getProductById(p_id)
    #     elif (len(args) == 1) and p_name and p_qty > 0:
    #         product_list = dao.getProductByName(p_name)
    #
    #     elif (len(args) == 1) and p_qty:
    #         product_list = dao.browseresourcesrequestedbydate(p_qty)
    #
    #     elif (len(args) == 1) and p_priceperunit and p_qty > 0:
    #         product_list = dao.getProductsGreaterPPU(p_priceperunit)
    #
    #     elif (len(args) == 1) and ct_type and p_qty > 0:
    #         product_list = dao.getProductsByCategoryName(ct_type)
    #     else:
    #         return jsonify(error="malformed query string"), 400
    #     result_list = []
    #     for row in product_list:
    #         result = self.build_product(row)
    #         result_list.append(result)
    #     return jsonify(Product=product_list)
    #

