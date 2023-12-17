from pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class SearchBook(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def searchByText(self,text):
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Caixa de edição: toque duas vezes para pesquisar livros, títulos, autores ou ISBNs")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.goodreads:id/search_text")
        el2.click()
        el2.send_keys(text)
        el2.click()
        
    def openBook(self):
       el = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ListView[@resource-id=\"android:id/list\"]/android.widget.RelativeLayout")
       el.click()

    def checkBookTitle(self,expected_title):
        try:
            el = self.driver.find_element(by=AppiumBy.ID, value="com.goodreads:id/book_info_title")
            element_text = el.text
            return element_text == expected_title
        except Exception as e:
            print(f"Erro ao verificar o texto do elemento: {e}")
            return False
        
    def checkBookTitleTagOrBookshelf(self,expected_title):
        try:
            el = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='com.goodreads:id/book_title']")
            element_text = el.text
            return element_text == expected_title
        except Exception as e:
            print(f"Erro ao verificar o texto do elemento: {e}")
            return False
  