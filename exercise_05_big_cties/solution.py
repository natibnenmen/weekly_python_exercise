import requests
import csv

gist_url = "https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json"
filename = 'cities.csv'

def cities_to_csv(url, filename):
    r = requests.get(gist_url)
    big_cities_list = r.json()

    with open(filename, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='\t',)
        for city in big_cities_list:
            spamwriter.writerow([city['city'], city['state'], city['rank'], city['population']])
            #spamwriter.writerow([city['city'], city['state']])
