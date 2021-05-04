import requests
import json
import datetime
"""
Json from open ottawa

https://open.ottawa.ca/datasets/covid-19-cases-and-deaths-in-ottawa/geoservice?page=2
"""

res = requests.get(
    'https://opendata.arcgis.com/datasets/6bfe7832017546e5b30c5cc6a201091b_0/FeatureServer/0/query?where=1%3D1&outFields=Date,Daily_Cases_by_Reported_Date,Total_Active_Cases_by_Date,Cumulative_Deaths_by_Date_of_Death,Cumulative_Cases_by_Episode_Date&outSR=4326&f=json'
)

data = json.loads(res.text)
features = data['features']


def daily_cases():
    current_day = features[-1]['attributes']
    day = datetime.datetime.fromtimestamp(current_day['Date'] / 1000.0)

    data = {}

    data['Date'] = day

    data['Daily Cases'] = current_day['Daily_Cases_by_Reported_Date']

    data['Total Active Cases'] = current_day['Total_Active_Cases_by_Date']

    data['Cumulative Deaths'] = current_day[
        'Cumulative_Deaths_by_Date_of_Death']

    data['Cumulative Cases'] = current_day['Cumulative_Cases_by_Episode_Date']

    return data
