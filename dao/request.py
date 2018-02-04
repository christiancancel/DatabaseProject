from config.dbconfig import pg_config
import psycopg2


class RequestDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequest(self):
        cursor = self.conn.cursor()
        query = "select * from request;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    # ######################SEARCH BY REQUESTED######################
    def browseResourcesRequestedByr_id(self, r_id):
        cursor = self.conn.cursor()
        query = "select pin_fname, pin_lname, r_pname, r_qty, r_date from request natural inner join pin " \
                "where r_id = %s order by r_pname;"
        cursor.execute(query, (r_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def browseResourcesRequestedByr_pname(self, r_pname):
        cursor = self.conn.cursor()
        query = "select pin_fname, pin_lname, r_pname, r_qty, r_date from request natural inner join pin " \
                "where r_pname = %s order by r_pname;"
        cursor.execute(query, (r_pname,))
        result = []

        for row in cursor:
            result.append(row)
        return result


    def browseResourcesRequestedByDate(self, r_date):
        cursor = self.conn.cursor()
        query = "select pin_fname, pin_lname, r_pname, r_qty, r_date from request natural inner join pin " \
                "where r_date = %s order by r_pname;"
        cursor.execute(query, (r_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def browseResourcesRequestedByQty(self, r_qty):
        cursor = self.conn.cursor()
        query = "select pin_fname, pin_lname, r_pname, r_qty, r_date from request natural inner join pin " \
                "where r_qty = %s order by r_pname;"
        cursor.execute(query, (r_qty,))
        result = []
        for row in cursor:
            result.append(row)
        return result
