from bs4 import BeautifulSoup
from urllib import request
from myapp.models import Restaurant, User, Review
import sys
import sqlite3 as lite


def get_beautifulsoup():
    url = "https://www.tripadvisor.es/Restaurant_Review-g666182-d2393788-Reviews-Mas_Que_Tapas-El_Viso_del_Alcor_Province_of_Seville_Andalucia.html"
    f = request.urlopen(url)
    page = f.read().decode(f.headers.get_content_charset())
    f.close()
    return BeautifulSoup(page, 'html.parser')


def find_url_restaurant():
    res = []
    url = "https://www.tripadvisor.es/Restaurant_Review-g666182-d2393788-Reviews-Mas_Que_Tapas-El_Viso_del_Alcor_Province_of_Seville_Andalucia.html"
    soup = get_beautifulsoup()
    header = soup.find("div",{"class":"ppr_rup ppr_priv_resp_rr_top_info"})
    name = header.find("h1",{"class":"ui_header h1"}).text
    town = soup.find("span",{"class":"brand-global-nav-geopill-GeoPill__pill--3spqt ui_pill inverted"}).text
    addressParts = header.find("span",{"class":"detail"}).findAll("span")
    address = ""
    for part in addressParts:
        address += part.text + " "
    phone = header.find("span",{"class":"detail is-hidden-mobile"}).text
    header2 = soup.find("div",{"class":"restaurants-detail-overview-cards-DetailsSectionOverviewCard__detailCard--WpImp"}).findAll("div",{"class":"restaurants-detail-overview-cards-DetailsSectionOverviewCard__tagText--1OH6h"})
    food_types = header2[0].text
    special_diets = header2[1].text
    aux = [name, town, address, phone, food_types, special_diets]
    res.append(aux)
    return res

def find_url_user_review():
    res = []
    url = "https://www.tripadvisor.es/Restaurant_Review-g666182-d2393788-Reviews-Mas_Que_Tapas-El_Viso_del_Alcor_Province_of_Seville_Andalucia.html"
    soup = get_beautifulsoup()
    containers = soup.find("div",{"class":"listContainer hide-more-mobile"})
    reviews = containers.findAll("div",{"class":"review-container"})
    header = soup.find("div",{"class":"ppr_rup ppr_priv_resp_rr_top_info"})
    restaurantName = header.find("h1",{"class":"ui_header h1"}).text
    for review in reviews:
        username = review.find("div", {"class":"info_text pointer_cursor"}).text
        photo = review.find("img",{"class":"basicImg"}).get('data-lazyurl')
        rate = review.find("div",{"class":"ui_column is-9"}).find("span").get('class')[1][-2:-1]
        visit_date = review.find("div",{"class":"prw_rup prw_reviews_stay_date_hsx"}).text
        title = review.find("span",{"class":"noQuotes"}).text
        description = review.find("p",{"class":"partial_entry"}).text
        aux = [username, photo, rate, visit_date, title, description,restaurantName]
        res.append(aux)
    return res



# def find_url_aux(url):
#     res = []
#     for i in range(3):
#         res.extend(find_url(url + "?page=" + str(i)))
#     return res

def import_restaurants():
    print('Indexing restaurants... look at progress:')
    restaurantsAux = find_url_restaurant()
    Restaurant.objects.all().delete()
    restaurants = []
    for restaurantAux in restaurantsAux:
        try:
            name = restaurantAux[0]
            town = restaurantAux[1]
            address = restaurantAux[2]
            phone = restaurantAux[3]
            food_types = restaurantAux[4]
            special_diets = restaurantAux[5]

            restaurants.append(Restaurant(name=name, town=town, address=address, phone=phone, food_types=food_types, special_diets=special_diets))
            
        except:
            e = sys.exc_info()[0]
            print("Error when creating a restaurant: {0}".format(e))
    Restaurant.objects.bulk_create(restaurants)

def import_reviews_users():
    print('Indexing reviews... look at progress:')
    aux = find_url_user_review()
    User.objects.all().delete()
    Review.objects.all().delete()
    reviews = []
    users = []
    for line in aux:
        try:
            name = line[0]
            photo = line[1]
    
            users.append(User(name=name,photo=photo))
            
        except:
            e = sys.exc_info()[0]
            print("Error when creating a review or user: {0}".format(e))
    User.objects.bulk_create(users)
   
    for line in aux:
        try:
            rate = line[2]
            visit_date = line[3]
            title = line[4]
            description = line[5]
            restaurant_name = line[6]
            user_name = line[0]
            
            restaurant_id = find_db_restaurant(restaurant_name)[0][0]
            user_id = find_db_user(user_name)[0][0]
    
            reviews.append(Review(user_id=user_id,restaurant_id=restaurant_id, rate=rate,visit_date=visit_date, title=title, description=description))
            
        except:
            e = sys.exc_info()
            print("Error when creating a review or user: {0}".format(e))
    Review.objects.bulk_create(reviews)


def find_db_user(name):
    conn = lite.connect('db.sqlite3')
    conn.text_factory = str
    if name is not None:
        s = "%" + name + "%"
        cursor = conn.execute("SELECT id FROM myapp_user WHERE NAME LIKE ?", (s,))        
    res = []
    for row in cursor:
        res.append(row)
    conn.close()
    return res


def find_db_restaurant(name):
    conn = lite.connect('db.sqlite3')
    conn.text_factory = str
    if name is not None:
        s = "%" + name + "%"
        cursor = conn.execute("SELECT id FROM myapp_restaurant WHERE name LIKE ?", (s,))        
    res = []
    for row in cursor:
        res.append(row)
    conn.close()
    return res


if __name__ == '__main__':
    import_restaurants()