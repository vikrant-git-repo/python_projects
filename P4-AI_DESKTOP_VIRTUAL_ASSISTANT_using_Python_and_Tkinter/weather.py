# from requests_html import HTMLSession
# # import speech_to_text

# s = HTMLSession()
# query = "hyderabad"
# url = f"https://www.google.com/search?q=weather+{query}"
# r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'}, verify=False)
# r.html.render(timeout=20)
# temp = r.html.find('span#wob_tm', first=True).text
# print(temp)
# unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
# print(unit)
# desc = r.html.find('span#wob_dc', first=True).text
# print(desc)

import requests

def weather():

    # Location to fetch weather for
    location = "hyderabad"
    # wttr.in API endpoint with JSON format
    url = f"https://wttr.in/{location}?format=j1"

    response = requests.get(url, verify=False)
    data = response.json()

    current = data['current_condition'][0]
    temperature = current['temp_C']
    description = current['weatherDesc'][0]['value']
    feels_like = current['FeelsLikeC']
    humidity = current['humidity']
    wind_speed = current['windspeedKmph']
    return temperature+" " + description+" " + feels_like+" " + humidity+" " + wind_speed+" "

