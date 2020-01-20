from myapp.models import Restaurant, User, Review
import sys
import sqlite3 as lite

class SqliteConsults:

    def get_search(self,atribute_to_find, table, ciega, atribute_to_compare='*', search='*'):
        res = []
        try:
            conn = lite.connect('db.sqlite3')
            conn.text_factory = str
            search_aux = "%" + search + "%"
            if ciega:
                cursor = conn.execute("SELECT * FROM {}".format(table))
            else:
                cursor = conn.execute("SELECT {} FROM {} WHERE {} LIKE {}".format(atribute_to_find, table, atribute_to_compare, search_aux))
            for row in cursor:
                res.append(row)
            conn.close()
        except:
            e = sys.exc_info()[0]
            print("Error doing the search (get_search): {0}".format(e))
        return res        

    def get_restaurants(self):
        return self.get_search('*', 'myapp_restaurant', True)

    def get_users(self):
        return self.get_search('*', 'myapp_user', True)

    def get_reviews(self):
        return self.get_search('*', 'myapp_review', True)        