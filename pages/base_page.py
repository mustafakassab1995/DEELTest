from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    facebook_logo_file_name = 'facebook_logo.png'

    def open_home_page(self, config):
        self.driver.get(config["tested_page"])

    def wait_for_element(self, locator, element_name):
        print("waiting for " + element_name + " to appear")
        try:
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, locator)
            self.change_color_before_react(locator)
        except:
            time.sleep(5)
            self.driver.find_element(By.CSS_SELECTOR, locator)
            self.change_color_before_react(locator)



    def scroll_to_element(self, locator, element_name):
        print("scrolling to element " + element_name + " ")
        element = self.driver.find_element(By.CSS_SELECTOR, locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def get_facebook_profile_image(self, locator):
        self.wait_for_element(locator, 'facebook_image')
        with open(self.facebook_logo_file_name, 'wb') as file:
            file.write(self.driver.find_element(By.CSS_SELECTOR, locator).screenshot_as_png)

    def make_sure_two_images_the_same(self, first_image, second_image):
        from PIL import Image
        import imagehash
        hash0 = imagehash.average_hash(Image.open(first_image))
        hash1 = imagehash.average_hash(Image.open(second_image))
        cutoff = 5  # maximum bits that could be different between the hashes.

        if hash0 - hash1 < cutoff:
            return True
        else:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def change_color_before_react(self, csslocator):
        self.driver.execute_script(f"document.querySelector(\'{csslocator}\').style.backgroundColor = '#2fb72f'")

    def script_execute(self, script, element_name):
        print("executing script for" + element_name)
        self.driver.execute_script(script)
        print("executing script done for" + element_name)

    def switch_tab_focus(self):
        # get current window handle
        current_window_handle = self.driver.current_window_handle

        # get first child window
        first_child_window = self.driver.window_handles

        for window in first_child_window:
            # switch focus to child window
            if window != current_window_handle:
                self.driver.switch_to.window(window)
                break

    def scroll_to_last(self):
        self.driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight)")

    def click_element_css(self, locator, element_name):
        try:
            self.wait_for_element(locator, element_name)
            print("clicking on " + element_name)
            self.driver.find_element(By.CSS_SELECTOR, locator).click()
        except:
            self.wait_for_element(locator, element_name)
            print("try again: clicking on " + element_name)
            self.driver.find_element(By.CSS_SELECTOR, locator).click()
        print("clicked on " + element_name)

    def select_from_select(self, locator, text, element_name):
        self.wait_for_element(locator, element_name)
        from selenium.webdriver.support.ui import Select
        print("selecting " + text + " from " + element_name)

        select = Select(self.driver.find_element(By.CSS_SELECTOR, locator))

        # select by visible text
        select.select_by_visible_text(text)
        print("selected " + text + " from " + element_name)

    def insert_text_to_element_css(self, locator, text, element_name):
        try:
            self.wait_for_element(locator, element_name)
            print("inserting " + text + " into " + element_name)

            self.driver.find_element(By.CSS_SELECTOR, locator).click()
            self.driver.find_element(By.CSS_SELECTOR, locator).clear()
            self.driver.find_element(By.CSS_SELECTOR, locator).send_keys(text)
        except:
            self.wait_for_element(locator, element_name)
            print("try again : inserting " + text + " into " + element_name)
            self.driver.find_element(By.CSS_SELECTOR, locator).click()
            self.driver.find_element(By.CSS_SELECTOR, locator).clear()
            self.driver.find_element(By.CSS_SELECTOR, locator).send_keys(text)
        print("inserted " + text + " to " + element_name)

    def get_element_css(self , locator, element_name):
        self.wait_for_element(locator, element_name)
        print("getting  text  from " + element_name)
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_text_element_css(self, locator, element_name):
        text = ''
        try:
            self.wait_for_element(locator, element_name)
            print("getting  text  from " + element_name)
            text = self.driver.find_element(By.CSS_SELECTOR, locator).text
        except:
            self.wait_for_element(locator, element_name)
            print("trying again :getting  text from " + element_name)
            text = self.driver.find_element(By.CSS_SELECTOR, locator).text
        print("returned text :" + text + " from " + element_name)
        return text

    def get_multiple_elements(self, locator, element_name):
        print("getting multiple elements related to :" + element_name)
        return self.driver.find_elements(By.CSS_SELECTOR, locator)

    def upload_file(self, path):
        import pyautogui
        pyautogui.write(path)
        pyautogui.press('enter')

    def refresh_the_page(self):
        time.sleep(3)
        self.driver.refresh()
