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
        cursor.execute(query, (p_id, district))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert_new_product(self, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit):
        cursor = self.conn.cursor()
        query = "insert into Product(ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit) values (%s, %s, %s, %s, %s, %s) returning p_id;"
        cursor.execute(query, (ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit,))
        p_id = cursor.fetchone()[0]
        self.conn.commit()
        return p_id

    def update_product(self, p_id, ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit):
        cursor = self.conn.cursor()
        query = "update product set ct_id = %s, s_id = %s, p_name = %s, p_qty = %s, p_unit = %s, p_priceperunit = %s where p_id = %s;"
        cursor.execute(query, (ct_id, s_id, p_name, p_qty, p_unit, p_priceperunit, p_id,))
        self.conn.commit()
        return p_id

    def getAllProductsA(self):
        cursor = self.conn.cursor()
        query = "select * from product where p_qty > 0 order by p_name;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchasableProduct(self):
        cursor = self.conn.cursor()
        query = "select * from product where p_priceperunit >= 0.01;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFreeProduct(self):
        cursor = self.conn.cursor()
        query = "select * from product where p_priceperunit = 0;"
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
