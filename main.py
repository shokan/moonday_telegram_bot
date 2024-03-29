# -*- coding: utf-8 -*-
import pandas as pd
import requests as req
import datetime as dt
import telegram
import secret
import sutras

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
    phases = {'New Moon': 'Новолуние', 'Waxing Crescent': 'Молодая луна ', 'First Quarter': 'Первая четверть', 'Waxing Gibbous': 'Растущая Луна', 'Full Moon': 'Полнолуние', 'Waning Gibbous': 'Убывающая луна', 'Last Quarter': 'Последняя четверть ', 'Waning Crescent': 'Старая луна'}
    return phases[ph]

def next_holiday():
    dateparse = lambda x: pd.datetime.strptime(x, '%d.%m.%Y')
    df = pd.read_csv("ashanga_holidays_2019_2020.csv", header=0, index_col=False, parse_dates=[0], date_parser=dateparse)
    d = dt.date.today()
    for i in df.mdate:
        if i.date()<d:
            pass
        else:
            next_day = i.date()
            delta = next_day - d
            break
    print('{} - {}'.format(next_day, delta))
    if delta.days == 0:
        next_text = ''
    elif delta.days == 1:
        next_text = 'Завтра отдыхаем! Высыпаемся и наслаждаемся круасанами ;)'
    elif  delta.days in (2, 3, 4):
        next_text = 'Следующий лунный день через {} дня'.format(delta.days)
    else:
        next_text = 'Следующий лунный день через {} дней'.format(delta.days)
    return next_text

messege_text = """Привет! Завтра ({}) температура воздуха в Астане будет колебаться от {} С до {} С. Время восхода в {} время заката в {}. Фаза луны: {}. {}""".format(tomorrow_date, mintempC, maxtempC, sunrise, sunset, phase_translate(moon_phase), next_holiday())
# print(messege_text)
bot.send_message(chat_id='@AhimsaInfo', text=messege_text)
bot.send_message(chat_id='@AhimsaInfo', text=sutras.s)