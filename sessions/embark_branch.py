import pages.page
import pages.URLs as URLs
import pages.elements as elements

class Branch:
    def __init__(self, urls, pages, elements) -> None:
        self.urls = urls
        self.pages = pages
        self.elements = elements


web_prod = Branch(URLs.ProdURLs, pages.page, elements.ProdElements)
web_stage = Branch(URLs.StageURLs, pages.page, elements.StageElements)
web_rc = Branch(URLs.RCURLs, pages.page, elements.RCElements)
web_dev = Branch(URLs.DevURLs, pages.page, elements.DevElements)

