import time 
from selenium import webdriver
driver = webdriver.Chrome('/home/thamarai/Downloads/chromedriver')
driver.get('https://dev.eventjini.com/DH2-MASTER/login')
driver.maximize_window()
time.sleep(1)
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys('gayathree@eventjini.me')
time.sleep(1)
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys('Arizona123')
driver.find_element_by_id('recaptcha-submit').click()
driver.find_element_by_id('project request').click()
time.sleep(1)
driver.find_element_by_class_name('btn').click()
time.sleep(1)
driver.find_element_by_class_name('radio').click()
time.sleep(1)
driver.find_element_by_id('existing_client_radio').click()
driver.find_element_by_id('order_name').send_keys('Anything')
driver.find_element_by_id('add_new_product').click()
time.sleep(1)
driver.find_element_by_id('goal_sales').click()
time.sleep(1)
driver.find_element_by_id('save_goals').click()
time.sleep(1)
driver.find_element_by_id('goals_save').click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, 500)")
driver.find_element_by_id('product_display').click()
driver.find_element_by_css_selector("input[type='radio'][value='yes']").click()
driver.find_element_by_name('start-date').send_keys('12-01-2020')
driver.find_element_by_name('end-date').send_keys('11-04-2020')
time.sleep(1)   
driver.find_element_by_css_selector("input[type='radio'][value='no']").click()
driver.find_element_by_class_name('monthly_budget').clear()
time.sleep(1)
driver.find_element_by_class_name('monthly_budget').send_keys('150000')
time.sleep(1)
driver.find_element_by_css_selector("input[type='radio'][name='gb_allocate'][value='no']").click()
driver.find_element_by_id('save_products').click()
driver.find_element_by_id('products_save').click()
time.sleep(1)
driver.find_element_by_id('display_monthly_budget').send_keys('2000')
time.sleep(1)
driver.find_element_by_name('display_cpm').send_keys('1.2')
driver.find_element_by_id('btn_calculate_impressions').click()
time.sleep(1)
driver.find_element_by_css_selector("input[type='radio'][name='allocate'][value='impression']").click()
driver.find_element_by_id('no_of_impressions').send_keys('12000')
driver.find_element_by_name('display_start_date').send_keys('23-01-2020')
time.sleep(1)
driver.find_element_by_name('display_end_date').send_keys('14-02-2020')
driver.find_element_by_css_selector("input[type='radio'][name='display_date'][value='no']").click()
driver.find_element_by_id('save_allocation').click()
driver.find_element_by_id('allocation_save').click()
driver.find_element_by_class_name('product_display').click()
driver.execute_script("window.scrollTo(0, 2800)")
driver.find_element_by_class_name('btn-attention').click()
time.sleep(1)
driver.find_element_by_class_name('add_content').click()
driver.find_element_by_name('display_add_creative_name_of_ad-1').send_keys('anything to test')
driver.find_element_by_name('display_add_creative_name_of_cta-1').send_keys('something')
driver.find_element_by_name('display_add_creative_name_of_client_url-1').send_keys('https://dev.eventjini.com/DH2-MASTER')
driver.find_element_by_name('display_add_creative_name_of_target_url-1').send_keys('https://www.facebook.com/')
driver.find_element_by_name('display_add_creative_name_of_ad_desc-1').send_keys('the quick brown fox jumps over the lazy dog')
time.sleep(1)
driver.find_element_by_name("userfile_display-1[]").send_keys("/home/thamarai/Pictures/0.jpeg")
time.sleep(1)
driver.find_element_by_class_name('btn-creative').click()
driver.find_element_by_css_selector("input[type='radio'][name='gb_choose_tactics'][value='1']").click()
driver.find_element_by_class_name('geo_fence').click()
time.sleep(1)
driver.find_element_by_class_name('add_geo_fence').click()
time.sleep(2)
driver.find_element_by_name('userfile_display-geo-fencing[]').send_keys("/home/thamarai/Pictures/0.jpeg")
time.sleep(2)
driver.find_element_by_id('save_display').click()
driver.find_element_by_class_name('geo_fence').click()
#Audience_retarget Option 
driver.find_element_by_class_name('audience_retarget').click()
time.sleep(1)
driver.find_element_by_class_name('add_audience_retarget').click()
driver.find_element_by_name('display-audience_retarget-personas').send_keys('paste_your_Info_here')
driver.find_element_by_name('display-audience_retarget-category').send_keys('catagory_information_here')
driver.find_element_by_name('display-audience_retarget-demography').send_keys('display-audience_retarget-demography')
driver.find_element_by_name('display-audience_retarget-your_notes').send_keys('display-audience_retarget-your_notes')
driver.find_element_by_css_selector("button[type='button'][class='audience_retarget btn btn-choose-tactics display_btn active']").click()
time.sleep(1)
driver.find_element_by_class_name('audience_collection').click()
time.sleep(1)
driver.find_element_by_name('userfile_display-audience-collection[]').send_keys('/home/thamarai/Pictures/0.jpeg')
time.sleep(2)
driver.find_element_by_class_name('add_audience_collection').click()
time.sleep(1)
driver.find_element_by_css_selector("button[type='button'][class='audience_collection btn btn-choose-tactics display_btn active']").click()
time.sleep(1)
driver.find_element_by_class_name('category_contextual').click()
driver.find_element_by_class_name('add_category_contextual').click()
driver.find_element_by_name('display-category_contextual-category').send_keys('hello , this , is , testing, profile,')
driver.find_element_by_css_selector("button[type='button'][class='category_contextual btn btn-choose-tactics display_btn active']").click()
time.sleep(1)
driver.find_element_by_class_name('keysearch_retarget').click()
time.sleep(1)
driver.find_element_by_class_name('add_keysearch_retarget').click()
time.sleep(1)
driver.find_element_by_name('display-keysearch_retarget-impression_allocated').send_keys('5000')
driver.find_element_by_css_selector("button[type='button'][class='keysearch_retarget btn btn-choose-tactics display_btn active']").click()
time.sleep(1)
driver.find_element_by_class_name('site_retarget').click()
driver.find_element_by_class_name('add_site_retarget').click()
driver.find_element_by_name('display-site_retarget-impression_allocated').send_keys('2000')
#driver.find_element_by_css_selector("button[type='button'][class='site_retarget btn btn-choose-tactics display_btn active']").click()
driver.find_element_by_class_name('site_retarget').click()
driver.find_element_by_class_name('card-active').click()
driver.find_element_by_id('save_products').click()