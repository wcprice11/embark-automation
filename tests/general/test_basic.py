from random import randint
from tests.embark_test_classes import EmbarkStageTest
from list_of_languages import languages

class TestAboutHyperlinks(EmbarkStageTest):
    def test_about_hyperlinks(self):
        # Basic Login
        e = self.elements
        lang = languages[randint(0, len(languages)-1)] # login with a random language
        self.login(lang)
        self.wait_for_element_to_be_clickable(e.whats_new_card_close_button)
        self.click(e.whats_new_card_close_button)

        # On Homepage
        self.validate_element_text( e.spaced_review_title,      "Spaced Review")
        self.find(                  e.level_number) # these finds would be better with a confirm "confirm text is not empty"
        self.validate_element_text( e.my_items_title,           "My Items")
        self.find(                  e.my_items_first_item)
        self.validate_element_text( e.recommended_title,        "Recommended")
        self.find(                  e.recommended_first_item)

        # Validate Tabs
        self.validate_element_text( e.basic_tab,                "Basic")
        self.click(                 e.basic_tab)

        # FIX ME: This will fail for non-new users need a branch to check if present
        self.wait_for_element_to_be_clickable( e.tip_pop_up_close)
        self.validate_element_text( e.tip_pop_up,               "Basic helps you learn common missionary tasks.") 
        self.click(                 e.tip_pop_up_close)
        self.find(                  e.basic_first_lesson_title)
        """ FIX ME
        # logo button goes home
        self.click(                 e.logo_button)
        self.wait_for_element_to_be_clickable(e.spaced_review)
        self.validate_element_text( e.spaced_review_title,      "Spaced Review")
        """

        # prework
        self.validate_element_text( e.prework_tab,              "Prework")
        self.click(                 e.prework_tab)
        self.wait_for_element_to_be_clickable( e.tip_pop_up_close)
        self.validate_element_text( e.tip_pop_up,               "Prework helps you prepare for conversation practice in your MTC class.") 
        self.click(                 e.tip_pop_up_close)
        self.validate_element_text( e.prework_first_group_title,"Building Genuine Relationships")
        self.find(                  e.prework_first_lesson)

        # for you tab goes home
        self.validate_element_text( e.for_you_tab,              "For You")
        self.click(                 e.for_you_tab)   
        self.wait_for_element_to_be_clickable( e.tip_pop_up_close)
        self.validate_element_text( e.tip_pop_up,               "For You has suggestions for what to work on next.") 
        self.click(                 e.tip_pop_up_close)
        self.validate_element_text( e.spaced_review_title,      "Spaced Review")

        # daily life
        self.validate_element_text( e.daily_life_tab,           "Daily Life")
        self.click(                 e.daily_life_tab)
        self.wait_for_element_to_be_clickable( e.tip_pop_up_close)
        self.validate_element_text( e.tip_pop_up,               "Daily Life has everyday words and phrases and extensions to Basics.") 
        self.click(                 e.tip_pop_up_close)
        self.validate_element_text( e.daily_life_first_group_title, "Common Vocabulary")

        # PMG Lessons
        self.validate_element_text( e.PMG_lessons_tab,          "PMG Lessons")
        self.click(                 e.PMG_lessons_tab)
        self.wait_for_element_to_be_clickable( e.tip_pop_up_close)
        self.validate_element_text( e.tip_pop_up,               "PMG Lessons help you prepare to teach gospel principles.") 
        self.click(                 e.tip_pop_up_close)
        self.validate_element_text( e.pmg_lessons_first_group_title, "Lesson 1")

        # Validate ribbon buttons

        # Resources
        self.validate_element_text( e.resources_button,         "Resources")
        self.click(                 e.resources_button)
        self.wait_for_element_to_be_clickable( e.tip_pop_up_close)
        self.validate_element_text( e.tip_pop_up,               "Resources is a library of video, audio, and PDF collections to help you with language learning.") 
        self.click(                 e.tip_pop_up_close)
        self.validate_element_text( e.resources_title,          "Resources")
        self.validate_element_text( e.resources_embark_title,   "How to Use Embark")

        # home button goes home
        self.validate_element_text( e.home_button,              "Home")
        self.click(                 e.home_button)
        self.wait_for_element_to_be_clickable(e.pmg_lessons_first_group_title)

        # Search
        self.validate_element_text( e.search_button,            "Search")
        self.click(                 e.search_button)
        self.wait_for_element_to_be_clickable( e.tip_pop_up_close)
        self.validate_element_text( e.tip_pop_up,               "Search empowers you to find specific words, phrases, and resources.") 
        self.click(                 e.tip_pop_up_close)
        self.validate_element_text( e.search_page_words_tab, "Words")
        self.validate_element_text( e.search_page_phrases_tab, "Phrases")
        self.validate_element_text( e.search_page_resources_tab, "Resources")
        self.fill(                  e.search_bar, "Jesus", enter=True)
        self.wait_for_element_to_be_clickable(e.search_first_result)
        self.fill(                  e.search_bar, "Hi Embark team!!", enter=True)
        self.wait_for_text_in_element(e.search_no_results_message, "No matches found.")

        # Settings
        self.validate_element_text( e.settings_button,  "Settings")
        self.click(                 e.settings_button)
        self.wait_for_element_to_be_clickable(e.log_out_button)
        self.validate_element_text( e.log_out_button, "Log out")
        # FIX ME usernames with consistent names? or add a contains method
        # self.validate_element_text( e.settings_username, self.user.username)
        # FIX ME general search for whatever language is loaded.
        # self.validate_element_text( e.loaded_language_subtext, "") 
        self.validate_element_text( e.languages_button, "Languages")
        self.validate_element_text( e.sound_effects, "Sound effects")
        self.validate_element_text( e.contact_us_button, "Contact us")
        self.validate_element_text( e.troubleshooting_button, "Troubleshooting")
        self.validate_element_text( e.whats_new_button, "What's new?")
        self.validate_element_text( e.about_button, "About")

        # Logout
        self.click(                 e.log_out_button)
        self.wait_for_text_in_url( "churchofjesuschrist.org")

