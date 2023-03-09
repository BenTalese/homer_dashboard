from datetime import datetime, timedelta
import json
import os

def getHourWeatherTile(data, index):
    return  '<div class="tile is-child weather-tile">'+\
                '<p>' + data[index]['time'] + '</p>'+\
                '<img class="weather-icon" width="50" src="http://openweathermap.org/img/wn/' + data[index]['icon'] + '@2x.png">'+\
                '<div id="main">'+\
                '</div>'+\
                '<div id="show">'+\
                    '<p>Humidity: ' + data[index]['humidity'] + '</p>'+\
                    '<p>Wind: <i class="fa fa-arrow-left" style="transform: rotate('+str(data[index]['wind_deg'])+'deg)"></i>' + ' ' + data[index]['wind_speed'] + '</p>'+\
                    '<p>Visibility: ' + data[index]['vis'] + '</p>'+\
                '</div>'+\
                '<div id="hide">'+\
                    '<p>' + data[index]['temp'] + '&deg;C</p>'+\
                    '<p>' + data[index]['summary'] + '</p>'+\
                    '<p>Rain: ' + data[index]['rain_vol'] + ' / ' + data[index]['rain_prob'] + '</p>'+\
                '</div>'+\
            '</div>'

def getDayWeatherTile(data, index):
    return  '<div class="tile is-child weather-tile">'+\
                '<p>' + (data[index]['day_of_week'] if datetime.strptime(data[index]['date'], '%Y-%m-%d').date() > datetime.now().date() else 'Today') + '</p>'+\
                '<img class="weather-icon" width="50" src="http://openweathermap.org/img/wn/' + data[index]['icon_day'] + '@2x.png">'+\
                '<div id="main">'+\
                '</div>'+\
                '<div id="show">'+\
                    '<p>Humidity: ' + data[index]['humidity_avg'] + '</p>'+\
                    '<p>Wind Speed: ' + data[index]['wind_speed_avg'] + '</p>'+\
                    '<p>Visibility: ' + data[index]['vis_avg'] + '</p>'+\
                '</div>'+\
                '<div id="hide">'+\
                    '<span class="high-temp">' + data[index]['temp_max'] + '&deg;C</span> / <span class="low-temp">' + data[index]['temp_min'] + '&deg;C</span>'+\
                    '<p>' + data[index]['summary'] + '</p>'+\
                    '<p>Chance of Rain: ' + data[index]['rain_prob_avg'] + '</p>'+\
                    '<p>Rainfall: ' + data[index]['rain_vol_total'] + '</p>'+\
                '</div>'+\
            '</div>'

def getMainWeatherTile(data, index):
    return  '<div class="tile is-child weather-tile">'+\
                '<p>Now</p>'+\
                '<img class="weather-icon" width="'+bigIconSize+'" src="http://openweathermap.org/img/wn/' + data[index]['icon'] + '@2x.png">'+\
                '<div id="main">'+\
                '</div>'+\
                '<div id="show">'+\
                    '<p>Feels Like: ' + data[index]['feels_like'] + '&deg;C</p>'+\
                    '<p>Chance of Rain: ' + data[index]['rain_prob'] + '</p>'+\
                    '<p>Rain Volume: ' + data[index]['rain_vol'] + '</p>'+\
                    '<p>Humidity: ' + data[index]['humidity'] + '</p>'+\
                    '<p>Wind: <i class="fa fa-arrow-left" style="transform: rotate('+str(data[index]['wind_deg'])+'deg)"></i>' + ' ' + data[index]['wind_speed'] + '</p>'+\
                    '<p>Clouds: ' + data[index]['clouds'] + '</p>'+\
                    '<p>Visibility: ' + data[index]['vis'] + '</p>'+\
                '</div>'+\
                '<div id="hide">'+\
                    '<p>' + data[index]['temp'] + '&deg;C</p>'+\
                    '<span class="high-temp">' + data['day-0']['temp_max'] + '&deg;C</span> / <span class="low-temp">' + data['day-0']['temp_min'] + '&deg;C</span>'+\
                    '<p>' + data[index]['summary'] + '</p>'+\
                    '<p>' + data[index]['detail'] + '</p>'+\
                '</div>'+\
            '</div>'

bigIconSize = '100'

# The IF is here to prevent the working directory changing every time a request comes into the dashboard
if 'homer-api.py' not in os.listdir():
    os.chdir('../volume2/docker/homer')

weatherData = json.load(open('weather.json'))
day0 = datetime.strptime(weatherData['day-0']['date'], '%Y-%m-%d')
day1 = datetime.strptime(weatherData['day-1']['date'], '%Y-%m-%d')
day2 = datetime.strptime(weatherData['day-2']['date'], '%Y-%m-%d')
day3 = datetime.strptime(weatherData['day-3']['date'], '%Y-%m-%d')
day4 = datetime.strptime(weatherData['day-4']['date'], '%Y-%m-%d')

currentHour = datetime.now().hour
hourIdx = 0
while hourIdx < currentHour and hourIdx < 21:
    hourIdx += 3

today = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hourIdx)

tile0Idx = str(today.date()) + "-" + str(today.hour).zfill(2)

today = today + timedelta(hours=3)
tile1Idx = str(today.date()) + "-" + str(today.hour).zfill(2)

today = today + timedelta(hours=3)
tile2Idx = str(today.date()) + "-" + str(today.hour).zfill(2)

today = today + timedelta(hours=3)
tile3Idx = str(today.date()) + "-" + str(today.hour).zfill(2)

today = today + timedelta(hours=3)
tile4Idx = str(today.date()) + "-" + str(today.hour).zfill(2)

def getWeatherWidget():
    return  '<div class="tile is-vertical widget">'+\
                '<div class="tile is-parent">'+\
                    '<div class="tile is-child">'+\
                        '<p class="widget-header title"><i class="fas fa-cloud-sun-rain fa-lg"></i>&ensp;Weather</p>'+\
                    '</div>'+\
                '</div>'+\
                '<div class="tile">'+\
                    '<div class="tile is-parent is-3">'+\
                        getMainWeatherTile(weatherData, tile0Idx)+\
                    '</div>'+\
                    '<div class="tile is-9 is-vertical">'+\
                        '<div class="tile is-parent">'+\
                            getHourWeatherTile(weatherData, tile1Idx)+\
                            getHourWeatherTile(weatherData, tile2Idx)+\
                            getHourWeatherTile(weatherData, tile3Idx)+\
                            getHourWeatherTile(weatherData, tile4Idx)+\
                        '</div>'+\
                        '<div class="tile is-parent">'+\
                            getDayWeatherTile(weatherData, 'day-0')+\
                            getDayWeatherTile(weatherData, 'day-1')+\
                            getDayWeatherTile(weatherData, 'day-2')+\
                            getDayWeatherTile(weatherData, 'day-3')+\
                        '</div>'+\
                    '</div>'+\
                '</div>'+\
                '<div class="widget-footer">'+\
                    '<p><b>Last Updated:</b> '+weatherData['other']['last_updated']+'</p>'+\
                '</div>'+\
            '</div>'