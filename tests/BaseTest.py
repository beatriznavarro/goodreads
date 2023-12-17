import unittest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from pages.BasePage import BasePage
from pages.MyBooks import MyBooks

class BaseTest(unittest.TestCase):
    def setUp(self)-> None:
        options = AppiumOptions()
        options.load_capabilities({
            'platformName': 'Android',
            'noReset': True, 
            'appPackage': "com.goodreads",
            'appActivity': ".kindle.ui.activity.RoutingActivity",
            'automationName': 'UiAutomator2',
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True})
        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        self.driver.implicitly_wait(10) 
        #Swipe dava erro no primeiro teste, como solução adicionei esses dois passos de navegação no setup
        MyBooks.openMyBooks(self)
        BasePage.swipe_down(self)

    def tearDown(self):
        if self.driver:
            self.driver.quit()



















