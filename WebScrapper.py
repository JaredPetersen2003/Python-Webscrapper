from bs4 import BeautifulSoup
import requests
import pandas as pd
master_list = []
for page in range(1, 51):
    print('getting page ' + str(page))
    response = requests.get('http://books.toscrape.com/catalogue/page-' + str(page)  + '.html')
    site = response.text
    soup = BeautifulSoup(site, 'lxml')
    books = soup.find_all('article', {'class':'product_pod'})


    def book_list(lisiting):   
        lisiting_dict = {}
        price = lisiting.find('p', {'class', 'price_color'}).text
        availability = lisiting.find('p', {'class':'instock availability'}).text.strip()
        source = lisiting.img['src']

        lisiting_dict['Title'] = lisiting.img['alt']
        lisiting_dict['Image_source'] = ('http://books.toscrape.com/' + source[2:])
        lisiting_dict['Price'] = price[1:]
        lisiting_dict['Rating'] = (lisiting.p['class'][1])
        lisiting_dict['Availability'] = availability
        return lisiting_dict

    
    for lisiting in books:
        books = book_list(lisiting)
        master_list.append(books)

df = pd.DataFrame(master_list)
df.to_csv("Book_listings.csv", index = False)
