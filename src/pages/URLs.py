#################################
#...............................#
#....%%...%%..%%%%%%..%%%%%.....#
#....%%...%%..%%......%%..%%....#
#....%%.%.%%..%%%%....%%%%%.....#
#....%%%%%%%..%%......%%..%%....#
#.....%%.%%...%%%%%%..%%%%%.....#
#...............................#
#################################

#---HELPERS---#
class URLs:
    common_urls = {
        "LOGIN":        "/#/login",
        "RESOURCES":    "/#/home/resources",
        "SEARCH":       "/#/home/search",
        "SETTINGS": "/#/home/settings",
        "LANGUAGES": "/#/home/settings/languages",
        "CONTACT_US": "/#/home/settings/contact-us",
        "TROUBLESHOOT": "/#/home/settings/troubleshoot",
        "ABOUT":            "/#/home/settings/about",
        "ACKNOWLEDGEMENTS": "/#/home/settings/acknowledgements",
        "BLANK_HOME":           "/#/home/learn",
        "HOME_PAGE":            "/#/home/learn?taskGroup=636000000",
        "BASIC":                "/#/home/learn?taskGroup=2",
        "PREWORK":              "/#/home/learn?taskGroup=152265",
        "DAILY_LIFE":           "/#/home/learn?taskGroup=4",
        "PMG_LESSONS":          "/#/home/learn?taskGroup=3",
        "FAVORITES":            "/#/home/tasks/635000000",
        "ALPHABET":             "/#/home/tasks/633000000/alphabet/discover",
        "MEET_SOMEONE":         "/#/home/tasks/5",
        "OFFER_A_PRAYER":       "/#/home/tasks/6",
        "TESTIFY":              "/#/home/tasks/7",
        "SHARE_A_SCRIPTURE":    "/#/home/tasks/9",
        "GIVE_AN_OVERVIEW":     "/#/home/tasks/10",
        "EXTEND_AN_INVITATION": "/#/home/tasks/8",
        "CLASSROOM_VOCABULARY": "/#/home/tasks/11",
        "ONBOARDING":           "/#/language-onboarding?redirectUrl=%2Fhome",
    }


class BasedURLs(URLs):
    def __init__(self, base) -> None:
        self.BASE = base
        for a in URLs.common_urls:
            self.__setattr__(a, self.BASE + URLs.common_urls[a])

ProdURLs = BasedURLs("https://tall.global/embark")
StageURLs = BasedURLs("https://stage.tall.global/embark")
RCURLs = BasedURLs("https://rc.tall.global/embark")
DevURLs = BasedURLs("https://dev.tall.global/embark")

# MISC

PRIVACY_POLICY = "https://www.churchofjesuschrist.org/services/platform/v3/resources/privacy-policy?lang=eng"
TERMS_OF_USE   = "https://www.churchofjesuschrist.org/services/platform/v3/resources/terms-of-use?lang=eng"
