# ------- Now we will discuss about the advance CSS selector strategies -------
# ------- demo URL : https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php -------
# ------  https://www.automatetheplanet.com/selenium-webdriver-locators-cheat-sheet/  ------
# ------  https://www.w3schools.com/cssref/css_selectors.php ------
# ------  https://www.w3.org/TR/selectors-3/#selectors ------

txtbox_name = "input[id='name']"  # --- Normal Css schema
txtbox_name = "input#name"  # --- tagname#id
txtbox_name = "#name"  # --- #id  Tagname is optional

link_selenium_tutorial = "a.external-link"  # --- Tagname.Classname
link_selenium_tutorial = ".external-link"  # --- .Classname  Tagname is optional

link_selenium_tutorial ="a[class='external-link'][title='back to Selenium Tutorial']"  # --- two properties
link_selenium_tutorial ="[class='external-link'][title='back to Selenium Tutorial']" # Tag name is optional

txtbox_mobile = "input#mobile.form-control"  # ------ combining tag, Id, Class
txtbox_mobile = "input#mobile.form-control[name='mobile']"  # ------ combining Tag,Id,Class,attribute
txtbox_mobile = "#mobile.form-control[name='mobile']"  # ------ combining Id,Class,attribute.    Tag is optional

option_uttar_pradesh = "option[value^='Uttar']"     # ----- value attribute starts with Uttar
option_uttar_pradesh = "option[value$='Pradesh']"   # ----- value attribute ends with Pradesh
option_uttar_pradesh = "option[value*='r Pr']"      # ----- value attribute contains 'r Pr'

option_element = "select#state>option"       # --------- all childs of select tag
option_element = "select#state option"      # all child & subchilds of Select tab
elements_collapse_sign = "h2#headingOne+div"    # all child & subchilds of Select tab   div element immediately preceeded by h2
elements_collapse_sign = "h2#headingOne~div"    # div element preceeded by h2

option_hariyana = "select#state option:nth-child(4)"     # ----- nth-child
option_hariyana = "select#state option:nth-last-child(2)"     # ----- nth-last-child
option_hariyana = "select#state option:nth-of-type(4)"     # ----- nth-of-type
option_hariyana = "select#state option:nth-last-of-type(2)"     # ----- nth-last-of-type
option_choose_state = "select#state option:first-child"    # ------- first-child
option_rajasthan = "select#state option:last-child"     # ------- last-child
option_choose_state = "select#state option:first-of-type"    #  ------- first-of-type
option_rajasthan = "select#state option:last-of-type"       # ------- last-of-type

#   a:link      a:visited       input:checked       input:enabled       input:disabled