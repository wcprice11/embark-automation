
class Page:
    def __init__(self, driver):
        self.driver = driver

    def title_is(self, text: str) -> bool:
        return self.driver.title == text

#################################
#...............................#
#....%%...%%..%%%%%%..%%%%%.....#
#....%%...%%..%%......%%..%%....#
#....%%.%.%%..%%%%....%%%%%.....#
#....%%%%%%%..%%......%%..%%....#
#.....%%.%%...%%%%%%..%%%%%.....#
#...............................#
#################################

#---PROD---#
class ProdBase(Page):
    pass

class ProdLogin(Page):
    pass

class ProdHome(Page):
    pass

class ProdResources(Page):
    pass

class ProdSearch(Page):
    pass

class ProdLanguageSettings(Page):
    pass

class ProdContactUs(Page):
    pass

class ProdTroubleShooting(Page):
    pass

"""class ProdAbout(Page):
    url = URLs.PROD_ABOUT
    back_button = 
    version
    copyright
    privacy_link
    Terms_of_use
    Acknowledgements
    feedback"""

    #pass

class Prod(Page):
    pass
class Prod(Page):
    pass
class Prod(Page):
    pass
class Prod(Page):
    pass

         
#---STAGE---#

#---RC---#

#---DEV---#


################################################
#..............................................#
#....%%%%%...%%%%%....%%%%...%%%%%%..%%%%%.....#
#....%%..%%..%%..%%..%%..%%....%%....%%..%%....#
#....%%..%%..%%%%%...%%..%%....%%....%%..%%....#
#....%%..%%..%%..%%..%%..%%....%%....%%..%%....#
#....%%%%%...%%..%%...%%%%...%%%%%%..%%%%%.....#
#..............................................#
################################################



################################
#..............................#
#....%%%%%%...%%%%....%%%%.....#
#......%%....%%..%%..%%........#
#......%%....%%..%%...%%%%.....#
#......%%....%%..%%......%%....#
#....%%%%%%...%%%%....%%%%.....#                       
#..............................#
################################

