from config.dbconfig import pg_config
import psycopg2


class ProductDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllProducts(self):
        cursor = self.conn.cursor()
        query = "select * from product;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def get_all_products(self):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, s_fname, s_lname, ct_type " \
                "from supplier natural inner join product natural inner join category " \
                "where supplier.s_id = product.s_id " \
                "AND product.ct_id = category.ct_id " \
                "ORDER BY p_name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def browseResourcesAvailable(self):
        cursor = self.conn.cursor()
        query = "select * from product where p_qty > 0 order by p_name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getProductById(self, p_id):
        cursor = self.conn.cursor()
        query = "select * from product where p_id = %s;"
        cursor.execute(query, (p_id,))
        result = cursor.fetchone()
        return result

    def getAvailabilityOfProduct(self, p_id):
        cursor = self.conn.cursor()
        query = "select * from product where p_id = %s order by p_name;"
        cursor.execute(query, (p_id,))
        result = cursor.fetchone()
        return result

    def getProductByName(self, p_name):
        cursor = self.conn.cursor()
        query = "select * from product where p_name = %s;"
        cursor.execute(query, (p_name,))
        result = cursor.fetchone()
        return result

    def getProductByQty(self, p_qty):
        cursor = self.conn.cursor()
        query = "select * from product where p_qty = %s order by p_name;"
        cursor.execute(query, (p_qty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getProductGreaterQty(self, p_qty):
        cursor = self.conn.cursor()
        query = "select * from product where p_qty >= %s order by p_name;"
        cursor.execute(query, (p_qty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getProductLessQty(self, p_qty):
        cursor = self.conn.cursor()
        query = "select * from product where p_qty < %s order by p_name;"
        cursor.execute(query, (p_qty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getProductsGreaterPPU(self, p_priceperunit):
        cursor = self.conn.cursor()
        query = "select * from product where p_priceperunit >= %s order by p_name;"
        cursor.execute(query, (p_priceperunit,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getProductsEqualPPU(self, p_priceperunit):
        cursor = self.conn.cursor()
        query = "select * from product where p_priceperunit = %s order by p_name;"
        cursor.execute(query, (p_priceperunit,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getProductsLessPPU(self, p_priceperunit):
        cursor = self.conn.cursor()
        query = "select * from product where p_priceperunit < %s order by p_name;"
        cursor.execute(query, (p_priceperunit,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getProductsByCategoryID(self, ct_id):
        cursor = self.conn.cursor()
        query = "select * from product natural inner join category where ct_id = %s order by p_name;"
        cursor.execute(query, (ct_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getProductsByCategoryName(self, ct_type):
        cursor = self.conn.cursor()
        query = "select * from product natural inner join category where ct_type = %s order by p_name;"
        cursor.execute(query, (ct_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getProductsBySubcategory(self, sct_type):
        cursor = self.conn.cursor()
        query = "select * from product natural inner join category natural inner join IsSubcategory " \
                "where sct_type = %s order by p_name;"
        cursor.execute(query, (sct_type,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def findProductByDistrict(self, district):
        cursor = self.conn.cursor()
        query = "select * from product natural inner join supplier natural inner join addresses " \
                "where p_id = %s and district = %s;"
        cursor.execute(query, (district,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def findSpecificProduct(self, p_id, district):
        cursor = self.conn.cursor()
        query = "select * from product natural inner join supplier natural inner join addresses " \
                "where p_id = %s and district = %s;"
        cursor.execute(query, (p_id, district,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert_product(self, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit):
        cursor = self.conn.cursor()
        query = "insert into Product(ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit) values (%s, %s, %s, %s, %s, %s) returning p_id;"
        cursor.execute(query, (ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit,))
        p_id = cursor.fetchone()[0]
        self.conn.commit()
        return p_id


    def filter_products(self, form, int):
        cursor = self.conn.cursor()
        query = "select p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, s_fname, s_lname, ct_type " \
                "from supplier natural inner join product natural inner join category " \
                "where supplier.s_id = product.s_id " \
                "AND product.ct_id = category.ct_id "
        if int == 1:
            query = query + "AND ct_id = %s;"
        elif int == 2:
            query = query + "AND s_id = %s;"
        elif int == 3:
            query = query + "AND p_name = %s;"
        elif int == 4:
            query = query + "AND p_qty = %s;"
        elif int == 5:
            query = query + "AND p_unit = %s;"
        else:
            query = query + "AND p_priceperunit = %s;"
        cursor.execute(query, (form,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def get_category_id(self, ct_type):
        cursor = self.conn.cursor()
        query = "select ct_id from category where ct_type = %s;"
        cursor.execute(query, (ct_type,))
        ct_id = cursor.fetchone()[0]
        return ct_id


    def create_category(self, ct_type):
        cursor = self.conn.cursor()
        query = "insert into category(ct_type) values (%s) returning ct_id;"
        cursor.execute(query, (ct_type,))
        ct_id = cursor.fetchone()[0]
        self.conn.commit()
        return ct_id

    def update_product(self, p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit):
        cursor = self.conn.cursor()
        query = "update product set ct_id = %s, s_id = %s, p_name = %s, p_qty = %s, p_unit = %s, p_priceperunit = %s where p_id = %s;"
        cursor.execute(query, (ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, p_id,))
        self.conn.commit()
        return p_id

    def delete_product(self, pid):
        cursor = self.conn.cursor()
        query = "delete from product where pid = %s;"
        cursor.execute(query, (pid,))
        self.conn.commit()
        return pid

    def getPurchasableProduct(self):
        cursor = self.conn.cursor()
        query = "select * from product where p_priceperunit >= 0.01 AND p_qty > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def check_product(self, p, qty):
        cursor = self.conn.cursor()
        query = "select p_id, p_qty, p_priceperunit, p_name from product where p_id = %s;"
        cursor.execute(query, (p,))
        test = cursor.fetchone()
        print(test)
        if not test:
            return False
        else:
            if qty <= test[1]:
                return test
            else:
                return False

    def insert_product_to_OrderDetails(self, od_qty, od_price, o_id, pin_id, s_id, ba_id, p_id):
        cursor = self.conn.cursor()
        query = "insert into orderdetails(od_qty, od_pprice, o_id, s_id, ba_id, p_id, pin_id) values (%s, %s, %s, %s, %s, %s, %s) returning od_id;"
        cursor.execute(query, (od_qty, od_price, o_id, s_id, ba_id, p_id, pin_id,))
        od_id = cursor.fetchone()[0]
        self.conn.commit()
        return od_id

    def get_max_order_id(self):
        cursor = self.conn.cursor()
        query = "select max(o_id) from orders;"
        cursor.execute(query)
        od_id = cursor.fetchone()[0]
        return od_id

    def getFreeProduct(self):
        cursor = self.conn.cursor()
        query = "select * from product where p_priceperunit = 0 AND p_qty > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #NOT YET

    # def insert(self, pname, pcolor, pmaterial, pprice):
    #     cursor = self.conn.cursor()
    #     query = "insert into parts(pname, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
    #     cursor.execute(query, (pname, pcolor, pmaterial, pprice,))
    #     pid = cursor.fetchone()[0]
    #     self.conn.commit()
    #     return pid
    #
    #
    # def delete(self, pid):
    #     cursor = self.conn.cursor()
    #     query = "delete from parts where pid = %s;"
    #     cursor.execute(query, (pid,))
    #     self.conn.commit()
    #     return pid
    #
    #
    # def update(self, pid, pname, pcolor, pmaterial, pprice):
    #     cursor = self.conn.cursor()
    #     query = "update parts set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
    #     cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
    #     self.conn.commit()
    #     return pid
    #
