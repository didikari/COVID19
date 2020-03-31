import requests
import simplejson
from datetime import datetime

title = "[ DATA CORONA VIRUS ]"
print(title.center(50,'='))
country = input("Find Country Region : ")

url = f'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?where=Country_Region%20like%20%27%25{country}%25%27&outFields=Country_Region,Last_Update,Recovered,Confirmed,Deaths&returnGeometry=false&outSR=4326&f=json'
r = requests.get(url)
res = simplejson.loads(r.text)

infections = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Confirmed%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&cacheHint=true'
r = requests.get(infections)
res_infections = simplejson.loads(r.text)
res_infections = res_infections['features'][0]['attributes']['value']

deaths = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Deaths%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&cacheHint=true'
r = requests.get(deaths)
res_deaths = simplejson.loads(r.text)
res_deaths = res_deaths['features'][0]['attributes']['value']

recovered = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Recovered%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&cacheHint=true'
r = requests.get(recovered)
res_recovered = simplejson.loads(r.text)
res_recovered = res_recovered['features'][0]['attributes']['value']

text = "[ WORLDWIDE TOTALS ]"
print(text.center(50,'='))
print(f'Infections : {res_infections}')
print(f'Deaths : {res_deaths}')
print(f'Recovered : {res_recovered}')
print('='*50)

res = [record['attributes'] for record in res['features']]
for rec in res:
    Last_Update = str(rec['Last_Update'])[0:10]
    for name,value in rec.items():
        rec['Last_Update'] = datetime.fromtimestamp(int(Last_Update)).strftime('%d %B %Y')
        print(f'{name} : {value}')

    print("="*50)
