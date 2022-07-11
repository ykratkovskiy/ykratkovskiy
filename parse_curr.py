import requests

url_usd = 'https://www.nbrb.by/api/exrates/rates/431'

r = requests.get(url_usd)

usd = r.json()

usd_rate = usd.get('Cur_OfficialRate')
req_date = usd.get('Date')
curr_name = usd.get('Cur_Name')

print (f'Курс {curr_name} на {req_date} равен {usd_rate} руб.')