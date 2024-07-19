# import frameworks
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# closing webApp
options = Options()
options.add_experimental_option("detach", True)



class testCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        self.driver.maximize_window()
        self.driver.get("https://jupiter.cloud.planittesting.com/#/home")
        self.wait = WebDriverWait(self.driver,10)
        self.waitTwentySec = WebDriverWait(self.driver, 20)

    def test1(self):
        self.links = self.driver.find_elements(By.XPATH, "//a[@href]")
        for Contact in self.links:
            if "Contact" in Contact.get_attribute("innerHTML"):
                Contact.click()
                break

        self.submit_button = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Submit")))
        self.submit_button.click()
        foremanErr = self.wait.until(EC.visibility_of_element_located((By.ID, "forename-err")))
        emailErr = self.wait.until(EC.visibility_of_element_located((By.ID, "email-err")))
        messageErr = self.wait.until(EC.visibility_of_element_located((By.ID, "message-err")))
        if foremanErr.is_displayed() | emailErr.is_displayed() | messageErr.is_displayed():
            print("Error Message Verified")

        forename_Field = self.wait.until(EC.visibility_of_element_located((By.ID, "forename")))
        if forename_Field.is_displayed():
            forename_Field.send_keys("Mark")

        email_Field = self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
        if email_Field.is_displayed():
            email_Field.send_keys("Mark@gmail.com")

        message_Field = self.wait.until(EC.visibility_of_element_located((By.ID, "message")))
        if message_Field.is_displayed():
            message_Field.send_keys("Hello World")

        foremanErr = self.driver.find_elements(By.ID, "forename-err")
        if foremanErr:
            print("Error Message Verified")
        else:
            print("Error Message Gone")

    def test2(self):
        self.links = self.driver.find_elements(By.XPATH, "//a[@href]")
        for Contact in self.links:
            if "Contact" in Contact.get_attribute("innerHTML"):
                Contact.click()
                break

        forename_Field = self.wait.until(EC.visibility_of_element_located((By.ID, "forename")))
        if forename_Field.is_displayed():
            forename_Field.send_keys("Mark")

        email_Field = self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
        if email_Field.is_displayed():
            email_Field.send_keys("Mark@gmail.com")

        message_Field = self.wait.until(EC.visibility_of_element_located((By.ID, "message")))
        if message_Field.is_displayed():
            message_Field.send_keys("Hello World")

        self.submit_button = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Submit")))
        self.submit_button.click()

        success = self.waitTwentySec.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-success")))
        if success.is_displayed():
            print("Success Message Appeared")
        else:
            print("No Success Message")

    def test3(self):
        self.links = self.driver.find_elements(By.XPATH, "//a[@href]")
        for Shop in self.links:
            if "Shop" in Shop.get_attribute("innerHTML"):
                Shop.click()
                break

        self.stuffedFrog = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/ul/li[2]/div/p/a")))
        self.stuffedFrog.click()
        self.stuffedFrog.click()

        self.fluppyBunny = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/ul/li[4]/div/p/a")))
        self.fluppyBunny.click()
        self.fluppyBunny.click()
        self.fluppyBunny.click()
        self.fluppyBunny.click()
        self.fluppyBunny.click()

        self.valentineBear = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/ul/li[7]/div/p/a")))
        self.valentineBear.click()
        self.valentineBear.click()
        self.valentineBear.click()

        self.cart = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/ul[2]/li[4]/a")))
        self.cart.click()

        self.stuffedFrogSubtotal = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/form/table/tbody/tr[1]/td[4]"))).text

        self.stuffedFrogPrice = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/form/table/tbody/tr[1]/td[2]"))).text

        self.fluffyBunnySubtotal = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/form/table/tbody/tr[2]/td[4]"))).text

        self.fluffyBunnyPrice = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/form/table/tbody/tr[2]/td[2]"))).text

        self.valentineBearSubtotal = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/form/table/tbody/tr[3]/td[4]"))).text

        self.valentineBearPrice = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/form/table/tbody/tr[3]/td[2]"))).text

        self.total = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/form/table/tfoot/tr[1]/td/strong"))).text

        if self.stuffedFrogSubtotal == "$21.98":
            print("Correct Stuffed Frag Subtotal")
        if self.fluffyBunnySubtotal == "$49.95":
            print("Correct Fluffy Bunny Subtotal")
        if self.valentineBearSubtotal == "$44.97":
            print("Correct Valentine Bear Subtotal")
        if self.stuffedFrogPrice == "$10.99":
            print("Correct Stuffed Frag Price")
        if self.fluffyBunnyPrice == "$9.99":
            print("Correct Fluffy Bunny Price")
        if self.valentineBearPrice == "$14.99":
            print("Correct Valentine Bear Price")
        if self.total == "Total: 116.9":
            print("Total is Correct")


    def tearDown(self):
        time.sleep(5)
        self.driver.quit()


def main():
    count = 0
    while count < 5:
        a = testCases()
        a.setUp()
        a.test1()
        a.tearDown()

        a.setUp()
        a.test2()
        a.tearDown()

        a.setUp()
        a.test3()
        a.tearDown()
        count = count + 1
if __name__ == '__main__':
    main()












