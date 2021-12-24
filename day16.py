from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="D:\\PyCharm 2020.1\\chromedriver.exe")

# 操作弹窗
# driver.get(r"C:/Users/墨小白/Desktop/练习的html/练习的html/弹框的验证/dialogs.html")
# driver.find_element_by_id("confirm").click()
# # driver.switch_to.alert.accept()  # 点击确定
# driver.switch_to.alert.dismiss()  # 点击取消

# 跳转页面操作
# driver.get(r"C:/Users/墨小白/Desktop/练习的html/练习的html/跳转页面/pop.html")
# driver.find_element_by_id("goo").click()
# a = driver.window_handles  # 获取窗口元素
# driver.switch_to.window(a[-1]) # 跳入指定窗口
# driver.find_element_by_id("kw").send_keys("迪迦")
# driver.find_element_by_id("su").click()

# 滑块的验证
# driver.get(r"C:/Users/墨小白/Desktop/练习的html/练习的html/滑动验证/mousedrag.html")
# try:
#     a=driver.find_element_by_xpath("/html/body/div")#把滑块打包
#     ac=ActionChains(driver)#把driver交给事件链执行
#     # ac来驱动鼠标  点住 滑块包. 从300滑倒0   .立即执行
#     ac.click_and_hold(a).move_by_offset(300,0).perform()#立即执行
# except:
#     driver.save_screenshot("a.png")

# 苏宁易购
driver.get(r"http://www.suning.com")
# a = driver.window_handles
# driver.switch_to.window(a[-1])
# driver.find_element_by_id("searchKeywords").send_keys("小米")
# driver.find_element_by_id("searchSubmit").click()
# driver.find_element_by_name("ssdsn_search_pro_name03-1_0_0_12349196510_0000000000").click()
# a = driver.window_handles
# driver.switch_to.window(a[-1])
# driver.find_element_by_id("addCart").click()
# driver.find_element_by_name("cart1_go").click()
a = driver.find_element_by_name("utf-8_homepagev8_126605238630_word01")
ActionChains(driver).move_to_element(a).perform()
time.sleep(1)
# driver.find_element_by_id()
driver.find_element_by_link_text("空调").click()

# from time import ctime, sleep
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains

# 百度鼠标悬停
# driver.get("http://www.baidu.com")
# y = driver.find_element_by_id("s-usersetting-top")  # 建议使用1.1.2方法
# ActionChains(driver).move_to_element(y).perform()  # 移动到设置
# time.sleep(1)
# driver.find_element_by_link_text("高级搜索").click()  # 弹出菜单后点击
# time.sleep(5)
# driver.quit()

# time.sleep(3)
# driver.quit()