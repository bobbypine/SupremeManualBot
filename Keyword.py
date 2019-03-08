import webbrowser
import json
import requests
import time


def keysearch(key):
    starttime = time.time()
    url = 'https://www.supremenewyork.com/mobile_stock.json'
    response = requests.get(url=url)
    data = json.loads(response.content.decode('utf-8'))
    mylist = []
    global mylists
    mylists = mylist
    for items in data['products_and_categories']:
        if items != 'new':
            categories = items
        for x in categories.split():
            for result in data['products_and_categories']['{}'.format(x)]:
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
                    print('Product Found and Opened in {:.2f} Seconds'.format(time.time()-starttime))
                    print()

keyword = input('Enter Keyword(s), Hit Enter When Ready:').lower()
keylist = keyword.split(",")
print()

try:
    for keyword in keylist:
        keysearch(keyword)
        if not mylists:
            for _ in range(10):
                print('Product Not Found, Will Look Again...')
                time.sleep(0.5)
                keysearch(keyword)
            print('No Product Found-Program Ended')
        print('------------------------------------------------------------------------------------------------------------')
except Exception as e:
    print('{}: or Webstore Closed'.format(e))


