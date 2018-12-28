"""
This program is used to automate the Pomodoro technique
(a studying method for maximum productivity). Studying
sessions are split into increments with the studying block,
break block, and longer break block.
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/search?q=timer&oq=timer&aqs=chrome..69i57.1059j0j'
           '1&sourceid=chrome&ie=UTF-8')

counter = 0
num_study_sessions_before_longer_break = 4
# Do not enter a time lower than 1 minute.
study_session_time_in_min = 25
break_session_time_in_min = 5
longer_break_session_time_in_min = 15

while True:
    if (counter % num_study_sessions_before_longer_break) != 0 or counter == 0:

        """ Study session code """
        # Entering time, adding 2 zeros to represent seconds
        driver.find_element_by_xpath('//*[@id="act-timer-section"]/div/div[1]/input') \
            .send_keys(str(study_session_time_in_min * 100))
        print('Entering time for {} minute(s).'.format(study_session_time_in_min))
        print('Study session begins now.')
        driver.find_element_by_xpath('//*[@id="act-timer-section"]/div/div[2]/span[1]'
                                     '/g-button[1]/span[2]').click()  # START button
        # Converts time to seconds and adds 2 more seconds for user to hear alarm sound
        time.sleep((study_session_time_in_min * 60) + 2)
        counter += 1
        driver.find_element_by_xpath('//*[@id="act-timer-section"]/div/div[2]/span[1]'
                                     '/g-button[2]').click()  # RESET button
        print('Study session has ended.')
        print('Total number of study sessions so far: {}'.format(counter))

        driver.refresh()

        if (counter % num_study_sessions_before_longer_break) != 0:
            """ Break session code """

            driver.find_element_by_xpath('//*[@id="act-timer-section"]/div/div[1]/input') \
                .send_keys(str(break_session_time_in_min * 100))  # Entering time
            print('Entering time for {} minute(s).'.format(break_session_time_in_min))
            print('Break session begins now.')
            driver.find_element_by_xpath('//*[@id="act-timer-section"]/div/div[2]/span[1]'
                                         '/g-button[1]/span[2]').click()  # START button
            time.sleep((break_session_time_in_min * 60) + 2)
            driver.find_element_by_xpath('//*[@id="act-timer-section"]/div/div[2]/span[1]'
                                         '/g-button[2]').click()  # RESET button
            print('Break session has ended.')

    else:

        """ Longer break session code """

        driver.find_element_by_xpath('//*[@id="act-timer-section"]/div/div[1]/input') \
            .send_keys(str(longer_break_session_time_in_min * 100))  # Entering time
        print('Entering time for {} minute(s).'.format(longer_break_session_time_in_min))
        print('Longer break session begins now.')
        driver.find_element_by_xpath('//*[@id="act-timer-section"]/div/div[2]/span[1]'
                                     '/g-button[1]/span[2]').click()  # START button
        time.sleep((longer_break_session_time_in_min * 60) + 2)
        counter = 0
        driver.find_element_by_xpath('//*[@id="act-timer-section"]/div/div[2]/span[1]'
                                     '/g-button[2]').click()  # RESET button
        print('Longer break session has ended.')

    driver.refresh()
