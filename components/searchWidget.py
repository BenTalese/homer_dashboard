# ISSUE: Make sure autofocus isn't on the config.yml search bar, otherwise the autofocus will conflict
def getSearchWidget():    
    return  '<div class="tile is-child p-2 widget">'+\
                "<form id='search-form' action='https://www.google.com.au/search' method='get'>"+\
                    "<input name='q' id='search-bar' placeholder='Google for something...' type='text' autofocus />"+\
                    "<button id='search-button' type='submit'>"+\
                        "<i class='fa fa-search'></i>"+\
                    "</button>"+\
                "</form>"+\
            '</div>'