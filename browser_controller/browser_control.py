import os
import datetime
import time
import sys

from browser_controller.speed_test import load_speed

from splinter import Browser
from termcolor import colored

URL = 'https://wwpre.multiply.co.za'
browser = Browser()
now = datetime.datetime.now()

print(colored('[###]', 'white'), colored('--------------------------------------------------------------', 'white'))
print(colored('[###]', 'white'), colored('Opening Browser', 'red'))
print(colored('[###]', 'white'), colored('Evaluating Browser Load Speed... please wait', 'red'))
load_speed = load_speed() + 1
print(colored('[###]', 'white'), colored('Page Load Speed Currently At {0} second(s)'.format(load_speed), 'red'))
print(colored('[###]', 'white'), colored('--------------------------------------------------------------', 'white'))


def screen_shot(name):
    try:
        print(colored('[LOG]', 'white'), colored('Taking A Screenshot', 'blue'))
        browser.driver.save_screenshot('screenshots/{0}-{1}.png'.format(name, now.date()))
    except Exception:
        print(colored('[ERR]', 'red'),
              colored('Execution failed at screen_shot()', 'red'))
        browser.quit()
        sys.exit()


def page_shot(page_name):
    try:
        pixels = [0, 300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000]
        n = 0
        for i in pixels:
            time.sleep(.5)
            browser.execute_script("window.scrollBy({0}, {1})".format(0, i))
            if browser.evaluate_script('(window.innerHeight + window.scrollY) >= document.body.scrollHeight'):
                print(colored('[LOG]', 'white'), colored('Reached End Of Page', 'blue'))
                break
            browser.driver.save_screenshot('screenshots/{0}-{1}-{2}.png'.format(page_name, i, now.date()))
            print(colored('[LOG]', 'white'), colored('Taking A Page Shot', 'blue'), n)
            n += 1
    except Exception:
        print(colored('[ERR]', 'red'),
              colored('Execution failed at page_shot()', 'red'))
        browser.quit()
        sys.exit()


def refresh():
    try:
        browser.execute_script("location.reload();")
        browser.execute_script("scroll(0,0);")
        print(colored('[LOG]', 'white'), colored('Refreshing Page... wait a few seconds', 'yellow'))
        time.sleep(load_speed)
    except Exception:
        print(colored('[ERR]', 'red'),
              colored('Execution failed at refresh()', 'red'))
        browser.quit()
        sys.exit()


def desktop():
    try:
        browser.driver.set_window_size(1024, 1500)
        print(colored('[LOG]', 'white'), colored('Set Window Size To Desktop', 'yellow'))
        refresh()
    except Exception:
        print(colored('[ERR]', 'red'),
              colored('Execution failed at desktop()', 'red'))
        browser.quit()
        sys.exit()


def tablet():
    try:
        browser.driver.set_window_size(768, 1500)
        print(colored('[LOG]', 'white'), colored('Set Window Size To Mobile', 'yellow'))
        refresh()
    except Exception:
        print(colored('[ERR]', 'red'),
              colored('Execution failed at tablet()', 'red'))
        browser.quit()
        sys.exit()


def mobile():
    try:
        browser.driver.set_window_size(400, 1500)
        print(colored('[LOG]', 'white'), colored('Set Window Size To Mobile', 'yellow'))
        refresh()
    except Exception:
        print(colored('[ERR]', 'red'),
              colored('Execution failed at mobile()', 'red'))
        browser.quit()
        sys.exit()


def login(username, password):
    try:
        print(colored('[###]', 'white'), colored('Logging in with {0}'.format(username), 'red'))
        browser.visit(URL)
        browser.find_by_text('LOGIN').click()
        browser.fill('username', username)
        browser.fill('password', password)
        browser.find_by_value('').click()
        if browser.evaluate_script('document.body.textContent.search("Oops!");') >= 1:
            print(colored('[WAR]', 'yellow'), colored('Failed To Log In', 'yellow'))
            print(colored('[###]', 'white'),
                  colored('--------------------------------------------------------------', 'white'))
            browser.quit()
            sys.exit()
        print(colored('[LOG]', 'white'), colored('Waiting For Page To Load... wait a few seconds', 'yellow'))
        time.sleep(load_speed)
        return 0
    except:
        print(colored('[ERR]', 'red'),
              colored('Execution failed at login()', 'red'))
        browser.quit()
        sys.exit()


