from myapp.models import Restaurant

global url = https://www.tripadvisor.es/Restaurant_Review-g666182-d2393788-Reviews-Mas_Que_Tapas-El_Viso_del_Alcor_Province_of_Seville_Andalucia.html

def get_beautifulsoup(self):
    f = request.urlopen(self.url)
    page = f.read().decode(f.headers.get_content_charset())
    f.close()
    return BeautifulSoup(page, 'html.parser')


def find_url(self):
    res = []
    soup = get_beautifulsoup(self.url)
    name = 
    town = 
    address = 
    phone = 
    link = 
    food_types = 
    special_diets = 
    aux = [name, town, address, phone, link, food_types, special_diets]
    res.append(aux)
    return res



def find_url_aux(url):
    res = []
    for i in range(3):
        res.extend(find_url(url + "?page=" + str(i)))
    return res

def import_restaurants():
    print('Indexing restaurants... look at progress:')
    Restaurant.objects.all().delete()
    restaurants = []
        try:
            name = 
            town = 
            address = 
            phone = 
            link = 
            food_types = 
            special_diets = 

            r.append(Restaurant(name=name, town=town, address=address, phone=phone,
            link=link, food_types=food_types, special_diets=special_diets))
            
        except:
            e = sys.exc_info()[0]
            print("Error when creating a restaurant: {0}".format(e))
    Restaurant.objects.bulk_create(restaurants)
    print(str(z) + ' restaurants indexes\n')