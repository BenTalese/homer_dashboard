import requests

def getSpeedWidget(url):
    speedTestData = None
    try:
        speedTestData = requests.get(url).json()
    except:
        print("Speed Test Tracker docker container is inaccessible because it is offline or it has errors.")

    if (speedTestData is not None):
        speedWidget =   '<div class="tile is-child widget">'+\
                                '<p class="widget-header title mb-1"><i class="fas fa-tachometer-alt fa-lg"></i>&ensp;Current Net Speed</p>'+\
                                '<div class="gauge-group">'+\
                                    '<div class="gauge-wrapper">'+\
                                        '<i class="fas fa-arrow-alt-circle-down fa-3x"></i>'+\
                                        '<div class="gauge">'+\
                                            '<div class="wheel-container">'+\
                                                '<div class="colour-wheel"></div>'+\
                                            '</div>'+\
                                            '<div class="needle" style="transform: rotate('+str(round(float(speedTestData['data']['download']),2)*1.8)+'deg)"></div>'+\
                                            '<div class="gauge-center">'+\
                                                '<div class="gauge-value">'+str(round(float(speedTestData['data']['download']),2))+'</div>'+\
                                                '<div class="gauge-label">Mb/s</div>'+\
                                            '</div>'+\
                                        '</div>'+\
                                    '</div>'+\
                                    '<div class="gauge-wrapper">'+\
                                        '<i class="fas fa-arrow-alt-circle-up fa-3x"></i>'+\
                                        '<div class="gauge">'+\
                                            '<div class="wheel-container">'+\
                                                '<div class="colour-wheel"></div>'+\
                                            '</div>'+\
                                            '<div class="needle" style="transform: rotate('+str(round(float(speedTestData['data']['upload']),2)*1.8)+'deg)"></div>'+\
                                            '<div class="gauge-center">'+\
                                                '<div class="gauge-value">'+str(round(float(speedTestData['data']['upload']),2))+'</div>'+\
                                                '<div class="gauge-label">Mb/s</div>'+\
                                            '</div>'+\
                                        '</div>'+\
                                    '</div>'+\
                                '</div>'+\
                                '<div class="ping-container">'+\
                                    '<p class="gauge-wrapper"><b>Ping: '+str(speedTestData['data']['ping'])+'ms</b></p>'+\
                                '</div>'+\
                            '</div>'

    return  '<div class="tile is-child widget">'+\
                '<p>speedWidget will go here</p>'+\
            '</div>'