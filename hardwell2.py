import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

#after parsing the URL link for each single, we store the URL into music_url variable

music_url='https://music.163.com/#/album?id=38299173'
desired_capabilities = DesiredCapabilities.CHROME.copy()
driver = webdriver.Chrome('C:\\Users\\themi\\Desktop\\chromedriver_win32\\chromedriver.exe',desired_capabilities=desired_capabilities)
driver.get(music_url)

#cookie is extremely important in this process. It is my only identifier. It also bypasses the authorization system, which is disabled by the server if I'm using automated web browser

name='MUSIC_U'
value='5e9b03e05649f4596785d3263cfbe395ca11528ff12602eba821bc33deebb17254c96c1a53b02de333f7976066421fdc7955a739ab43dce1'
print("adding cookie...")
driver.add_cookie({'name':name,'value':value})
print('added')

#refresh is needed so the cookie can be loaded
driver.refresh()
time.sleep(10)

#the page structure is wierd: the actual content is stored inside an iframe
driver.switch_to.frame(driver.find_element_by_id("g_iframe"))
add_to_favorite = driver.find_elements_by_xpath("//a[@data-res-id='38299173']")
add_to_favorite[2].click()
time.sleep(10)
final_click=driver.find_element_by_xpath("//li[@data-id='2382701309']")
final_click.click()

#now we've done it! All further needed is a loop to go through all the single!
#I'm so happy about it!