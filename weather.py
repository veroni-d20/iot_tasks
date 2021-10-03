import json
import urllib.request as request

def weatherInfo():
    weatherUrl="http://dataservice.accuweather.com/forecasts/v1/daily/1day/206671?apikey=Y89KvqQD9p7lP5cBuSURERSqbSyObcAT&details=true"
    with request.urlopen(weatherUrl) as weatherdata:
        data = json.loads(weatherdata.read().decode())["DailyForecasts"][0]
        Temperature_data = str(data["Temperature"]["Maximum"]["Value"]) + data["Temperature"]["Maximum"]["Unit"]
        Description = str(data["Day"]["ShortPhrase"])
        Wind_data = str(data["Day"]["Wind"]["Speed"]["Value"])+data["Day"]["Wind"]["Speed"]["Unit"]
        
    print("Temperature: ",Temperature_data)
    print("Description: ",Description)
    print("Wind Speed: ",Wind_data)
    
weatherInfo()