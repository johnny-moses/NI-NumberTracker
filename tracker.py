from selenium import webdriver
import time
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import schedule

# m_date = datetime.now().time()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
b = webdriver.Chrome('PATH/to/ChromeDriver', options=chrome_options)


def line():
    print('=' * 100)

def space():
    print(' ')


def login():  # CHANGE HERE PER STATION
    space()
    print('*============*')
    print('| Logging in |')
    print('*============*')
    space()
    b.find_element_by_xpath('//*[@id="ap_email"]').send_keys('*EMAIL*', '\n')
    time.sleep(2)
    b.find_element_by_xpath('//*[@id="ap_password"]').send_keys('*PASSWORD*')  # , '\n')
    b.find_element_by_xpath('//*[@id="authportal-main-section"]/div[2]/div/div/div/form/div/div['
                            '2]/div/div/label/div/label/input').click()
    b.find_element_by_xpath('//*[@id="signInSubmit"]').click()
    space()
    print('*==================*')
    print('| Login Successful |')
    print('*==================*')
    space()


def logincheck():
    b.refresh()
    url = b.current_url
    if url[:32] == '*SIGN IN PAGE*':
        print('*=================*')
        print('| Logging back in |')
        print('*=================*')
        space()
        b.find_element_by_xpath('//*[@id="ap_password"]').send_keys('*PASSWORD*')
        time.sleep(1)
        b.refresh()

    else:
        print('*=================*')
        print('| No login needed |')
        print('*=================*')
        space()
        return


def nums():
    x = b.current_url
    logincheck()
    d_t = datetime.now().strftime("%I:%M:%S")
    try:
        if x[-8:] == 'evaluate' and x[:32] != '*SIGN IN PAGE*':
            client = MongoClient('*MONGODB*')
            db = client["*MONGODB*"]
            collection = db["*MONGOCOLLECTION*"]
            time.sleep(2)
            total = b.find_element_by_xpath('//*[@id="rootDiv"]/div[3]/div/div[1]/div')
            tstring = total.text
            intstring = int(tstring[20:])
            avg = intstring / 60
            # CHANGE HERE PER STATION
            collection.update_one({"station": "7"}, {"$set": {"time": d_t}})
            collection.update_one({"station": "7"}, {"$set": {"total": intstring}})
            collection.update_one({"station": "7"}, {"$set": {"average": avg}})
            client.close()
            print('*======================================*')
            print('| Numbers sent to database @ ' + d_t + ' |')
            print('*======================================*')
            space()
            print(intstring)

        else:
            print('*=======================================*')
            print('| Items Scanned not Available: ' + d_t + ' |')
            print('*=======================================*')
            space()

    except ServerSelectionTimeoutError:
        print('*=================================*')
        print('| Server not available @ ' + d_t + ' |')
        print('*=================================*')
        space()


b.get('*WORK PAGE*')
line()
time.sleep(2)
login()
nums()
time.sleep(1)
schedule.every(45).seconds.do(nums)

while True:
    schedule.run_pending()
    time.sleep(1)
