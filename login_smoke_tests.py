from decouple import config  # Used for getting Login Credentials
from datetime import datetime  # Used for Time stamping Test Results in Results file
from selenium import webdriver  # Used for communicating the python code over the selenium code to the chrome browser
from selenium.webdriver.common.by import By  # Used for indentifying elements By Xpath, Name, CSS_Selector, etc
from selenium.webdriver.support import expected_conditions as EC  # Used for waits and to specify the conditions
from selenium.webdriver.support.wait import WebDriverWait as Wait  # Used for waiting for certain elements to appear
username = config('VUSER')  # Sets the Username from .env in project
password = config('PASS')  # Sets the Password name from .env in project
timestamp = datetime.now()  # Sets the current date and time to the variable for Test Results
f = open("results.txt", "a+")  # Creates a file in which test results will be recorded to

class TestLoginTest():
    def setup_method(self):
        self.driver = webdriver.Chrome("/Users/richard/chromedriver") # Sets the location of the WebDriver that will be
        # needed

    def teardown_method(self):
        self.driver.quit()  # kills the browser after the test is finished

    def preconditions(self):
        # Pre-Conditions
        driver = self.driver
        driver.get("https://www.votervoice.net/AdminSite/Login")  # opens browser to Login page
        driver.set_window_size(1200, 988)  # Sets the size of the window to specified dimensions
        Wait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    def test_login_valid(self):  # Test Case: A user with valid login credentials is able to log into and out of their
        # account.
        try:
            # Pre-Conditions
            self.preconditions()
            driver = self.driver
            f.write("test_valid_login: " + str(timestamp) + "\n")  # writes a header on the file for the first case

            # Test Step 1: Input Username into Username Field
            step = 1
            driver.find_element(By.NAME, "username").send_keys(username)  # Identifies the username field and inputs
            # username
            if driver.find_element(By.NAME, "username").get_attribute("value") != username: # Check is made to ensure it
                #  was inputted correctly
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")  # Writes Step as FAIL to the Results file
                step = None
                raise Exception()  # With Step as None it passes this to the exception to write the Test Case as Fail
            f.write("   Test Step " + str(step) + " = " + "PASS\n")  # Writes Step as PASS to the Results file

            # Test Step 2: Input Password into Password Field
            step += 1
            driver.find_element(By.NAME, "password").send_keys(password)  # Identifies the password field and inputs
            # password
            if driver.find_element(By.NAME, "password").get_attribute("value") != password:
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")  # Writes Step as FAIL to the Results file
                step = None
                raise Exception()  # With Step as None it passes this to the exception to write the Test Case as Fail
            f.write("   Test Step " + str(step) + " = " + "PASS\n")  # Writes Step as PASS to the Results file

            # Test Step 3: Logging in brings the user to the Dashboard
            step += 1
            driver.find_element_by_xpath("//button[@type='submit']").click()  # Identifies the Login button and clicks
            # it
            Wait(driver, 10).until(EC.url_to_be("https://www.votervoice.net/AdminSite/LA8AAA/Dashboard"))  # Waits for
            # the Dashboard URL to be present
            Wait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='contentarea']/div/div[1]/label")))  # Waits until
            # the content area and possible Dashboard is present
            if not driver.find_element(By.XPATH, "//*[@id='contentarea']/div/div[1]/label").get_attribute(
                    "innerHTML") == "Dashboard":  #  Verifies that the user landed on the dashboard
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")  # Writes Step as FAIL to the Results file
                step = None
                raise Exception()  # With Step as None it passes this to the exception to write the Test Case as Fail
            f.write("   Test Step " + str(step) + " = " + "PASS\n")  # Writes Step as PASS to the Results file

            # Test Step 4: Logging Out Brings the User Back to the Login Page
            step += 1
            driver.find_element_by_xpath("//*[@id='adminName']").click()  # Identifies Admin Name drop down options and
            # clicks
            while driver.find_element_by_xpath("//*[@id='adminOptions']").get_attribute("style") == "display: none;":
                driver.implicitly_wait(1)
                print("Waited")  # Loops over the xpath until the style option represents the dropdown being present for
                #  next step.
            driver.find_element_by_xpath("//*[@id='logout']").click()  # Identifies the Logout option and clicks
            Wait(driver, 10).until(EC.url_to_be("https://www.votervoice.net/AdminSite/Login?error=notauthorized"))
            # Verifies that Login url page has been navigated to
            Wait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))  # Waits for Username field to
            #  be present
            if not driver.find_element(By.NAME, "username"):  # Extra verification to ensure landed on Login page
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")  # Writes Step as FAIL to the Results file
                step = None
                raise Exception()  # With Step as None it passes this to the exception to write the Test Case as Fail
            f.write("   Test Step " + str(step) + " = " + "PASS\n")  # Writes Step as PASS to the Results file
            f.write("Test Case Result = " + "PASS\n")  # Writes to the Results file that the Test Case has Passed
        except:
            if step is not None:  # A check on the variable step to see if it is not None
                f.write("   Test Step " + str(step) + " = " + "BLOCKED\n")  # Step is marked BLOCKED due to code failing
                #  outside of test parameters
                f.write("Test Case Result = " + "BLOCKED\n")  # Overall Test Case is marked block due to a Blocked Step
            else:
                f.write("Test Case Result = " + "FAIL\n")  # Test Case marked failed due to step variable is None and
                # Step has failed.

    def test_invalid_login(self):  # Test Case: A user with invalid login credentials will see an error when attempting
        # to log in.
        try:
            # Pre-Conditions
            self.preconditions()
            driver = self.driver
            f.write("test_invalid_login: " + str(timestamp) + "\n")
            # Test Step 1: Input Incorrect Username into Username Field
            step = 1
            driver.find_element(By.NAME, "username").send_keys("dummytest@test.com")
            if driver.find_element(By.NAME, "username").get_attribute("value") != "dummytest@test.com":
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")
                step = None
                raise Exception()
            f.write("   Test Step " + str(step) + " = " + "PASS\n")

            # Test Step 2: Input Incorrect Password into Password Field
            step += 1
            driver.find_element(By.NAME, "password").send_keys("1234abcd")
            if driver.find_element(By.NAME, "password").get_attribute("value") != "1234abcd":
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")
                step = None
                raise Exception()
            f.write("   Test Step " + str(step) + " = " + "PASS\n")

            # Test Step 3: Attempting to Login Results in Error Being Displayed
            step += 1
            driver.find_element_by_xpath("//button[@type='submit']").click()
            Wait(driver, 10).until(EC.visibility_of_element_located
                                   ((By.XPATH, "//*[contains(text(), 'Invalid UserName/Password Combination')]")))
            if driver.find_element_by_xpath\
                        ("//*[@id='contentarea']/div/router-view/div/div/div[1]/div/form/div[4]/loading-display/span")\
                    .get_attribute("innerHTML") != "Invalid UserName/Password Combination":
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")
                step = None
                raise Exception()
            f.write("   Test Step " + str(step) + " = " + "PASS\n")
            f.write("Test Case Result = " + "PASS\n")
        except:
            if step is not None:
                f.write("   Test Step " + str(step) + " = " + "BLOCKED\n")
                f.write("Test Case Result = " + "BLOCKED\n")
            else:
                f.write("Test Case Result = " + "FAIL\n")

    def test_empty_pass(self):  # Test Case: A user who leaves the password field blank will see an error message.
        try:
            # Pre-Conditions
            self.preconditions()
            driver = self.driver
            f.write("test_empty_pass: " + str(timestamp) + "\n")  # writes a header on the file for the first case

            # Test Step 1: Input Username into Username Field
            step = 1
            driver.find_element(By.NAME, "username").send_keys(
                username)  # Identifies the username field and inputs username
            if driver.find_element(By.NAME, "username").get_attribute(
                    "value") != username:  # Check is made to ensure it was inputted correctly
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")  # Writes Step as FAIL to the Results file
                step = None
                raise Exception()  # With Step as None it passes this to the exception to write the Test Case as Fail
            f.write("   Test Step " + str(step) + " = " + "PASS\n")  # Writes Step as PASS to the Results file

            # Test Step 2: Attempting to Login Results in Empty Password Error
            step += 1
            driver.find_element_by_xpath("//button[@type='submit']").click()
            Wait(driver, 10).until(EC.visibility_of_element_located
                                   ((By.XPATH, "//*[contains(text(), '* Require Password')]")))
            if driver.find_element_by_xpath(
                    "//*[@id='contentarea']/div/router-view/div/div/div[1]/div/form/div[2]") \
                    .get_attribute("innerHTML") != "* Require Password":
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")
                step = None
                raise Exception()
            f.write("   Test Step " + str(step) + " = " + "PASS\n")
            f.write("Test Case Result = " + "PASS\n")
        except:
            if step is not None:
                f.write("   Test Step " + str(step) + " = " + "BLOCKED\n")
                f.write("Test Case Result = " + "BLOCKED\n")
            else:
                f.write("Test Case Result = " + "FAIL\n")

    def test_empty_user(self):  # Test Case: A user who leaves the username field blank will see an error message.
        try:
            # Pre-Conditions
            self.preconditions()
            driver = self.driver
            f.write("test_empty_user: " + str(timestamp) + "\n")  # Writes a header on the file for the first case

            # Test Step 1:
            step = 1
            driver.find_element(By.NAME, "password").send_keys(
                password)  # Identifies the username field and inputs username
            if driver.find_element(By.NAME, "password").get_attribute(
                    "value") != password:  # Check is made to ensure it was inputted correctly
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")  # Writes Step as FAIL to the Results file
                step = None
                raise Exception()  # With Step as None it passes this to the exception to write the Test Case as Fail
            f.write("   Test Step " + str(step) + " = " + "PASS\n")  # Writes Step as PASS to the Results file

            # Test Step 2: Attempting to Login Results in Empty User Error
            step += 1
            driver.find_element_by_xpath("//button[@type='submit']").click()
            Wait(driver, 10).until(EC.visibility_of_element_located
                                   ((By.XPATH, "//*[contains(text(), '* Require User Name')]")))
            if driver.find_element_by_xpath(
                    "//*[@id='contentarea']/div/router-view/div/div/div[1]/div/form/div[1]") \
                    .get_attribute("innerHTML") != "* Require User Name":
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")
                step = None
                raise Exception()
            f.write("   Test Step " + str(step) + " = " + "PASS\n")
            f.write("Test Case Result = " + "PASS\n")
        except:
            if step is not None:
                f.write("   Test Step " + str(step) + " = " + "BLOCKED\n")
                f.write("Test Case Result = " + "BLOCKED\n")
            else:
                f.write("Test Case Result = " + "FAIL\n")

    def test_empty_user_pass(self):  # Test Case: A user who leaves both fields blank will see an error message.
        try:
            # Pre-Conditions
            self.preconditions()
            driver = self.driver
            f.write("test_empty_user_pass: " + str(timestamp) + "\n")  # writes a header on the file for the first case

            # Test Step 1: Attempting to Login Results in Empty User and Password Error
            step = 1
            driver.find_element_by_xpath("//button[@type='submit']").click()
            Wait(driver, 10).until(EC.visibility_of_element_located
                                   ((By.XPATH, "//*[contains(text(), '* Require User Name')]")))
            Wait(driver, 10).until(EC.visibility_of_element_located
                                   ((By.XPATH, "//*[contains(text(), '* Require Password')]")))
            if driver.find_element_by_xpath(
                    "//*[@id='contentarea']/div/router-view/div/div/div[1]/div/form/div[2]") \
                    .get_attribute("innerHTML") != "* Require User Name" and driver.find_element_by_xpath(
                    "//*[@id='contentarea']/div/router-view/div/div/div[1]/div/form/div[1]") \
                    .get_attribute("innerHTML") != "* Require User Name":
                f.write("   Test Step " + str(step) + " = " + "FAIL\n")
                step = None
                raise Exception()
            f.write("   Test Step " + str(step) + " = " + "PASS\n")
            f.write("Test Case Result = " + "PASS\n")

        except:
            if step is not None:
                f.write("   Test Step " + str(step) + " = " + "BLOCKED\n")
                f.write("Test Case Result = " + "BLOCKED\n")
            else:
                f.write("Test Case Result = " + "FAIL\n")