import feedparser
from random import randint

def getNewsWidget(rssUrl):
    feed = feedparser.parse(rssUrl)
    feedItem1 = feed.entries[randint(0, len(feed.entries)-1)]
    item1Title = feedItem1.title
    item1Date = feedItem1.published
    item1Summary = feedItem1.summary
    item1Link = feedItem1.link

    feedItem2 = feed.entries[randint(0, len(feed.entries)-1)]
    
    return  '<div class="tile is-child widget">'+\
                '<p class="widget-header title mb-1"><i class="fas fa-globe-europe fa-lg"></i>&ensp;World Headlines</p>'+\
                '<div class="widget-content">'+\
                    '<p><b>'+item1Title+'</b></p>'+\
                    '<p>'+item1Summary+'</p>'+\
                '</div>'+\
                '<div class="widget-footer">'+\
                    '<a href='+item1Link+'><b>Read More</b></a>'+\
                    '<p><b>Published</b>: '+str(item1Date)[5:16]+'</p>'+\
                '</div>'+\
            '</div>'