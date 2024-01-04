# AUTOMATION
# SELENIUM

from selenium import webdriver
import time

from main import userName,passwd
browser = webdriver.Firefox("./")

#print(browser.page_source)
#print(browser.title)
#browser.fullscreen_window()
#time.sleep(2)
#browser.set_window_size(1980,1200)
#browser.save_screenshot("screenshot.png")
#browser.get("https://yandex.com/")
#time.sleep(2)
#browser.back()
#browser.quit()
browser.get("https://google.com/")

searching_field = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
searching_field.send_keys("youtube.com")

search_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]")
search_button.click()
'''
youtube = browser.find_element_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a/h3")
youtube.click()

youtube_searchButton = browser.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon")
youtube_searchButton.send_keys("Saud Abdul Wahed")

search = browser.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon")
search.click()

channel = browser.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-renderer[1]/div/div[1]/a")
channel.click()

videos_page = browser.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[2]/div")
videos_page.click()

python = browser.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[2]/div")
python.click()

'''
