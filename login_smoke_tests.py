from decouple import config
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait
username = config('VUSER')
password = config('PASS')
f = open("results.txt", "a+")
timestamp = datetime.now()

class TestLoginTest():
    def setup_method(self, method):
        self.driver = webdriver.Chrome("/Users/richard/chromedriver")
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_valid(self):
        try:
            driver = self.driver
            f = open("results.txt", "a+")
            f.write("test_valid_login: " + str(timestamp) + "\n")
            driver.get("https://www.votervoice.net/AdminSite/Login")
            driver.set_window_size(1200, 988)
            Wait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
            print(username)

            step = 1
            driver.find_element(By.NAME, "username").send_keys(username)
            if driver.find_element(By.NAME, "username").get_attribute("value") != username:
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")
                step = None
                raise Exception()
            f.write("   Test Step " + str(step) + " = " + "PASS\n")
            step += 1
            driver.find_element(By.NAME, "password").send_keys(password)
            print(password)
            if driver.find_element(By.NAME, "password").get_attribute("value") != password:
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")
                step = None
                raise Exception()
            f.write("   Test Step " + str(step) + " = " + "PASS\n")

            step += 1
            driver.find_element_by_xpath("//button[@type='submit']").click()
            Wait(driver, 10).until(EC.url_to_be("https://www.votervoice.net/AdminSite/LA8AAA/Dashboard"))
            Wait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='contentarea']/div/div[1]/label")))
            if not driver.find_element(By.XPATH, "//*[@id='contentarea']/div/div[1]/label").get_attribute(
                    "innerHTML") == "Dashboard":
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")
                step = None
                raise Exception()
            f.write("   Test Step " + str(step) + " = " + "PASS\n")

            step += 1
            driver.find_element_by_xpath("//*[@id='adminName']").click()
            while driver.find_element_by_xpath("//*[@id='adminOptions']").get_attribute("style") == "display: none;":
                driver.implicitly_wait(1)
                print("Waited")
            driver.find_element_by_xpath("//*[@id='logout']").click()
            Wait(driver, 10).until(EC.url_to_be("https://www.votervoice.net/AdminSite/Login?error=notauthorized"))
            Wait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
            if not driver.find_element(By.NAME, "username"):
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")
                step = None
                raise Exception()
            f.write("   Test Step " + str(step) + " = " + "PASS\n")
            f.write("Test Result = " + "PASS\n")
            driver.quit()
        except:
            if step is not None:
                f.write("   Test Step " + str(step) + " = " + "BLOCKED\n")
                f.write("Test Result = " + "BLOCKED\n")
                driver.quit()
            else:
                f.write("Test Result = " + "FAIL\n")
                driver.quit()

    def test_invalid_login(self):
        self.driver.get("https://www.votervoice.net/AdminSite/Login")

    def test_empty_pass(self):
        self.driver.get("https://www.votervoice.net/AdminSite/Login")

    def test_empty_user(self):
        self.driver.get("https://www.votervoice.net/AdminSite/Login")

    def test_empty_user_pass(self):
        self.driver.get("https://www.votervoice.net/AdminSite/Login")
