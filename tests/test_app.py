import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FlaskAppTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
        cls.driver.get("http://127.0.0.1:5000/")
        time.sleep(2)  # Wait for the page to load

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_home_page(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")  # Ensure navigation to the home page
        time.sleep(2)
        print("Home Page title:", driver.title)
        self.assertIn("Home Page", driver.title)
        header = driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(header.text, "Welcome to the Home Page!")

    def test_about_page(self):
        driver = self.driver
        link = driver.find_element(By.LINK_TEXT, "Go to About Page")
        link.click()
        time.sleep(2)  # Wait for the page to load
        print("About Page title:", driver.title)
        self.assertIn("About Page", driver.title)
        header = driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(header.text, "Welcome to the About Page!")

if __name__ == "__main__":
    unittest.main()