def btn_with_text(text):
    try:
        browser.find_by_text(text).click()
        print(colored('[LOG]', 'white'), colored('Navigating By Button {0}'.format(text), 'green'))
    except Exception:
        print(colored('[ERR]', 'red'),
              colored('Execution failed at btn_with_text()', 'red'))
        browser.quit()
        sys.exit()


def scroll_to_class(class_name):
    try:
        print(colored('[LOG]', 'white'), colored('Scrolling To {0}'.format(class_name), 'blue'))
        browser.execute_script("$(document.getElementsByClassName('{0}')).get(0).scrollIntoView();".format(class_name))
    except Exception:
        print(colored('[ERR]', 'red'),
              colored('Execution failed at scroll_to_class()', 'red'))
        browser.quit()
        sys.exit()


def scroll_to_id(id_name):
    try:
        print(colored('[LOG]', 'white'), colored('Scrolling To {0}'.format(id_name), 'blue'))
        browser.execute_script("$(document.getElementsById('{0}')).get(0).scrollIntoView();".format(id_name))
    except Exception:
        print(colored('[ERR]', 'red'),
              colored('Execution failed at scroll_to_id()', 'red'))
        browser.quit()
        sys.exit()


def nav_to(new_page='/engaged/home'):
    try:
        print(colored('[LOG]', 'white'), colored('Navigating To {0}'.format(new_page), 'green'))
        browser.visit('https://wwpre.multiply.co.za{0}'.format(new_page))
        print(colored('[LOG]', 'white'), colored('Waiting For Page To Load... wait a few seconds', 'yellow'))
        time.sleep(load_speed)
    except Exception:
        print(colored('[ERR]', 'red'),
              colored('Execution failed at nav_to()', 'red'))
        browser.quit()
        sys.exit()


def test_service():
    try:
        print(colored('[LOG]', 'white'), colored('Testing Page Service Condition', 'blue'))
        if browser.evaluate_script('document.body.textContent.search("nginx");') >= 1:
            print(colored('[WAR]', 'yellow'), colored('Page Bounce or nginx down', 'yellow'))
        elif browser.evaluate_script('document.body.textContent.search("Service Temporarily Unavailable");') >= 1:
            print(colored('[WAR]', 'yellow'), colored('Service Temporarily Unavailable', 'yellow'))
        elif browser.evaluate_script('document.body.textContent.search("Page Portlet Temporarily Unavailable");') >= 1:
            print(colored('[WAR]', 'yellow'), colored('Page Portlet Temporarily Unavailable', 'yellow'))
        elif browser.evaluate_script('document.body.textContent.search("Portlet temporarily unavailable");') >= 1:
            print(colored('[WAR]', 'yellow'), colored('Portlet temporarily unavailable', 'yellow'))
        else:
            print(colored('[RES]', 'white'), colored('Condition Good', 'blue'))
    except Exception:
        print(colored('[ERR]', 'red'),
              colored('Execution failed at test_service()', 'red'))
        browser.quit()
        sys.exit()


def end():
    path, dirs, files = next(os.walk("screenshots"))
    file_count = len(files)
    print(colored('[###]', 'white'), colored('--------------------------------------------------------------', 'white'))
    print(colored('[###]', 'white'), colored('Closing Browser', 'red'))
    print(colored('[###]', 'white'), colored('Page Load Speed Ended At {0} Second(s)'.format(load_speed), 'red'))
    print(colored('[###]', 'white'), colored('Tested URL {0}'.format(URL), 'red'))
    print(colored('[###]', 'white'), colored('Screenshots Taken {0}'.format(file_count), 'red'))
    print(colored('[###]', 'white'), colored('--------------------------------------------------------------', 'white'))
    browser.quit()
