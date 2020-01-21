from myapp.models import Restaurant, User, Review
import sys
import sqlite3 as lite

class SqliteConsults:

    def get_search(self,atribute_to_find, table, ciega, atribute_to_compare='*', search='*'):
        res = []
        try:
            conn = lite.connect('db.sqlite3')
            conn.text_factory = str
            search_aux = "%" + str(search) + "%"
            if ciega:
                cursor = conn.execute("SELECT * FROM {}".format(table))
            else:
                query = "SELECT {} FROM {} WHERE {} LIKE '{}'".format(atribute_to_find, table, atribute_to_compare, search_aux)
                cursor = conn.execute(query)
            for row in cursor:
                res.append(row)
            conn.close()
        except:
            e = sys.exc_info()
            print("Error doing the search (get_search): {0}".format(e))
        return res        

    def get_restaurants(self):
        return Restaurant.objects.all()

    def get_restaurant_by_id(self, id):
        return self.get_search('*', 'myapp_restaurant', False, 'id', str(id))

    def get_users(self):
        return User.objects.all()

    def get_user_by_id(self, id):
        return self.get_search('*', 'myapp_user', False, 'id', str(id))

    def get_reviews(self):
        return Review.objects.all()

    '''Position 0 is the review, position 1 is de restaurant and position 2 is the user'''
    def ger_reviews_with_user_and_restaurant(self):
        res = []
        reviews = self.get_search('*', 'myapp_review', True)
        for review in reviews:
            aux = []
            restaurant = self.get_restaurant_by_id(review[4])
            user = self.get_user_by_id(review[5])
            aux.append(review)
            aux.append(restaurant[0])
            aux.append(user[0])
            res.append(aux)
        return res
