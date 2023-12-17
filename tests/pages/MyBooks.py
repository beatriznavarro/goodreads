from pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyBooks(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def openMyBooks(self):
        el = self.driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@resource-id=\"com.goodreads:id/navigation_bar_item_icon_view\"])[2]")
        el.click()

    def createTag(self,tagName):
        BasePage.swipe_down(self)
        el1 = self.driver.find_element(by=AppiumBy.ID, value="com.goodreads:id/button")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.goodreads:id/tag_or_shelf_name")
        el2.click()
        el2.send_keys(tagName)
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ID, value="com.goodreads:id/save")
        el3.click()

    def createBookshelf(self,bookshelfName):
        BasePage.swipe_down(self)
        el1 = self.driver.find_element(by=AppiumBy.ID, value="com.goodreads:id/button")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.goodreads:id/radio_shelf")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ID, value="com.goodreads:id/tag_or_shelf_name")
        el3.click()
        el3.send_keys(bookshelfName)
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="com.goodreads:id/save")
        el4.click()

    def deleteBookshelf(self,bookshelfName):
        el1 =  self.driver.find_element(by=AppiumBy.XPATH,  value="//android.widget.TextView[@resource-id=\"com.goodreads:id/shelf_name\" and @text=\""+ bookshelfName + "\"]")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Mais opções")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.goodreads:id/title\" and @text=\"Excluir\"]")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="android:id/button1")
        el4.click()

    def deleteBookshelfWithBook(self,bookshelfName):
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Mais opções")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.goodreads:id/title\" and @text=\"Excluir\"]")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="android:id/button1")
        el4.click()

    def isSucessMessageVisible(self):
        success_message_locator = (By.ID, 'com.goodreads:id/snackbar_text')
        try:
            # Esperar até que a mensagem de sucesso esteja visível
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(success_message_locator))
            return True
        except:
            # Se a mensagem não estiver visível dentro do tempo limite, retornar False
            return False

    def openBook(self, name):
        el = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.goodreads:id/book_title\" and @text=\""+ name+ "\"]")
        el.click()

    def openBookshelf(self,bookshelfName):
        el = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.goodreads:id/shelf_name\" and @text=\"" + bookshelfName +"\"]")
        el.click()

    def addTag(self,tagName):
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Opções de estantes.")
        el1.click()
        el4 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.goodreads:id/shelf_tag_name\" and @text=\"my-new-tag\"]")
        el4.click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Salvar")
        el3.click()

    def openTag(self):
        el4 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.goodreads:id/shelf_tag_name\" and @text=\"my-new-tag\"]")
        el4.click()

    def deleteTagWithBook(self):
        # MyBooks.openMyBooks(self)
        # el4 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.goodreads:id/shelf_tag_name\" and @text=\"my-new-tag\"]")
        # el4.click()
        #el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Mais opções")
        el2 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView[@content-desc='Mais opções']")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.goodreads:id/title\" and @text=\"Excluir\"]")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="android:id/button1")
        el4.click()
        
    def addBookshelf(self,bookshelfName):     
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Opções de estantes.")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.goodreads:id/shelf_name\" and @text=\"my-new-bookshelf\"]")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Salvar")
        el3.click()
   