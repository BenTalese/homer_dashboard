import flask
from flask import jsonify
from components import weatherWidget
from components import newsWidget
from components import systemWidget
from components import searchWidget
from components import galleryWidget
from components import speedWidget

app = flask.Flask(__name__)
app.config["DEBUG"] = False

in_development = True

####-----------URL CONFIGURATION-------------####
if (in_development):
    apiHostIP = "localhost" # this used to be 192.168.1.117, but after trying to access the script via reverse proxy...it didn't work...so somehow localhost and 192.168.1.117 (NAS IP) are different...
    apiHostPort = 9080
    qbURL = "http://192.168.1.117:4883/api/v2/transfer/info"
    rssUrl = "http://feeds.bbci.co.uk/news/world/rss.xml"
    glancesURL = "http://192.168.1.117:61208/api/3"
    speedTestURL = "http://192.168.1.117:5775/api/speedtest/latest"
else:
    apiHostIP = "localhost" # might end up being 192.168.1.117, or it might be 127.0.0.1
    apiHostPort = 9080
    qbURL = "http://localhost:4883/api/v2/transfer/info"
    rssUrl = "http://feeds.bbci.co.uk/news/world/rss.xml"
    glancesURL = "http://localhost:61208/api/3"
    speedTestURL = "http://localhost:5775/api/speedtest/latest"
####-----------URL CONFIGURATION-------------####

@app.route('/', methods=['GET'])
def home():
    return '''Use /stats to get all readings'''

@app.route('/stats', methods=['GET'])
def stats():
    layout =    '<div class="tile is-ancestor">'+\
                    '<div class="tile is-7 is-vertical column">'+\
                        weatherWidget.getWeatherWidget()+\
                        systemWidget.getSystemWidget(glancesURL, qbURL)+\
                    '</div>'+\
                    '<div class="tile is-5 is-parent is-vertical column">'+\
                        speedWidget.getSpeedWidget(speedTestURL)+\
                        galleryWidget.getGalleryWidget()+\
                        newsWidget.getNewsWidget(rssUrl)+\
                    '</div>'+\
                    '<div class="tile is-parent">'+\
                        searchWidget.getSearchWidget()+\
                    '</div>'+\
                '</div>'\

    data = { 'content': layout }
    response = jsonify(data) 
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

app.run (host = apiHostIP, port = apiHostPort)