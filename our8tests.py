from time import sleep
from unittest import expectedFailure
from xml.etree.ElementPath import xpath_tokenizer

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# chrome_options = Options()
# chrome_options.add_argument('--start-maximized')
#
# website = webdriver.Chrome(options=chrome_options)
# website.get('https://watanimall.com/?srsltid=AfmBOorcekbHU1S-mK6pLquCe68PneCckCJwqBTMvh0eIfzmCUE9NG1w//')
#
# profile_pic= website.find_element(By.CLASS_NAME,"icon-user")

# profile_pic.click()


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://watanimall.com/?srsltid=AfmBOorcekbHU1S-mK6pLquCe68PneCckCJwqBTMvh0eIfzmCUE9NG1w//')
    yield driver
    driver.quit()

def test1(driver):
     profile_pic= driver.find_element(By.CLASS_NAME,"icon-user")
     profile_pic.click()
     sleep(20)

# def test2(driver):
#     profile_pic= driver.find_element(By.CLASS_NAME,"icon-user")
#     profile_pic.click()
#     sleep(2)
#     emailBox=driver.find_element(By.ID,"login_email")
#
#     emailBox.send_keys("189c0c556b@emaily.pro")
#
#     passBox=driver.find_element(By.ID,"login_password")
#
#     passBox.send_keys("123123123")
#     sleep(2)
#     btn_login=driver.find_element(By.CLASS_NAME,"btn.btn-login")
#     btn_login.click()
#     sleep(10)
#     profile_pic = driver.find_element(By.CLASS_NAME, "icon-user")
#     profile_pic.click()
#     sleep(6)

# def test3(driver):
#
#     btn_lang=driver.find_element(By.CLASS_NAME,"js-wpml-ls-item-toggle.wpml-ls-item-toggle")
#     btn_lang.click()
#     sleep(3)
#     str_element = btn_lang.find_elements(By.CLASS_NAME, 'wpml-ls-native')
#     for str in str_element:
#         if str.text == 'english':
#             assert True
#         else:
#             pytest.fail("hello world")
#
# def test4(driver):
#     btn_lang=driver.find_element(By.CLASS_NAME,"js-wpml-ls-item-toggle.wpml-ls-item-toggle")
#     btn_lang.click()
#     sleep(3)
#     str_element = btn_lang.find_elements(By.CLASS_NAME, 'wpml-ls-native')
#     for str in str_element:
#         if str.text == 'english':
#             str.click()
#         else:
#             pytest.fail("we can not click the lang as it is not found")

# def test5(driver):
#     search_bar=driver.find_element(By.CLASS_NAME,"search-input")
#     search_bar.send_keys("Asus")
#     sleep(4)
#


# def test6(driver):
#     search_bar=driver.find_element(By.CLASS_NAME,"search-input")
#     search_bar.click()
#     search_bar.send_keys("Asus")
#     sleep(4)
#     btn_search = driver.find_element(By.XPATH, "//button[@class='btn-search']")
#     sleep(3)
#     btn_search.click()
#     sleep(4)

# def test7(driver):
#     search_bar=driver.find_element(By.CLASS_NAME,"search-input")
#     search_bar.click()
#     search_bar.send_keys("12423loiuim52")
#     sleep(4)
#     btn_search = driver.find_element(By.XPATH, "//button[@class='btn-search']")
#     sleep(3)
#     btn_search.click()
#     sleep(4)
#     msg=driver.find_element(By.XPATH,"//div[@class='woocommerce-info']")
#     assert msg.text != "لا توجد منتجات تتوافق مع اختيارك.	", "Test failed: Expected message not found."
#


#def test8(driver):
#    bool=False
#    search_bar=driver.find_element(By.CLASS_NAME,"search-input")
#    search_bar.click()
#    search_bar.send_keys("GPU ASUS DUAL RTX4060-O8G-GAMING")
#    sleep(4)
#    btn_search = driver.find_element(By.XPATH, "//button[@class='btn-search']")
#    sleep(3)
#    btn_search.click()
#    sleep(4)
#    prodect=driver.find_elements(By.XPATH,"//div[@class='product-col']")
#    for pro in prodect:
#        headerr=pro.find_element(By.XPATH,".//h3[@class='product-name']")
#        if headerr.text=="GPU ASUS DUAL RTX4060-O8G-GAMING":
#            bool=True
#    if bool==False:
#         pytest.fail()=

# def test20(driver):
#     LaptopAccessories = driver.find_elements(By.XPATH, ".//span[@class='category-name']")
#     for i in LaptopAccessories:
#         if (i.text == "laptop"):
#             i.click()
#             break
#     sleep(2)
#
#
# def test21(driver):
#     LaptopAccessories = driver.find_elements(By.XPATH, ".//span[@class='category-name']")
#     for i in LaptopAccessories:
#         if (i.text == "LAPTOP ACCESSORIES"):
#             i.click()
#             break
#     sleep(2)
#
#
# def test22(driver):
#     LaptopAccessories = driver.find_elements(By.XPATH, ".//span[@class='category-name']")
#     for i in LaptopAccessories:
#         if (i.text == "WATANI PRE-BUILT PC"):
#             i.click()
#             break
#     sleep(2)
#
#
# def test23(driver):
#     LaptopAccessories = driver.find_elements(By.XPATH, ".//span[@class='category-name']")
#     for i in LaptopAccessories:
#         if (i.text == "MONITORS"):
#             i.click()
#             break
#     sleep(2)

