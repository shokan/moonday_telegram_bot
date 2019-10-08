import pandas as pd
import requests as req
import datetime as dt
import telegram
import secret

api_url='https://api.worldweatheronline.com/premium/v1/weather.ashx?q=Astana&num_of_days=2&key={}&format=json&date=tomorrow'.format(secret.tokens['weather_api'])
bot = telegram.Bot(token=secret.tokens['telegram'])

resp = req.get(api_url)
data = resp.json()
tomorrow_date = data['data']['weather'][0]['date']

maxtempC = data['data']['weather'][0]['maxtempC']
mintempC = data['data']['weather'][0]['mintempC']
totalSnow_cm = data['data']['weather'][0]['totalSnow_cm']

sunrise = data['data']['weather'][0]['astronomy'][0]['sunrise']
sunset = data['data']['weather'][0]['astronomy'][0]['sunset']
moon_phase = data['data']['weather'][0]['astronomy'][0]['moon_phase']

def phase_translate(ph):
    phases = {'New Moon': 'Новолуние', 'Waxing Crescent': 'Молодая луна ', 'First Quarter': 'Первая четверть', 'Waxing Gibbous': 'Прибывающая луна', 'Full Moon': 'Полнолуние', 'Waning Gibbous': 'Убывающая луна', 'Last Quarter': 'Последняя четверть ', 'Waning Crescent': 'Старая луна'}
    return phases[ph]

messege_text = """Привет! Завтра ({}) температура воздуха будет колебаться от {} С до {} С. Время заката в {} время восхода в {}. Фаза луны: {}.""".format(tomorrow_date, mintempC, maxtempC, sunrise, sunset, phase_translate(moon_phase))

bot.send_message(chat_id='@AhimsaInfo', text=messege_text)