from selenium.webdriver.common.by import By

class Elements:
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

    sign_in_button          = (By.CSS_SELECTOR , "#login-button")

    sign_in_username_field  = (By.CSS_SELECTOR , "#okta-signin-username")
    sign_in_next            = (By.CSS_SELECTOR , "#okta-signin-submit")
    sign_in_password_field  = (By.CSS_SELECTOR , "#input73")
    sign_in_submit          = (By.CSS_SELECTOR , "input[type=submit]")

    i_want_to_learn         = (By.CSS_SELECTOR , "#target-language-select")

    learn_english           = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(15)")
    learn_french            = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(19)")
    learn_korean            = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(32)")
    learn_spanish           = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(56)")
    learn_vietnamese        = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(65)")
    
    native_language         = (By.CSS_SELECTOR , "#native-language-select")

    native_english          = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(15)")
    native_french           = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(19)")
    native_korean           = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(32)")
    native_spanish          = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(56)")
    native_vietnamese       = (By.CSS_SELECTOR , "ng-dropdown-panel div.ng-option:nth-of-type(65)")

    language_submit         = (By.CSS_SELECTOR, "#add-language-submit")

    home_button             = (By.CSS_SELECTOR , "#tab-button-learn")
    resources_button        = (By.CSS_SELECTOR , "#tab-button-resources")
    search_button           = (By.CSS_SELECTOR , "#tab-button-search")
    settings_button         = (By.CSS_SELECTOR , "#tab-button-search + ion-tab-button")

    for_you_tab             = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(1)")
    basic_tab               = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(2)")
    prework_tab             = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(3)")
    daily_life_tab          = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(4)")
    PMG_lessons_tab         = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(5)")

    start_button            = (By.CSS_SELECTOR , "#start-btn")



    # = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(5)")


class ProdElements(Elements):
    pass

class StageElements(Elements):
    whats_new_card_close_button         = (By.CSS_SELECTOR , "ion-card ion-button:nth-of-type(1)")
    whats_new_card_learn_more_button    = (By.CSS_SELECTOR , "ion-card ion-button:nth-of-type(2)")

    my_added_phrases                    = (By.CSS_SELECTOR , "app-for-you-group > ion-card:nth-of-type(2)")

    added_phrase_group                  = (By.CSS_SELECTOR, "div.section:nth-of-type(2) p")
    embark_topics_view_all              = (By.CSS_SELECTOR, "div.section:nth-of-type(2) div.header button")
    
    log_out_button                      = (By.CSS_SELECTOR , "app-home-settings-popover ion-button")
    languages_button                    = (By.CSS_SELECTOR , "ion-item:nth-of-type(2)")
    sound_effects                       = (By.CSS_SELECTOR , "ion-item:nth-of-type(3)")
    sound_effects_toggle                = (By.CSS_SELECTOR , "ion-item:nth-of-type(3) ion-toggle")
    contact_us_button                   = (By.CSS_SELECTOR , "ion-item:nth-of-type(4)")
    troubleshooting_button              = (By.CSS_SELECTOR , "ion-item:nth-of-type(5)")
    whats_new_button                    = (By.CSS_SELECTOR , "ion-item:nth-of-type(6)")
    about_button                        = (By.CSS_SELECTOR , "ion-item:nth-of-type(7)")

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
