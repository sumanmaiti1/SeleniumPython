# ------- Now we will discuss about the advance CSS selector strategies -------
# ------- demo URL : https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php -------
# ------  https://www.automatetheplanet.com/selenium-webdriver-locators-cheat-sheet/  ------

textbox_name = "/html/body/main/div/div/div[2]/form/div[1]/div/input"   #---------- Absolute Xpath
textbox_name = "//input[@id='name']"        # ----------- attribute with ID
textbox_name = "//input[@name='name']"        # ----------- attribute with name
textbox_name = "//input[@id='name' and @name='name']"        # ----------- attribute with name and id
textbox_name = "//input[@id='name' or @name='name']"        # ----------- attribute with name or id
textbox_name = "//input[@id='name' and @name!='bame']"        # ----------- attribute with name and id and Not
textbox_with_id_attribute = "//input[@id]"      # ------------  input field with name attribute
textbox_name = "//input[@id='name'][@name='name']"  # ----------- attribute with name and id
textbox_name = "//input[@id='name' and not(@name='bame')]"        # ----------- attribute with name and id and Not
label_dob = "//label[contains(text(),'Date')]"  #----------- contains and text
label_dob = "//label[starts-with(text(),'Date')]"  #----------- contains text in starts-with
label_dob = "//label[ends-with(text(),'Birth:')]"  #----------- contains text in ends-with
label_dob = "//label[normalize-space(text()) = 'Date of Birth:']"   #---------- Normalize-Text
textbox_name = "//form[@id='practiceForm']//input[1]"     #----------- use of // and index
textbox_name = "//input[@id][1]"     #----------- use of index
option_meerut = "//select[@id='city']//option[last()]"      # ---------- Last()
option_lucknow = "//select[@id='city']//option[last()-1]"   # ---------- Second Last element

#------------ Xpath Axes --------------
select_city = "//select[@id='city']/."     # ----------- . represents current element
parent_div_select_city = "//select[@id='city']/.."     # ----------- .. represents Parent element
parent_div_select_city_state = "//select[@id='city']/../.."     # ----------- .. represent parent
select_city = "//select[@id='city']/self::*"     # ----------- . represents current element Self
parent_div_select_city = "//select[@id='city']/parent::div/.."     # ----------- parent
select_city = "//select[@id='city']/parent::div/child::select"      # ----------- child


# ------------ https://www.tutorialspoint.com/selenium/practice/webtables.php -----------
td_salary = "//td[text()>10000]"
td_ancestor = "//td[text()='Insurance']/ancestor::tbody"
td_descendant = "//td[text()='Insurance']/ancestor::tbody/descendant::td[text()='Vega']"
td_following = "//td[text()='Vega']/following::td"
td_preceeding = "//td[text()='Insurance']/preceding::td"
td_preceeding_siblings ="(//td[text()='Cantrell']/preceding-sibling::td)[1]"
td_following_siblings = "(//td[text()='Cantrell'])[2]/following-sibling::td"
chkbox_music = "//label[text()='Music']/preceding-sibling::input"