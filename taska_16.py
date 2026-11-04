import collections

with open('shop.txt', encoding='utf-8') as shop_file:
    shops = list(map(lambda x: x.replace('\n', ''), shop_file))

city_shops = collections.defaultdict(list)

for line in shops:
    shop, city = line.split(':')
    print(shop, city)
    city_shops[city].append(shop)

print(city_shops)
from  faker  import Faker

fake = Faker()

for _ in range(5):
    print(fake.name())


import mysql.connector as mysql
import creds

db = mysql.connect(
    user=creds.user,
    passwd=creds.passwd,
    host=creds.host,
    port=creds.port,
    database=creds.database
)