import unittest
from sessions import embark_session


class TestStageRegPhrases(unittest.TestCase):
    def setUp(self) -> None:
        self.session = embark_session.webStageSession
        # get to the home page.
        return super().setUp()
    
    def add_phrase(self):
        s = self.session
        s.click(E.my_added_phrases)
        s.find(E.embark_topics_view_all)
        assert(len(s.driver.find_elements("CSS", "div.section:nth-of-type(2) p")) == 0)
        s.get(URLs.STAGE_HOME_PAGE)
        # s.click(MeetSomeone)
        # s.click(Phrases)
        # s.click(AddPhrase)
        # s.fill(Spanish, "My Spanish Phrase")
        # s.fill(English, "My English Phrase")
        # s.goto(home)
        s.click(E.my_added_phrases)
        # s.click(meetSomeone)
        # assert("My Spanish Phrase"==present)
        # assert("My English Phrase"==present)


    def remove_phrase(self):
        pass

    def tearDown(self) -> None:
        self.session.save_screenshot(f"a{self.id()}.png")
        return super().tearDown()
