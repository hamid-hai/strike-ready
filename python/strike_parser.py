import requests
import collections
import pandas as pd
from bs4 import BeautifulSoup
collections.Callable = collections.abc.Callable

r = requests.get('https://www.telegraph.co.uk/business/2023/07/12/train-strikes-2023-dates-rmt-rail-services-affected/')

soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('strong')
# print(results)



# first_result = results[0].text
# print(first_result)

# first_result = results[1].text
# print(first_result)

# first_result = results[2].text
# print(first_result)

# Looking inside each 'tag', this 'tag' contains one element, always use [0] referring to the first object within the tag.
# print(first_result.contents[0])


strike_dates = []
for result in results:
    strike_date = result.contents[0] + ' 2023'
    strike_dates.append((strike_date))

# print(len(strike_dates))
# print(strike_dates)

df = pd.DataFrame(strike_dates, columns=['Strike Dates'])

print(df.head())

# Converts to machine readable format in d-m-y format
# df['Strike Dates'] = pd.to_datetime(df['Strike Dates']).dt.strftime('%d-%m-%Y')
# print(df.head)

# Creating the CSV file, no index required, since most spreadsheet programs do this automatically
df.to_csv('strike_dates.csv', index=False, encoding='utf-8')

df = pd.read_csv('strike_dates.csv', parse_dates=['Strike Dates'], encoding='utf-8')

