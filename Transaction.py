from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import codecs, os, time
import urllib.request
from bs4 import BeautifulSoup as bs
import pause, datetime

def execute_trades(position):

    options = Options()
    options.add_argument("user-data-dir=C:\\Users\\jesse\\AppData\\Local\\Google\\Chrome\\User Data")


    # https://stackoverflow.com/questions/45651879/using-selenium-how-to-keep-logged-in-after-closing-driver-in-python
    browser = webdriver.Chrome('chromedriver.exe', options=options)
    browser.get("https://www.predictit.org/markets/detail/5676/What-will-Bernie-Sanders'-social-media-support-rank-be-on-July-17,-2019")

    options = browser.find_elements_by_class_name("market-contract-horizontal-v2")

    #which
    to_buy = options[position]

    buy_yes_1 = to_buy.find_element_by_class_name("market-contract-horizontal-v2__button-single--buy-yes")
    buy_yes_1.click()

    input_box = browser.find_element_by_class_name("purchase-quantity-value__input")
    input_box.send_keys('100')

    next_button = browser.find_element_by_class_name("purchase-offer-desktop__footer-next-button")
    next_button.click()

    # submit_button = browser.find_element_by_class_name("button button--primary button--full-width purchase-review-and-confirm__footer-next-button")
    time.sleep(5)

    submit = browser.find_element_by_class_name("purchase-review-and-confirm__footer-summary-right")
    submit_button = submit.find_element_by_class_name("button")

    submit_button.click()
    pause.seconds(5)
    print("Exiting")

def get_standings():
    # https://scottrasmussen.com/2020-democratic-candidate-social-media-analysis/
    link = 'https://scottrasmussen.com/2020-democratic-candidate-social-media-analysis/'

    while True:
        page = urllib.request.urlopen(link)
        soup = bs(page, 'html.parser')
        refresh_date = soup.body.findAll(text='last updated at 04:30EST on 07-17-2019')
        if len(refresh_date) > 0:
            break
        else:
            print("Refresh date incorrect")
            pause.seconds(15)

    print("Refresh date good continuing")

    table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="demtable")
    rows = table.findAll(lambda tag: tag.name=='tr')
    for i in range(0, len(rows)):
        if rows[i].find('td').text == "Bernie Sanders":
            return i

def wait():

    timer = datetime.datetime(2019, 7, 17, 4, 29)
    print("Starting Wait", datetime.datetime.now())
    pause.until(timer)
    print("Finished Wait", datetime.datetime.now())

#do waiting
# pause.hours(2)
# pause.minutes(30)
# pause.minutes(3)
# pause.seconds(20)
wait()
position = get_standings()

print("Found Sanders in position ", position)
#
execute_trades(position)

