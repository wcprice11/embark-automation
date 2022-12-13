from selenium.webdriver.common.by import By
from selenium import webdriver

"""
Creating a new element requires a couple things:
- A unique name
- A selection scheme (By.CSS_SELECTOR, unless there is a serious issue) 
- The selection string ("div.titleClass>span")
- And a quick description that will appear in error messages. (include context to how you chose the selector "level number (og:P-Sp homepage)"

I'm trying to start using the shorthand of Branch-Language in the context notes. "S-kor" would be Stage-Korean.
"""


class Elements:

    sign_in_button          = (By.CSS_SELECTOR, "#login-button", "sign in button")
    # Church of Jesus Christ authentication page
    sign_in_username_field  = (By.CSS_SELECTOR, "#okta-signin-username", "username field (sign in)")
    sign_in_next            = (By.CSS_SELECTOR, "#okta-signin-submit", "next (sign in page)")
    too_many_attempts_message=(By.CSS_SELECTOR, "div.o-form-has-errors", "too many requests error")
    sign_in_password_field  = (By.CSS_SELECTOR, "#input73", "password field (sign in)")
    sign_in_submit          = (By.CSS_SELECTOR, "input[type=submit]", "submit (sign in)")

    # language selection
    i_want_to_learn         = (By.CSS_SELECTOR, "#target-language-select input", "i want to learn dropdown menu")
    i_want_to_learn_close   = (By.CSS_SELECTOR, "#target-language-select span.ng-arrow", "collapse menu button")
    learn_english           = (By.CSS_SELECTOR, "ng-dropdown-panel div.ng-option:nth-of-type(15)", "learn english")
    learn_french            = (By.CSS_SELECTOR, "ng-dropdown-panel div.ng-option:nth-of-type(19)", "learn french")
    learn_japanese          = (By.CSS_SELECTOR, "ng-dropdown-panel div.ng-option:nth-of-type(30)", "learn french")
    learn_korean            = (By.CSS_SELECTOR, "ng-dropdown-panel div.ng-option:nth-of-type(32)", "learn korean")
    learn_polish            = (By.CSS_SELECTOR, "ng-dropdown-panel div.ng-option:nth-of-type(45)", "learn polish")
    learn_spanish           = (By.CSS_SELECTOR, "ng-dropdown-panel div.ng-option:nth-of-type(56)", "learn spanish")
    learn_vietnamese        = (By.CSS_SELECTOR, "ng-dropdown-panel div.ng-option:nth-of-type(65)", "learn vietnamese")
    native_language         = (By.CSS_SELECTOR, "#native-language-select", "FIX_ME")
    native_english          = (By.CSS_SELECTOR, "ng-dropdown-panel div.ng-option:nth-of-type(15)", "native english")
    native_french           = (By.CSS_SELECTOR, "ng-dropdown-panel div.ng-option:nth-of-type(19)", "native french")
    native_korean           = (By.CSS_SELECTOR, "ng-dropdown-panel div.ng-option:nth-of-type(32)", "native korean")
    native_spanish          = (By.CSS_SELECTOR, "ng-dropdown-panel div.ng-option:nth-of-type(56)", "native spanish")
    native_vietnamese       = (By.CSS_SELECTOR, "ng-dropdown-panel div.ng-option:nth-of-type(65)", "native vietnamese")
    language_submit         = (By.CSS_SELECTOR, "#add-language-submit", "Submit language-choose your adventure")

    # Home page
    logo_button             = (By.CSS_SELECTOR, "ion-tab-bar>ion-img", "embark logo button (og:S-spanish homepage")
    home_button             = (By.CSS_SELECTOR, "#tab-button-learn", "ribbon home button")
    resources_button        = (By.CSS_SELECTOR, "#tab-button-resources", "Resources Button")
    search_button           = (By.CSS_SELECTOR, "#tab-button-search", "Search Button")
    settings_button         = (By.CSS_SELECTOR, "#tab-button-search + ion-tab-button", "Settings Button")
    for_you_tab             = (By.CSS_SELECTOR, "ion-segment-button:nth-of-type(1)", "FIX_ME")
    basic_tab               = (By.CSS_SELECTOR, "ion-segment-button:nth-of-type(2)", "FIX_ME")
    prework_tab             = (By.CSS_SELECTOR, "ion-segment-button:nth-of-type(3)", "FIX_ME")
    daily_life_tab          = (By.CSS_SELECTOR, "ion-segment-button:nth-of-type(4)", "FIX_ME")
    PMG_lessons_tab         = (By.CSS_SELECTOR, "ion-segment-button:nth-of-type(5)", "FIX_ME")
    alphabet_progress_bar   = (By.CSS_SELECTOR, "app-home-learn-tab>div>div>app-for-you-group>app-task-card:nth-of-type(3)>ion-card>div>div>div:nth-of-type(2)>progress", "Progress bar on alphabet card in home learn")
    alphabet_progress_secondary_language    = (By.CSS_SELECTOR, "app-home-learn-tab>div>div>app-for-you-group>app-task-card:nth-of-type(2)>ion-card>div>div>div:nth-of-type(2)>progress", "Progress bar on alphabet card in home learn when you've switched languages")
    my_added_words          = (By.CSS_SELECTOR, "app-for-you-group>div>ion-card", "Added words button on home page")


    spaced_review           = (By.CSS_SELECTOR, "app-spaced-review-card ion-card", "spaced review dashboard (og: spanish homepage)")
    spaced_review_title     = (By.CSS_SELECTOR, "app-spaced-review-card ion-card>div.title", "spaced review dashboard title (og: spanish homepage)")
    spaced_review           = (By.CSS_SELECTOR, "app-spaced-review-card ion-card>div.title", "'My items' title (og: spanish homepage)")
    level_number            = (By.CSS_SELECTOR, "span#level-number", "level number (og: spanish homepage)")
    spaced_review_button    = (By.CSS_SELECTOR, "app-spaced-review-card button", "spaced review start button (og: spanish homepage)")
    my_items_title          = (By.CSS_SELECTOR, "app-for-you-group>div.my-items>h1", "'My items' title (og: spanish homepage)")
    my_items_group          = (By.CSS_SELECTOR, "app-for-you-group>div.my-items>ion-card", "'My items' cards --selects multiple-- (og: spanish homepage)")
    my_items_first_item     = (By.CSS_SELECTOR, "app-for-you-group>div.my-items>ion-card:nth-of-type(1)", "First 'My items' card (og: spanish homepage)")
    recommended_title       = (By.CSS_SELECTOR, "app-for-you-group>h1", "Recommended title (og: spanish homepage)")
    recommended_group       = (By.CSS_SELECTOR, "app-for-you-group>app-task-card>ion-card", "Recommended items cards --selects multiple-- (og: spanish homepage)")
    recommended_first_item  = (By.CSS_SELECTOR, "app-for-you-group>app-task-card:nth-of-type(1)>ion-card", "First Recommended item card (og: spanish homepage)")
    

    whats_new_card_close_button         = (By.CSS_SELECTOR , "ion-card ion-button:nth-of-type(1)", "FIX_ME")
    whats_new_card_learn_more_button    = (By.CSS_SELECTOR , "ion-card ion-button:nth-of-type(2)", "FIX_ME")

    recommended_alphabet_lesson         = (By.CSS_SELECTOR, "app-for-you-group>app-task-card:nth-of-type(3)>ion-card", "recommended alphabet lesson (og:spanish")
    recommended_alphabet_lesson_title   = (By.CSS_SELECTOR, "app-for-you-group>app-task-card:nth-of-type(3)>ion-card span.title", "recommended alphabet lesson (og:spanish")
    recommended_tones_lesson            = (By.CSS_SELECTOR, "app-for-you-group ion-card:has(div.tones-icon) span.title", "tones lesson (og:mandarin(traditional)")

    recommended_meet_someone_lesson     = (By.CSS_SELECTOR, "app-for-you-group>app-task-card:nth-of-type(4)>ion-card", "recommended meet someone lesson (og:spanish")

    # Generic elements, may exist on any page
    body                    = (By.CSS_SELECTOR, "body", "page body, good for simulating key presses")
    start_button            = (By.CSS_SELECTOR, "ion-footer>ion-button", "FIX_ME")
    page_title              = (By.CSS_SELECTOR, "div#title", "Page title")
    error_message           = (By.CSS_SELECTOR, "h1", "error message (og: 503 server error page)")
    main_header             = (By.CSS_SELECTOR, "h1", "main header (og: choose your adventure screen)")
    # back_button             = (By.CSS_SELECTOR, "ion-icon[title='Back Arrow']", "Back Arrow (og: spanish alphabet lesson")
    back_button             = (By.CSS_SELECTOR, "ion-icon[src='assets/icon/arrow-left.svg']", "Back Arrow (og: spanish alphabet lesson")
    lesson_section_title    = (By.CSS_SELECTOR, "h3.task__section-title", "Section title (og: spanish alphabet lesson")
    lesson_card             = (By.CSS_SELECTOR, "app-study-list-card>ion-card", "lesson card item (og: spanish alphabet Symbols and Sounds")
    close_button            = (By.CSS_SELECTOR, "#close", "Close button in activity (og: spanish alphabet flashcards")
    close_popover           = (By.CSS_SELECTOR, "ion-popover", "close popover")
    task_page_back_button   = (By.CSS_SELECTOR, "app-task-study-list>app-header>div>ion-header>ion-toolbar>div>ion-grid>ion-row>ion-col>div>ion-icon", "back button on task page")

    # Added words items
    add_topic                           = (By.CSS_SELECTOR, "app-added-words>div>ion-content>div>div>div>div>div>div>button", "Add topic button")
    add_topic_title                     = (By.CSS_SELECTOR, "app-edit-added-words>ion-content>ion-grid>ion-card>app-text-box-suggestions>div>div:nth-of-type(2)>input", "Add topic title input")
    add_topic_add_word_native           = (By.CSS_SELECTOR, "app-edit-added-words>ion-content>ion-grid>ion-card>div>app-added-word-inputs>div>div>div>app-text-box-suggestions>div>div:nth-of-type(2)>input", "Add topic native word input")
    add_topic_add_word_target           = (By.CSS_SELECTOR, "app-edit-added-words>ion-content>ion-grid>ion-card>div>app-added-word-inputs>div>div>div>app-text-box-suggestions:nth-of-type(2)>div>div:nth-of-type(2)>input", "Add topic target language word input")
    add_topic_done_button               = (By.CSS_SELECTOR, "app-edit-added-words>div>ion-header>ion-toolbar>ion-buttons:nth-of-type(2)>button", "Add topic done button")
    added_topic_task_page_back_button   = (By.CSS_SELECTOR, "app-task-study-list>app-header>div>ion-header>ion-toolbar>div>ion-grid>ion-row>ion-col>div>ion-icon", "Back button in added topic task")
    added_words_edit                    = (By.CSS_SELECTOR, "app-added-words>div>ion-content>div>div>div>div>div>div:nth-of-type(2)>button:nth-of-type(2)", "Edit button added words")
    added_words_delete                  = (By.CSS_SELECTOR, "app-added-words>div>ion-content>div>div>div>div>div:nth-of-type(2)>div>div>div>app-topic-slider>div>div:nth-of-type(2)>div>ion-icon", "Delete button added words")
    added_words_confirm_delete          = (By.CSS_SELECTOR, "button[id='confirm-button']", "Confirm delete topic on popover")
    added_topics_absent_text            = (By.CSS_SELECTOR, "app-added-words>div>ion-content>div>div>div>div>div:nth-of-type(2)", "Area indicating if there are no added topics")

    # Settings dropdown menu
    settings_username                       = (By.CSS_SELECTOR, "app-home-settings-popover ion-item:first-of-type h5", "Settings dropdown username (og:S-span)")
    log_out_button                          = (By.CSS_SELECTOR , "app-home-settings-popover ion-button", "settings menu logout button")
    languages_button                        = (By.CSS_SELECTOR , "app-home-settings-popover ion-item:nth-of-type(2) h5", "FIX_ME")
    sound_effects                           = (By.CSS_SELECTOR , "ion-item:nth-of-type(3)", "FIX_ME")
    sound_effects_toggle                    = (By.CSS_SELECTOR , "ion-item:nth-of-type(3) ion-toggle", "FIX_ME")
    contact_us_button                       = (By.CSS_SELECTOR , "ion-item:nth-of-type(4)", "FIX_ME")
    troubleshooting_button                  = (By.CSS_SELECTOR , "ion-item:nth-of-type(5)", "FIX_ME")
    whats_new_button                        = (By.CSS_SELECTOR , "ion-item:nth-of-type(6)", "FIX_ME")
    about_button                            = (By.CSS_SELECTOR , "ion-item:nth-of-type(7)", "FIX_ME")
    loaded_language_subtext                 = (By.CSS_SELECTOR, "app-home-settings-popover p", "language listed in settings menu")
    about_page_hyperlinks_privacy_notice    = (By.CSS_SELECTOR , "ion-card>a:nth-of-type(1)", "about page hyperlinks, for example, 'Privacy notice'")
    about_page_hyperlinks_terms_of_use      = (By.CSS_SELECTOR , "ion-card>a:nth-of-type(2)", "about page hyperlinks, for example, 'Privacy notice'")
    about_page_hyperlinks_acknowledgements  = (By.CSS_SELECTOR , "ion-card>a:nth-of-type(3)", "about page hyperlinks, for example, 'Privacy notice'")

    language_manage_page_language_name      = (By.CSS_SELECTOR , "ion-radio-group ion-item:nth-of-type(1) ion-label", "Label for first language on language select page")
    language_manage_page_delete_button      = (By.CSS_SELECTOR , "ion-radio-group ion-item:nth-of-type(1) ion-buttons ion-button", "Delete button on select language page, trash icon")
    language_manage_page_add_language_button    = (By.CSS_SELECTOR , "app-language-manage div ion-button", "Add language button")
    language_manage_page_confirm_delete_button  = (By.CSS_SELECTOR , "ion-alert div div:nth-of-type(3) button:nth-of-type(2)", "Add language button")

    language_select_page_target_language_dropdown = (By.CSS_SELECTOR , "ng-select:nth-of-type(1)", "Target language select dropdown")
    language_select_page_choose_japanese = (By.CSS_SELECTOR , "ng-dropdown-panel div div div:nth-of-type(30)", "Select japanese from language select dropdown")
    language_select_page_submit_button = (By.CSS_SELECTOR , "app-add-language div div ion-button", "Submit language on selection page")

    log_out_button          = (By.CSS_SELECTOR, "ion-item ion-button", "settings menu logout button")

    tip_pop_up              = (By.CSS_SELECTOR, "div.tip-popover-box", "tip pop-up box")
    tip_pop_up_close        = (By.CSS_SELECTOR, "div.tip-popover-box ion-icon", "close pop-up button")

    lesson_1_heavenly_father= (By.CSS_SELECTOR, "app-task-card:nth-of-type(1)>ion-card", "Heavenly Father task in PMG lesson 1(og:spanish)")
    heavenly_father_listening=(By.CSS_SELECTOR, "app-lesson-card[iconname='listening']>ion-card", "listening task in Heavenly Father(og:spanish)")

    # Basic Lessons
    basic_first_lesson          = (By.CSS_SELECTOR, "div.learnTab__container:nth-of-type(2)>app-task-card:first-of-type>ion-card", "first lesson on basic tab (og:S-spanish)")
    basic_first_lesson_title    = (By.CSS_SELECTOR, "div.learnTab__container:nth-of-type(2)>app-task-card:first-of-type>ion-card span.title", "first lesson title on basic tab (og:S-spanish)")
    basic_alphabet_card         = (By.CSS_SELECTOR, "div.learnTab>div:nth-of-type(2)>app-task-card:first-of-type>ion-card", "alphabet card in basic(og:korean)")
    basic_alphabet_card_title   = (By.CSS_SELECTOR, "div.learnTab>div:nth-of-type(2)>app-task-card:first-of-type>ion-card span.title", "alphabet card in basic(og:korean)")
    
    # Prework Lessons
    prework_first_group_title   = (By.CSS_SELECTOR, "div.learnTab__container:nth-of-type(3) app-task-card:first-of-type>h1", "first prework lesson group title (og: S-spanish 'Building Genuine Relationships')")
    prework_first_lesson        = (By.CSS_SELECTOR, "div.learnTab__container:nth-of-type(3) app-task-card:first-of-type>ion-card", "first prework lesson (og: S-spanish 'Introducing Yourself')")

    # Daily life Lessons
    daily_life_first_group_title   = (By.CSS_SELECTOR, "div.learnTab__container:nth-of-type(4) app-task-card:first-of-type>h1", "first daily life lesson group title (og: S-spanish 'Common Vocabulary')")
    daily_life_first_lesson        = (By.CSS_SELECTOR, "div.learnTab__container:nth-of-type(4) app-task-card:first-of-type>ion-card", "first daily life lesson (og: S-spanish 'Common Verbs')")
    
    # PMG Lessons
    pmg_lessons_first_group_title   = (By.CSS_SELECTOR, "div.learnTab__container:nth-of-type(5) app-task-card:first-of-type>h1", "first 'pmg lessons' lesson group title (og: S-spanish 'Common Vocabulary')")
    pmg_lessons_first_lesson        = (By.CSS_SELECTOR, "div.learnTab__container:nth-of-type(5) app-task-card:first-of-type>ion-card", "first 'pmg lessons' lesson (og: S-spanish 'Common Verbs')")
    
    first_card_in_alphabet  = (By.CSS_SELECTOR, "app-flashcard:first-of-type>ion-card h1", "first card in alphabet discover(og:korean)")
    
    basic_meet_someone_card = (By.CSS_SELECTOR, "div.learnTab>div:nth-of-type(2)>app-task-card:nth-of-type(2)>ion-card", "meet someone lesson card in basic(og:spanish)")

    # Resources
    resources_title         = (By.CSS_SELECTOR, "app-home-resources-tab>h1", "Resources page title (og:S-span 'Resources')")
    resources_embark_lesson = (By.CSS_SELECTOR, "app-home-resources-tab app-collections>div>div:last-of-type>app-study-list-card:last-of-type>ion-card", "Resources page last lesson (og:S-span 'How to use embark lesson')")
    resources_embark_title  = (By.CSS_SELECTOR, "app-home-resources-tab app-collections>div>div:last-of-type>app-study-list-card:last-of-type>ion-card span#title", "Resources page last lesson title (og:S-span 'How to use embark lesson')")
    spanish_resources_grammar=(By.CSS_SELECTOR, "app-lesson-collection-card:last-of-type>ion-card", "Grammar Lessons in resources(og:spanish)")
    spanish_grammar_articles= (By.CSS_SELECTOR, "ion-content>ion-card:nth-of-type(3)", "articles card in grammar lessons(og:spanish)")
    grammar_lesson_header   = (By.CSS_SELECTOR, "app-lesson ion-toolbar", "Header of grammar lesson(og:spanish-articles")
    spanish_resources_vocab = (By.CSS_SELECTOR, "div>ion-card:nth-of-type(9)", "Vocabulary and Phrases card(og:spanish)")
    resources_pray_often    = (By.CSS_SELECTOR, "ion-card:nth-of-type(24)", "Pray often in vocab in resources(og:spanish)")
    pdf_header_title        = (By.CSS_SELECTOR, "div.headerWrapper ion-title", "title in header of pdf viewer(og:spanish pray often)")

    # Search
    search_bar                  = (By.CSS_SELECTOR, "app-home-search-tab input", "Search page search bar (og: S-span)")
    search_page_words_tab       = (By.CSS_SELECTOR, "app-home-search-tab ion-segment-button:nth-of-type(1)", "Search page words tab (og: S-span)")
    search_page_phrases_tab     = (By.CSS_SELECTOR, "app-home-search-tab ion-segment-button:nth-of-type(2)", "Search page phrases tab (og: S-span)")
    search_page_resources_tab   = (By.CSS_SELECTOR, "app-home-search-tab ion-segment-button:nth-of-type(3)", "Search page resources tab (og: S-span)")
    search_no_results_message   = (By.CSS_SELECTOR, "app-home-search-tab div.no-results", "Search page no results message (og: S-span 'No matches found')")
    search_first_result         = (By.CSS_SELECTOR, "app-home-search-tab app-search-card ion-card:first-of-type", "Search page first result (og: S-span)")
    

    # Tones
    tones_main_header       = (By.CSS_SELECTOR, "app-header[maintitle='Tones']", "tones main title (og:mandarin (traditional))")
    tones_selector          = (By.CSS_SELECTOR, "ion-toolbar.tone-card", "tones main title (og:mandarin (traditional))")
    tones_option_combinations = (By.CSS_SELECTOR, "app-tone-study-list-type-select ion-item:nth-of-type(2)", "tones main title (og:mandarin (traditional))")

    individual_tones_first  = (By.CSS_SELECTOR, "ion-row.tone-card>ion-col:nth-of-type(1)", "individual tones first (og:mandarin (traditional))")
    individual_tones_second = (By.CSS_SELECTOR, "ion-row.tone-card>ion-col:nth-of-type(2)", "individual tones second (og:mandarin (traditional))")
    individual_tones_third  = (By.CSS_SELECTOR, "ion-row.tone-card>ion-col:nth-of-type(3)", "individual tones third (og:mandarin (traditional))")
    individual_tones_fourth = (By.CSS_SELECTOR, "ion-row.tone-card>ion-col:nth-of-type(4)", "individual tones fourth (og:mandarin (traditional))")
    individual_tones_fifth  = (By.CSS_SELECTOR, "ion-row.tone-card>ion-col:nth-of-type(5)", "individual tones fifth (og:mandarin (traditional))")
    
    combination_tones_first  = (By.CSS_SELECTOR, "ion-row.tone-card>ion-col:nth-of-type(1)", "combination tones first (og:mandarin (traditional))")
    combination_tones_second = (By.CSS_SELECTOR, "ion-row.tone-card>ion-col:nth-of-type(2)", "combination tones second (og:mandarin (traditional))")
    combination_tones_third  = (By.CSS_SELECTOR, "ion-row.tone-card>ion-col:nth-of-type(3)", "combination tones third (og:mandarin (traditional))")
    combination_tones_fourth = (By.CSS_SELECTOR, "ion-row.tone-card>ion-col:nth-of-type(4)", "combination tones fourth (og:mandarin (traditional))")
   
    language_manage_page_language_name      = (By.CSS_SELECTOR , "ion-radio-group ion-item:nth-of-type(1) ion-label", "Label for first language on language select page")
    language_manage_page_delete_button      = (By.CSS_SELECTOR , "ion-radio-group ion-item:nth-of-type(1) ion-buttons ion-button", "Delete button on select language page, trash icon")
    language_manage_page_add_language_button    = (By.CSS_SELECTOR , "app-language-manage div ion-button", "Add language button")
    language_manage_page_confirm_delete_button  = (By.CSS_SELECTOR , "ion-alert div div:nth-of-type(3) button:nth-of-type(2)", "Add language button")

    language_select_page_target_language_dropdown = (By.CSS_SELECTOR , "ng-select:nth-of-type(1)", "Target language select dropdown")
    language_select_page_choose_japanese = (By.CSS_SELECTOR , "ng-dropdown-panel div div div:nth-of-type(30)", "Select japanese from language select dropdown")
    language_select_page_submit_button = (By.CSS_SELECTOR , "app-add-language div div ion-button", "Submit language on selection page")

    tip_pop_up              = (By.CSS_SELECTOR , "div.tip-popover-box", "tip pop-up box")
    tip_pop_up_close        = (By.CSS_SELECTOR , "div.tip-popover-box ion-icon", "close pop-up button")

    lesson_1_heavenly_father= (By.CSS_SELECTOR , "app-task-card:nth-of-type(1)>ion-card", "Heavenly Father task in PMG lesson 1(og:spanish)")
    heavenly_father_listening=(By.CSS_SELECTOR , "app-lesson-card[iconname='listening']>ion-card", "listening task in Heavenly Father(og:spanish)")
    # = (By.CSS_SELECTOR , "ion-segment-button:nth-of-type(5)", "FIX_ME")
    first_card_in_alphabet  = (By.CSS_SELECTOR , "app-flashcard:nth-of-type(1)>ion-card h1", "first card in alphabet discover(og:korean)")
    alphabet_learn_card     = (By.CSS_SELECTOR, "app-home-learn-tab>div>div>app-for-you-group>app-task-card:nth-of-type(3)", "Experimenting with clicking")

    spanish_resources_grammar=(By.CSS_SELECTOR , "app-lesson-collection-card:last-of-type>ion-card", "Grammar Lessons in resources(og:spanish)")
    spanish_grammar_articles= (By.CSS_SELECTOR , "ion-content>ion-card:nth-of-type(3)", "articles card in grammar lessons(og:spanish)")
    grammar_lesson_header   = (By.CSS_SELECTOR , "app-lesson ion-toolbar", "Header of grammar lesson(og:spanish-articles")
    spanish_resources_vocab = (By.CSS_SELECTOR , "div>ion-card:nth-of-type(9)", "Vocabulary and Phrases card(og:spanish)")
    resources_pray_often    = (By.CSS_SELECTOR , "ion-card:nth-of-type(24)", "Pray often in vocab in resources(og:spanish)")
    pdf_header_title        = (By.CSS_SELECTOR , "div.headerWrapper ion-title", "title in header of pdf viewer(og:spanish pray often)")


    # Lesson Discover
    lesson_discover_button  = (By.CSS_SELECTOR, "app-task-nav-button:nth-of-type(1)>ion-button", "lesson page discover button (og: spanish alphabet)")
    lesson_practice_button  = (By.CSS_SELECTOR, "app-task-nav-button:nth-of-type(2)>ion-button", "lesson page button (og: spanish alphabet)")
    lesson_pass_off_button  = (By.CSS_SELECTOR, "app-task-nav-button:nth-of-type(3)>ion-button", "lesson page button (og: spanish alphabet)")
    alphabet_first_letter   = (By.CSS_SELECTOR, "#alphabet-grid>button:first-of-type", "First card on alphabet lesson (og: spanish alphabet 'a')")

    vocab_most_common_label     = (By.CSS_SELECTOR, "ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>div", "Most Common header")
    vocab_first_word            = (By.CSS_SELECTOR, "ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item>div>div>span", "First word in vocab list")
    vocab_first_word_play       = (By.CSS_SELECTOR, "ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item>ion-icon", "Play button for first word in vocab list")
    vocab_first_word_playing    = (By.CSS_SELECTOR, ".audio-icon", "First word in vocab list is playing")
    # vocab_first_word_favorite   = (By.CSS_SELECTOR, "ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item>div>div>ion-button", "Favorite button on first audio word")

    vocab_discover_record           = (By.CSS_SELECTOR, "app-activity-tool-bar>div>div>div:nth-of-type(2)>span>ion-icon", "Record button in flashcards")
    vocab_discover_recording        = (By.CSS_SELECTOR, "ion-icon[title='Stop Recording']", "Recording icon in flashcards")
    vocab_discover_play_recording   = (By.CSS_SELECTOR, "ion-icon[title='Play Recording']", "Recording icon in flashcards")
    vocab_discover_re_record        = (By.CSS_SELECTOR, "ion-icon[title='Record Again']", "Recording icon in flashcards")
    vocab_discover_right_arrow      = (By.CSS_SELECTOR, "#right", "Right button on flashcards")
    vocab_discover_take_quiz_button = (By.CSS_SELECTOR, "app-quiz>div>div>div>ion-button", "Take quiz button")
    vocab_discover_exit             = (By.CSS_SELECTOR, "ion-toolbar>div>ion-icon", "Exit out of quiz")

    vocab_discover_quiz_native_1    = (By.CSS_SELECTOR, "app-matching-quiz>div>div:nth-of-type(1)>div:nth-of-type(1)", "Native language item 1 in quiz")
    vocab_discover_quiz_native_2    = (By.CSS_SELECTOR, "app-matching-quiz>div>div:nth-of-type(1)>div:nth-of-type(2)", "Native language item 2 in quiz")
    vocab_discover_quiz_native_3    = (By.CSS_SELECTOR, "app-matching-quiz>div>div:nth-of-type(1)>div:nth-of-type(3)", "Native language item 3 in quiz")
    vocab_discover_quiz_native_4    = (By.CSS_SELECTOR, "app-matching-quiz>div>div:nth-of-type(1)>div:nth-of-type(4)", "Native language item 4 in quiz")
    vocab_discover_quiz_native_5    = (By.CSS_SELECTOR, "app-matching-quiz>div>div:nth-of-type(1)>div:nth-of-type(5)", "Native language item 5 in quiz")
    vocab_discover_quiz_native_6    = (By.CSS_SELECTOR, "app-matching-quiz>div>div:nth-of-type(1)>div:nth-of-type(6)", "Native language item 6 in quiz")

    vocab_discover_quiz_target_1    = (By.CSS_SELECTOR, "app-matching-quiz>div>div:nth-of-type(2)>div:nth-of-type(1)", "Native language item 1 in quiz")
    vocab_discover_quiz_target_2    = (By.CSS_SELECTOR, "app-matching-quiz>div>div:nth-of-type(2)>div:nth-of-type(2)", "Native language item 2 in quiz")
    vocab_discover_quiz_target_3    = (By.CSS_SELECTOR, "app-matching-quiz>div>div:nth-of-type(2)>div:nth-of-type(3)", "Native language item 3 in quiz")
    vocab_discover_quiz_target_4    = (By.CSS_SELECTOR, "app-matching-quiz>div>div:nth-of-type(2)>div:nth-of-type(4)", "Native language item 4 in quiz")
    vocab_discover_quiz_target_5    = (By.CSS_SELECTOR, "app-matching-quiz>div>div:nth-of-type(2)>div:nth-of-type(5)", "Native language item 5 in quiz")
    vocab_discover_quiz_target_6    = (By.CSS_SELECTOR, "app-matching-quiz>div>div:nth-of-type(2)>div:nth-of-type(6)", "Native language item 6 in quiz")

    symbol_popover_symbols  = (By.CSS_SELECTOR, "app-symbol-popover div.symbol-row", "Symbol popup top row symbols (og: spanish alphabet 'a')")
    symbol_popover_play     = (By.CSS_SELECTOR, "#volume-icon", "Symbol popup bottom row play sound (og: spanish alphabet 'a')")
    symbol_popover_playing  = (By.CSS_SELECTOR, "#volume-icon-playing", "Symbol popup bottom row play sound (og: spanish alphabet 'a')")
    symbol_popover_favorite = (By.CSS_SELECTOR, "ion-icon[title='Star']", "Symbol popup bottom row favorite (og: spanish alphabet 'a')")
    symbol_popover_unfavorite=(By.CSS_SELECTOR, "ion-icon[title='Unstar']", "Symbol popup bottom row unfavorite (og: spanish alphabet 'a')")

    symbol_popover_example          = (By.CSS_SELECTOR, "div.examples:nth-of-type(2)>span.example-words", "Symbol popup first example word (og: spanish alphabet 'a')")
    symbol_popover_example_play     = (By.CSS_SELECTOR, "div.examples:nth-of-type(2) ion-icon.example-sound", "Symbol popup first example word play button (og: spanish alphabet 'a')")
    symbol_popover_example_playing  = (By.CSS_SELECTOR, "div.examples:nth-of-type(2) ion-icon.ion-color-primary", "Symbol popup first example word play button (og: spanish alphabet 'a')")

    symbol_popover_discovered   =(By.CSS_SELECTOR, "span[title='Mark as Discovered']", "Symbol popup bottom row unmarked (og: spanish alphabet 'a')")
    symbol_popover_mastered     =(By.CSS_SELECTOR, "span[title='Mark as Mastered']", "Symbol popup bottom row unmarked (og: spanish alphabet 'a')")
    symbol_popover_unmark       =(By.CSS_SELECTOR, "span[title='Unmark']", "Symbol popup bottom row unmarked (og: spanish alphabet 'a')")

    vocab_concept_list_discovered_1 = (By.CSS_SELECTOR, "app-task-study-list>ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item:nth-of-type(2)>ion-icon:nth-of-type(3)", "Discovered button in vocab list 1")
    vocab_concept_list_discovered_2 = (By.CSS_SELECTOR, "app-task-study-list>ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item:nth-of-type(3)>ion-icon:nth-of-type(3)", "Discovered button in vocab list 2")
    vocab_concept_list_discovered_3 = (By.CSS_SELECTOR, "app-task-study-list>ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item:nth-of-type(4)>ion-icon:nth-of-type(3)", "Discovered button in vocab list 3")
    vocab_concept_list_discovered_4 = (By.CSS_SELECTOR, "app-task-study-list>ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item:nth-of-type(5)>ion-icon:nth-of-type(3)", "Discovered button in vocab list 4")
    vocab_concept_list_discovered_5 = (By.CSS_SELECTOR, "app-task-study-list>ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item:nth-of-type(6)>ion-icon:nth-of-type(3)", "Discovered button in vocab list 5")
    vocab_concept_list_discovered_6 = (By.CSS_SELECTOR, "app-task-study-list>ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item:nth-of-type(7)>ion-icon:nth-of-type(3)", "Discovered button in vocab list 6")

    vocab_concept_list_discovered_button_1 = (By.CSS_SELECTOR, "app-task-study-list>ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item:nth-of-type(1)>div>div:nth-of-type(2)>span", "Discovered button in vocab list 1")
    vocab_concept_list_discovered_button_2 = (By.CSS_SELECTOR, "app-task-study-list>ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item:nth-of-type(2)>div>div:nth-of-type(2)>span", "Discovered button in vocab list 2")
    vocab_concept_list_discovered_button_3 = (By.CSS_SELECTOR, "app-task-study-list>ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item:nth-of-type(3)>div>div:nth-of-type(2)>span", "Discovered button in vocab list 3")
    vocab_concept_list_discovered_button_4 = (By.CSS_SELECTOR, "app-task-study-list>ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item:nth-of-type(4)>div>div:nth-of-type(2)>span", "Discovered button in vocab list 4")
    vocab_concept_list_discovered_button_5 = (By.CSS_SELECTOR, "app-task-study-list>ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item:nth-of-type(5)>div>div:nth-of-type(2)>span", "Discovered button in vocab list 5")
    vocab_concept_list_discovered_button_6 = (By.CSS_SELECTOR, "app-task-study-list>ion-content>div>div>div>div:nth-of-type(3)>app-concept-list>ion-card>ion-item:nth-of-type(6)>div>div:nth-of-type(2)>span", "Discovered button in vocab list 6")


    lesson_discover_flashcards          = (By.CSS_SELECTOR, "ion-content h1", "Flashcards info card title (og: spanish alphabet discover)")
    lesson_discover_flashcards_start    = (By.CSS_SELECTOR, "ion-footer>ion-button", "Flashcards start button (og: spanish alphabet discover)")
    lesson_discover_flashcard_text      = (By.CSS_SELECTOR, "app-discover>ion-content>div>swiper>div", "Flashcard text")
    lesson_discover_toolbar             = (By.CSS_SELECTOR, "app-activity-tool-bar", "Toolbar in flashcards")
    
    lesson_practice_multiple_choice         = (By.CSS_SELECTOR, "app-pick-activity>ion-content>div>div:nth-of-type(2)>app-study-list-card", "First option on pick activity page, in this case multiple choice")
    lesson_practice_fill_in_blank           = (By.CSS_SELECTOR, "div>div:nth-of-type(2)>app-study-list-card>ion-card", "First option on pick activity page")
    lesson_practice_check                   = (By.CSS_SELECTOR, "ion-grid ion-button", "Check button in fill in blank")
    lesson_practice_input                   = (By.CSS_SELECTOR, "app-symbol-test>div>div>ion-card>ion-item>ion-input>input", "Text input")
    lesson_spaced_review_button             = (By.CSS_SELECTOR, "app-task-study-list>ion-content>div>div>div>ion-button", "Spaced review button on vocab/phrase/alphabet page")
    lesson_practice_mine_works_too_button   = (By.CSS_SELECTOR, "app-quadrants>div>ion-footer>ion-toolbar>ion-row>ion-button", "Mine works too button in lesson practice")
    lesson_practice_got_it_button           = (By.CSS_SELECTOR, "app-quadrants>div>ion-footer>ion-toolbar>ion-row>ion-button:nth-of-type(2)", "Got it button in lesson practice")
    lesson_practice_header_progress_numbers = (By.CSS_SELECTOR, "app-activity-wrapper>app-progress-header>div>ion-header>ion-toolbar>div>app-progress-bar>div>p", "Toolbar in lesson practice")
    
    lesson_practice_type_or_say             = (By.CSS_SELECTOR, "app-pick-activity>ion-content>div>div:nth-of-type(2)>app-study-list-card:nth-of-type(3)", "Third option on pick activity page, in this case type and say")
    lesson_practice_type_or_say_prompt      = (By.CSS_SELECTOR, "app-typing>div>div>ion-toolbar>ion-title", "Prompt in type or say")
    lesson_practice_type_or_say_input       = (By.CSS_SELECTOR, "app-typing>div>div>div>ion-card>ion-item>ion-textarea", "Type or say input")

    spaced_review_quadrants_prompt  = (By.CSS_SELECTOR, "app-quadrants>div>ion-header", "Prompt word in quadrants for Spaced Review")
    spaced_review_quadrants_answer1 = (By.CSS_SELECTOR, "app-quadrants>div>div>ion-grid>ion-row>ion-col", "Answer 1 spaced review quadrants")
    spaced_review_quadrants_answer2 = (By.CSS_SELECTOR, "app-quadrants>div>div>ion-grid>ion-row>ion-col:nth-of-type(2)", "Answer 2 spaced review quadrants")
    spaced_review_quadrants_answer3 = (By.CSS_SELECTOR, "app-quadrants>div>div>ion-grid>ion-row>ion-col:nth-of-type(3)", "Answer 3 spaced review quadrants")
    spaced_review_quadrants_answer4 = (By.CSS_SELECTOR, "app-quadrants>div>div>ion-grid>ion-row>ion-col:nth-of-type(4)", "Answer 4 spaced review quadrants")
    spaced_review_skip_button       = (By.CSS_SELECTOR, "ion-footer>ion-button", "Skip button in spaced review")

    spaced_review_continue_button       = (By.CSS_SELECTOR, "ion-footer ion-button", "Continue button in spaced review")
    spaced_review_mine_works_too_button = (By.CSS_SELECTOR, "ion-footer>ion-toolbar>ion-row>ion-button", "Mine works too button in spaced review")
    spaced_review_got_it_button         = (By.CSS_SELECTOR, "ion-toolbar ion-button:nth-of-type(2)", "Got it button in spaced review")
    spaced_review_start_button          = (By.CSS_SELECTOR, "app-spaced-review-card>div>ion-card>div:nth-of-type(2)>div:nth-of-type(3)>button", "Start button on spaced review card")
    spaced_review_heart1                = (By.CSS_SELECTOR, "app-spaced-review>ion-header>ion-toolbar>ion-item>ion-icon:nth-of-type(1)", "First heart in Spaced Review (lastone marked")
    
    spaced_review_soundbite                         = (By.CSS_SELECTOR, "app-spaced-review>ion-content>div>app-soundbite", "Sound bites component")
    spaced_review_soundbite_answer                  = (By.CSS_SELECTOR, "app-spaced-review>ion-content>div>app-soundbite>div>div>ion-row>ion-col>ion-buttons>app-audio>ion-button", "Sound bites answer button")
    spaced_review_soundbite_check_button            = (By.CSS_SELECTOR, "app-spaced-review>ion-content>div>app-soundbite>div>ion-footer>ion-toolbar>ion-row>ion-button", "Sound bites check answer button")
    spaced_review_soundbite_mine_works_too_button   = (By.CSS_SELECTOR, "app-spaced-review>ion-content>div>app-soundbite>div>ion-footer>ion-toolbar>ion-row:nth-of-type(2)>ion-button", "Mine works too button in soundbite activity spaced review")
    spaced_review_type_or_say_input                 = (By.CSS_SELECTOR, "app-spaced-review>ion-content>div>app-typing>div>div>div>ion-card>ion-item>ion-textarea>div>textarea", "Type or say input")
    spaced_review_type_or_say_check                 = (By.CSS_SELECTOR, "app-spaced-review>ion-content>div>app-typing>div>div>ion-grid>ion-row>ion-col>ion-button", "Spaced review type or say check button")
    spaced_review_typing_continue_button            = (By.CSS_SELECTOR, "app-spaced-review>ion-content>div>app-typing>div>div>ion-grid>ion-row>ion-col>ion-button", "Continue button is different for typing? Same selector as check though, just makes it more clear")

    move_up_one_day_button  = (By.CSS_SELECTOR, "app-home-learn-tab>div>div>app-for-you-group>app-spaced-review-card>ion-button", "Move up one day button")
    
    session_summary_text = (By.CSS_SELECTOR, "app-session-summary>ion-card>ion-card-header>h4", "Message to user when spaced review finishes, used in Hearts test")


