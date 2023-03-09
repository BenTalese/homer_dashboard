import requests

def getSystemWidget(glancesUrl, qbUrl):

    qbResponse = requests.get(qbUrl).json()

    cpu = requests.get(glancesUrl+"/cpu").json()
    mem = requests.get(glancesUrl+"/mem").json()
    memSwap = requests.get(glancesUrl+"/memswap").json()
    upTime = requests.get(glancesUrl+"/uptime").json()
    disk = requests.get(glancesUrl+"/fs").json()
    system = requests.get(glancesUrl+"/system").json()
    sensors = requests.get(glancesUrl+"/sensors").json()
    proc = requests.get(glancesUrl+"/processcount").json()

    return  '<div class="tile widget">'+\
                '<div class="tile is-parent is-12">'+\
                    '<div class="tile is-child">'+\
                        '<p class="widget-header title mb-1"><i class="fas fa-robot fa-lg"></i>&ensp;System Activity</p>'+\
                    '</div>'+\
                '</div>'+\
                '<div class="tile is-parent is-12">'+\
                    '<div class="tile is-child sys-box">'+\
                        '1'+\
                    '</div>'+\
                    '<div class="tile is-child sys-box">'+\
                        '2'+\
                    '</div>'+\
                    '<div class="tile is-child sys-box">'+\
                        '3'+\
                    '</div>'+\
                    '<div class="tile is-child sys-box">'+\
                        '4'+\
                    '</div>'+\
                '</div>'+\
            '</div>'