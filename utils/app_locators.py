from appium.webdriver.common.appiumby import AppiumBy

# Onboarding
title = (AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
btn_continue = (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
btn_skip = (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')
ann_main_screen = (AppiumBy.ID, 'org.wikipedia.alpha:id/view_announcement_text')

# Search
search = (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
field_search = (AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')
result_search = (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')

# Menu
btn_menu = (AppiumBy.ID, 'org.wikipedia.alpha:id/menu_icon')
menu_item_login = (AppiumBy.ID, 'org.wikipedia.alpha:id/main_drawer_login_button')

# Login
field_username = (AppiumBy.XPATH, '(//*[@class="android.widget.EditText"])[1]')
text_error = (AppiumBy.ID, 'org.wikipedia.alpha:id/textinput_error')
btn_negative = (AppiumBy.ID, 'org.wikipedia.alpha:id/negativeButton')

# Saved Articles
widget_saved = (AppiumBy.ID, 'org.wikipedia.alpha:id/nav_tab_reading_lists')
empty_list = (AppiumBy.ID, 'org.wikipedia.alpha:id/empty_title')