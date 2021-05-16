import requests
import datetime

def nextbus():
    date=datetime.datetime.today().strftime('%Y%m%d') 


    url='https://futar.bkk.hu/api/query/v1/ws/otp/api/where/schedule-for-stop.json?'
    paramteres={'key':'apaiary-test'
            ,'version':'3'
            ,'appVersion':'apiary-1.0'
            ,'includeReferences':'true'
            ,'stopId':'BKK_F03557'
            ,'onlyDepartures':'true'
            ,'date':date}

    data=requests.get(url, params=paramteres).json()

    for i in data['data']['entry']['schedules'][0]['directions'][0]['stopTimes']:
        if datetime.datetime.fromtimestamp(i['departureTime']) < datetime.datetime.today():
            continue
        else:
            print(datetime.datetime.fromtimestamp(i['departureTime']))
            break