class ProdElements(Elements):
    pass

class StageElements(Elements):
    whats_new_card_close_button         = (By.CSS_SELECTOR , "ion-card ion-button:nth-of-type(1)", "FIX_ME")
    whats_new_card_learn_more_button    = (By.CSS_SELECTOR , "ion-card ion-button:nth-of-type(2)", "FIX_ME")
    my_added_phrases                    = (By.CSS_SELECTOR , "app-for-you-group > ion-card:nth-of-type(2)", "FIX_ME")

    added_phrase_group                  = (By.CSS_SELECTOR, "div.section:nth-of-type(2) p", "FIX_ME")
    embark_topics_view_all              = (By.CSS_SELECTOR, "div.section:nth-of-type(2) div.header button", "FIX_ME")
    
    log_out_button                      = (By.CSS_SELECTOR , "app-home-settings-popover ion-button", "Log out button in settings popover")
    languages_button                    = (By.CSS_SELECTOR , "app-home-settings-popover ion-item:nth-of-type(2)", "Languages button button in settings popover")
    sound_effects                       = (By.CSS_SELECTOR , "app-home-settings-popover ion-item:nth-of-type(3)", "Sound effects menu item")
    sound_effects_toggle                = (By.CSS_SELECTOR , "app-home-settings-popover ion-item:nth-of-type(3)>ion-toggle", "Sound effects on/off toggle")
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
