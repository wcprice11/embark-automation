import pages.page
import pages.URLs as URLs

class Branch:
    def __init__(self, urls, pages) -> None:
        self.urls = urls
        self.pages = pages


web_prod = Branch(URLs.ProdURLs, pages.page)
web_stage = Branch(URLs.StageURLs, pages.page)
web_rc = Branch(URLs.RCURLs, pages.page)
web_dev = Branch(URLs.DevURLs, pages.page)

