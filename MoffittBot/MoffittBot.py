"""
This program will automate reserving a study room from Moffitt's 5th floor.
Current program time takes an average of 30 seconds, but is largely dependent
on individual computers. This program requires you to have your phone ready
to authenticate your Cal Net login and to enter your information in Info.py.
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from Info import keys
import datetime as dt
import time


def booking():
    """
    Uses the desired time slots and login credentials in info.py to
    reserve the study rooms.
    """
    driver.execute_script("window.open('https://berkeley.libcal.com/booking/moffitt-5');")
    driver.switch_to.window(driver.window_handles[1])
    print('Fetching web page...')

    """
    @source Found how to wait for a web element to load before clicking it. 
    This is efficient since loading time is dependent on individual computers.
    https://stackoverflow.com/questions/26566799/wait-until-page-is-loaded-with-selenium-webdriver-for-python
    """
    element_present = ec.presence_of_element_located((By.XPATH, '//*[@id="s-lc-rm-cal"]/div/table/tbody/tr[3]/td[4]/a'))
    WebDriverWait(driver, keys['timeout_sec']).until(element_present).click()

    print('Finding desired study rooms...')
    time.sleep(1)  # Delay needed because driver is sometimes too fast

    try:
        element_present = ec.presence_of_element_located((By.XPATH, '//*[@id="660555210"]'))  # 10:00
        WebDriverWait(driver, keys['timeout_sec']).until(element_present).click()

        """ 
        NOTE: We do not need a WedDriverWait instance here because the first
        instance for 10:00 automatically loads subsequent time slots on the page.
        """
        driver.find_element_by_xpath('//*[@id="660555211"]').click()  # 11:00
    except Exception:
        print('Specified rooms are currently booked or unavailable. Try entering a different time slot.')
        driver.quit()
        exit()

    driver.find_element_by_xpath('//*[@id="rm_tc_cont"]').click()  # Continue Button
    driver.find_element_by_xpath('//*[@id="s-lc-rm-sub"]').click()  # Submit Time Slots Button
    print('Submitting reservation for desired time slots...')

    """
    Information Release Window
    """
    element_present = ec.presence_of_element_located((By.XPATH, '/html/body/form/div/div[2]/p[2]/input[2]'))
    WebDriverWait(driver, keys['timeout_sec']).until(element_present).click()  # Information Release Window
    print('Accepting information release terms and agreement...')
    driver.find_element_by_xpath('//*[@id="s-lc-rm-sub"]').click()  # Accept Button

    driver.find_element_by_xpath('//*[@id="s-lc-rm-sub"]').click()  # Submit Booking button
    element_present = ec.element_to_be_clickable((By.XPATH, '//*[@id="s-lc-rm-auth-retbb"]'))
    WebDriverWait(driver, keys['timeout_sec']).until(element_present).click()
    print('Booking successfully reserved! Check your email to confirm your booking.')
    element_present = ec.presence_of_element_located((By.XPATH, '//*[@id="s-lc-rm-cal"]/div/table/tbody/tr[3]/td[4]/a'))
    WebDriverWait(driver, keys['timeout_sec']).until(element_present).click()


def cal_net_authentication():
    """
    Automated Cal Net Authentication. Make sure to have your phone ready at hand.
    """
    print('Entering two-step authentication...')
    element_present = ec.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
    WebDriverWait(driver, keys['timeout_sec']).until(element_present).send_keys(keys['cal_net_username'])  # Username
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(keys['cal_net_password'])  # Password
    driver.find_element_by_xpath('//*[@id="loginForm"]/fieldset/p[4]/input[4]').click()  # Login Button
    driver.switch_to.frame('duo_iframe')
    element_present = ec.visibility_of_element_located((By.XPATH, '//*[@id="login-form"]/fieldset[2]/div[1]/button'))
    WebDriverWait(driver, keys['timeout_sec']).until(element_present).click()  # Send Push
    print('Please authenticate the session on your phone.')


def login_prep():
    """
    Logs into Berkeley email and Cal Net account.
    """
    driver.get('https://accounts.google.com/ServiceLogin/identifier?service=mail&continue=https%3A%2F%2Fmail.'
               'google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AddSession')
    print('Logging into your Berkeley email...')
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(keys['berkeley_email'])
    driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
    cal_net_authentication()
    print('Authentication successful.')
    element_present = ec.presence_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/'
                                                                'div[2]/div/div[1]/div/content/span'))
    WebDriverWait(driver, keys['timeout_sec']).until(element_present).click()


def waiting_period():
    """
    @source Learned how to use Python's built-in datetime module
    https://www.youtube.com/watch?v=eirjjyP2qcQ
    """
    curr_time = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day,
                            dt.datetime.now().hour, dt.datetime.now().minute, dt.datetime.now().second)
    des_time = dt.datetime(keys['desired_year'], keys['desired_month'], keys['desired_day'], keys['desired_hour'],
                           keys['desired_minute'], keys['desired_second'])
    change_in_time = (des_time - curr_time).total_seconds()
    if change_in_time < 0:
        print('Please enter a valid time.')
        exit()
    print('Program starting in {} second(s).'.format(change_in_time))
    time.sleep(change_in_time + 10.0)  # 10 second buffer for library page to match system time.


if __name__ == '__main__':
    waiting_period()
    start_time = time.time()
    driver = webdriver.Chrome()
    login_prep()
    print('Successfully logged in.')
    booking()
    print("--- {} seconds ---".format(time.time() - start_time))
