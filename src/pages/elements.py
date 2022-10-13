from selenium.webdriver.common.by import By

class Elements:
    #---HELPERS---#

    sign_in_button          = (By.CSS_SELECTOR , "#login-button", "sign in button")

    sign_in_username_field  = (By.CSS_SELECTOR , "#okta-signin-username", "username field (sign in)")
    sign_in_next            = (By.CSS_SELECTOR , "#okta-signin-submit", "next (sign in page)")
    sign_in_password_field  = (By.CSS_SELECTOR , "#input73", "password field (sign in)")
    sign_in_submit          = (By.CSS_SELECTOR , "input[type=submit]", "submit (sign in)")

    i_want_to_learn         = (By.CSS_SELECTOR , "#target-language-select input", "i want to learn dropdown menu")
    i_want_to_learn_close   = (By.CSS_SELECTOR , "#target-language-select span.ng-arrow", "collapse menu button")

    learn_english           = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(15)", "learn english")
    learn_french            = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(19)", "learn french")
    learn_korean            = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(32)", "learn korean")
    learn_spanish           = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(56)", "learn spanish")
    learn_vietnamese        = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(65)", "learn vietnamese")
    
    native_language         = (By.CSS_SELECTOR , "#native-language-select", "FIX_ME")

    native_english          = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(15)", "native english")
    native_french           = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(19)", "native french")
    native_korean           = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(32)", "native korean")
    native_spanish          = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(56)", "native spanish")
    native_vietnamese       = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(65)", "native vietnamese")

    language_submit         = (By.CSS_SELECTOR, "#add-language-submit", "Submit language-choose your adventure")

    home_button             = (By.CSS_SELECTOR , "#tab-button-learn", "Home tab")
    resources_button        = (By.CSS_SELECTOR , "#tab-button-resources", "Resources Button")
    search_button           = (By.CSS_SELECTOR , "#tab-button-search", "Search Button")
    settings_button         = (By.CSS_SELECTOR , "#tab-button-search + ion-tab-button", "Settings Button")

    for_you_tab             = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(1)", "FIX_ME")
    basic_tab               = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(2)", "FIX_ME")
    prework_tab             = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(3)", "FIX_ME")
    daily_life_tab          = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(4)", "FIX_ME")
    PMG_lessons_tab         = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(5)", "FIX_ME")

    start_button            = (By.CSS_SELECTOR , "#start-btn", "FIX_ME")

    # Settings dropdown menu
    loaded_language_subtext = (By.CSS_SELECTOR , "app-home-settings-popover p", "language listed in settings menu")

    tip_pop_up              = (By.CSS_SELECTOR , "div.tip-popover-box", "tip pop-up box")
    tip_pop_up_close        = (By.CSS_SELECTOR , "div.tip-popover-box ion-icon", "close pop-up button")

    lesson_1_heavenly_father= (By.CSS_SELECTOR , "app-task-card:nth-of-type(1)>ion-card", "Heavenly Father task in PMG lesson 1(og:spanish)")
    heavenly_father_listening=(By.CSS_SELECTOR , "app-lesson-card[iconname='listening']>ion-card", "listening task in Heavenly Father(og:spanish)")
    # = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(5)", "FIX_ME")
    basic_alphabet_card     = (By.CSS_SELECTOR , "app-task-card:nth-of-type(1)>ion-card ion-icon", "alphabet card in basic(og:korean)")
    first_card_in_alphabet  = (By.CSS_SELECTOR , "app-flashcard:nth-of-type(1)>ion-card h1", "first card in alphabet discover(og:korean)")

    spanish_resources_grammar=(By.CSS_SELECTOR , "app-lesson-collection-card:last-of-type>ion-card", "Grammar Lessons in resources(og:spanish)")
    spanish_grammar_articles= (By.CSS_SELECTOR , "ion-content>ion-card:nth-of-type(3)", "articles card in grammar lessons(og:spanish)")
    grammar_lesson_header   = (By.CSS_SELECTOR , "app-lesson ion-toolbar", "Header of grammar lesson(og:spanish-articles")
    spanish_resources_vocab = (By.CSS_SELECTOR , "div>ion-card:nth-of-type(9)", "Vocabulary and Phrases card(og:spanish)")
    resources_pray_often    = (By.CSS_SELECTOR , "ion-card:nth-of-type(24)", "Pray often in vocab in resources(og:spanish)")
    pdf_header_title        = (By.CSS_SELECTOR , "div.headerWrapper ion-title", "title in header of pdf viewer(og:spanish pray often)")



class ProdElements(Elements):
    pass

class StageElements(Elements):
    whats_new_card_close_button         = (By.CSS_SELECTOR , "ion-card ion-button:nth-of-type(1)", "FIX_ME")
    whats_new_card_learn_more_button    = (By.CSS_SELECTOR , "ion-card ion-button:nth-of-type(2)", "FIX_ME")
    my_added_phrases                    = (By.CSS_SELECTOR , "app-for-you-group > ion-card:nth-of-type(2)", "FIX_ME")

    added_phrase_group                  = (By.CSS_SELECTOR, "div.section:nth-of-type(2) p", "FIX_ME")
    embark_topics_view_all              = (By.CSS_SELECTOR, "div.section:nth-of-type(2) div.header button", "FIX_ME")
    
    log_out_button                      = (By.CSS_SELECTOR , "app-home-settings-popover ion-button", "FIX_ME")
    languages_button                    = (By.CSS_SELECTOR , "ion-item:nth-of-type(2)", "FIX_ME")
    sound_effects                       = (By.CSS_SELECTOR , "ion-item:nth-of-type(3)", "FIX_ME")
    sound_effects_toggle                = (By.CSS_SELECTOR , "ion-item:nth-of-type(3) ion-toggle", "FIX_ME")
    contact_us_button                   = (By.CSS_SELECTOR , "ion-item:nth-of-type(4)", "FIX_ME")
    troubleshooting_button              = (By.CSS_SELECTOR , "ion-item:nth-of-type(5)", "FIX_ME")
    whats_new_button                    = (By.CSS_SELECTOR , "ion-item:nth-of-type(6)", "FIX_ME")
    about_button                        = (By.CSS_SELECTOR , "ion-item:nth-of-type(7)", "FIX_ME")

    lesson_1_heavenly_father            = (By.CSS_SELECTOR , "div.learnTab__container:last-of-type>app-task-card:first-of-type>ion-card", "Heavenly Father task in PMG lesson 1(og:spanish)")
    heavenly_father_listening           = (By.CSS_SELECTOR , "app-study-list-card[iconname='listening']>ion-card", "listening task in Heavenly Father(og:spanish)")
    #---RC---#
class RCElements(Elements):
    pass
    #---DEV---#
class DevElements(Elements):
    pass

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


    # MISC