#
# def test24(driver):
#     LaptopAccessories = driver.find_elements(By.XPATH, ".//span[@class='category-name']")
#     for i in LaptopAccessories:
#         if (i.text == "COMPUTER CPU"):
#             i.click()
#             break
#     sleep(2)
#
#
# def test25(driver):
#     LaptopAccessories = driver.find_elements(By.XPATH, ".//span[@class='category-name']")
#     for i in LaptopAccessories:
#         if (i.text == "MOTHERBOARDS"):
#             i.click()
#             break
#     sleep(2)
#def test29(driver):
#     fakepass="123123123"
#     for i in range(10):
#         profile_pic = driver.find_element(By.CLASS_NAME, "icon-user")
#         profile_pic.click()
#         sleep(3)
#         emailBox = driver.find_element(By.ID, "login_email")
#         emailBox.send_keys("189c0c556b@emaily.pro")
#         passBox = driver.find_element(By.ID, "login_password")
#         passBox.send_keys(fakepass)
#         sleep(2)
#         LoginPopUp1 = driver.find_element(By.CLASS_NAME,"login-modal")
#         btn_login = driver.find_element(By.CLASS_NAME, "btn.btn-login")
#         btn_login.click()
#         sleep(6)
#         LoginPopUp3 = driver.find_element(By.CLASS_NAME,"login-modal")
#         assert LoginPopUp1 != LoginPopUp3, "Test Failed: Error message not found."
#         sleep(3)
#         profile_pic = driver.find_element(By.CLASS_NAME, "icon-user")
#         profile_pic.click()
#         logoutbtn = driver.find_element(By.CLASS_NAME,"woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout")
#         logoutbtn.click()
#         sleep(3)

# def test34(driver):
#     LaptopAccessories = driver.find_elements(By.XPATH, ".//span[@class='category-name']")
#     for i in LaptopAccessories:
#         if (i.text == "laptop"):
#           i.click()
#           break
#     sleep(2)
#     btn_addCart = driver.find_element(By.XPATH, '//a[@data-id="179666"]')
#     actions = ActionChains(driver)
#     actions.move_to_element(btn_addCart).perform()
#     sleep(2)
#     btn_addCart.click()
#     cart_icon = driver.find_elem*ent(By.XPATH, ".//span[@class='counter']")
#     cart_icon.click()
#     sleep(4)
#     cart_product = driver.find_element(By.XPATH,"//a[@href='https://watanimall.com/product/dell-vostro-v3530-15-6-fhd-i5-1334u-ram16-ssd512-dos/']")
#     cart_product_text = cart_product.text
#     cart_product.click()
#     sleep(2)
#     ProductAfterClick = driver.find_element(By.XPATH, ".//h1[@class='product_title entry-title']")
#     assert cart_product_text != ProductAfterClick.text, "Test Failed: Error message not found."
#     LaptopAccessories = driver.find_elements(By.XPATH, ".//span[@class='category-name']")
#     for i in LaptopAccessories:
#         if (i.text == "laptop"):
#           i.click()
#           break
#     firstlaptop = driver.find_element(By.CLASS_NAME, "woocommerce-placeholder.wp-post-image")
#     FilterByPrice=driver.find_elements(By.CLASS_NAME,"filter-group-title.d-flex.flex-column")
#     for i in FilterByPrice:
#         if(i.text == "Manufacturer"):
#             i.click()
#             break
#     sleep(3)
#     Selection = driver.find_element(By.CLASS_NAME,"label-text")
#     Selection.click()
#     for i in FilterByPrice:
#         if(i.text == "CPU / Processor"):
#             i.click()
#             break
#     sleep(3)
#     filter = driver.find_elements(By.CLASS_NAME,"label-text")
#     for i in filter:
#         if (i.text == "i3-1215U"):
#             i.click()
#             break
#     sleep(2)
#     gc = driver.find_elements(By.CLASS_NAME,"filter-group-title.d-flex.flex-column")
#     for i in gc:
#         if (i.text == "Graphics Card"):
#             i.click()
#             break
#     sleep(2)
#     for i in filter:
#         if (i.text == "Intel Iris Xe Graphics"):
#             i.click()
#             break
#     sleep(2)
#     clearbtn=driver.find_element(By.CLASS_NAME,"filter-link.clear_filter")
#     clearbtn.click()
#     sleep(10)
#     firstlaptop2= driver.find_element(By.CLASS_NAME, "woocommerce-placeholder.wp-post-image")
#     assert firstlaptop != firstlaptop2 , "Test Failed: Error message not found."
#

































