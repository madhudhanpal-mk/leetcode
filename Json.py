import requests, json

title = 'Python'
url = f'https://www.googleapis.com/books/v1/volumes?q={title}'
response = requests.get(url).json()

data = response['items']

s1 = json.dumps(data)
books = json.loads(s1)

BookDB = []

for i in range(len(data)):
    if 'listPrice' in books[i]['saleInfo']:
        tempBooks = {
            'title': books[i]['volumeInfo']['title'],
            'price' :books[i]['saleInfo']['listPrice']['amount'],
            'currencyCode' :  books[i]['saleInfo']['listPrice']['currencyCode'],
            'authors' : books[i]['volumeInfo']['authors']
        }
        print
        BookDB.append(tempBooks)
    else:
        tempBooks = {
            'title' : books[i]['volumeInfo']['title'],
            'price' : "Not available",
            'currencyCode' :  'Not Available',
            'authors' : books[i]['volumeInfo']['authors']
        }
        BookDB.append(tempBooks)


for i in range(len(BookDB)):
    print(BookDB[i])




    
   