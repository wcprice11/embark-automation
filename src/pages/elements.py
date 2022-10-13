from selenium.webdriver.common.by import By

class Elements:
    #---HELPERS---#

    sign_in_button          = (By.CSS_SELECTOR , "#login-button", "sign in button")

    sign_in_username_field  = (By.CSS_SELECTOR , "#okta-signin-username", "username field (sign in)")
    sign_in_next            = (By.CSS_SELECTOR , "#okta-signin-submit", "next (sign in page)")
    sign_in_password_field  = (By.CSS_SELECTOR , "#input73", "password field (sign in)")
    sign_in_submit          = (By.CSS_SELECTOR , "input[type=submit]", "submit (sign in)")

    i_want_to_learn         = (By.CSS_SELECTOR , "#target-language-select", "FIX_ME")

    learn_english           = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(15)", "FIX_ME")
    learn_french            = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(19)", "FIX_ME")
    learn_korean            = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(32)", "FIX_ME")
    learn_spanish           = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(56)", "FIX_ME")
    learn_vietnamese        = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(65)", "FIX_ME")
    
    native_language         = (By.CSS_SELECTOR , "#native-language-select", "FIX_ME")

    native_english          = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(15)", "FIX_ME")
    native_french           = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(19)", "FIX_ME")
    native_korean           = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(32)", "FIX_ME")
    native_spanish          = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(56)", "FIX_ME")
    native_vietnamese       = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(65)", "FIX_ME")

    language_submit         = (By.CSS_SELECTOR, "#add-language-submit", "FIX_ME")

    home_button             = (By.CSS_SELECTOR , "#tab-button-learn", "FIX_ME")
    resources_button        = (By.CSS_SELECTOR , "#tab-button-resources", "FIX_ME")
    search_button           = (By.CSS_SELECTOR , "#tab-button-search", "FIX_ME")
    settings_button         = (By.CSS_SELECTOR , "#tab-button-search + ion-tab-button", "FIX_ME")

    for_you_tab             = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(1)", "FIX_ME")
    basic_tab               = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(2)", "FIX_ME")
    prework_tab             = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(3)", "FIX_ME")
    daily_life_tab          = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(4)", "FIX_ME")
    PMG_lessons_tab         = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(5)", "FIX_ME")

    start_button            = (By.CSS_SELECTOR , "#start-btn", "FIX_ME")



    # = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(5)", "FIX_ME")


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
