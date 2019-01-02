import webbrowser
import json
import requests
import time

url = 'https://www.supremenewyork.com/mobile_stock.json'

response = requests.get(url=url)

data = json.loads(response.content)

for result in data['products_and_categories']['new']:
    num = str(result['id'])
    if num[0] == '3':
        locale = 'EU'
    else:
        locale = 'US'
    global locales
    locales = locale



print(data['release_week']+' New Products','-',locales, data['release_date'])
print('------------------------------------------------------------------------------------------------------------')

def keysearch(key):
    mylist = []
    global mylists
    mylists = mylist
    for result in data['products_and_categories']['new']:
        if keyword in result['name'].lower():
            print('Product Found!')
            name = result['name']
            id = result['id']
            cat = result['category_name']
            price = '${}'.format(result['price']*.01)
            link = 'https://www.supremenewyork.com/shop/{}'.format(id)
            mylist.append(id)
            print(len(mylist), end=""),
            print('.)', end = ""),
            print(name,'-',cat, '-', price)
            webbrowser.open(link)

keyword = input('Enter Keyword, Hit Enter When Ready:').lower()
print()

keysearch(keyword)


if not mylists:
    for _ in range(10):
        print('Product Not Found, Will Look Again...')
        time.sleep(0.5)
        keysearch(keyword)
    print('No Product Found-Program Ended')
print('------------------------------------------------------------------------------------------------------------')



