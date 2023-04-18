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
