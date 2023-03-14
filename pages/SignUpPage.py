from pages.base_page import BasePage
from locators.signup_locators import SignUpLocators
import time

class SignUpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_to_load(self):
        self.wait_for_element(SignUpLocators.signup_header, 'signup_header')

    def go_to_sign_up(self):
        self.click_element_css(SignUpLocators.signup_anchor, 'signup_anchor')
        self.wait_for_page_to_load()

    def click_contractor_type_and_next(self):
        self.click_element_css(SignUpLocators.contractor_tab, 'contractor_tab')
        self.click_element_css(SignUpLocators.sign_up_next_button, 'sign_up_next_button')
        self.wait_for_page_to_load()

    def fill_sign_up(self,first_name,last_name,email,password):
        self.insert_text_to_element_css(SignUpLocators.sign_up_first_name, first_name, 'first_name')
        self.insert_text_to_element_css(SignUpLocators.sign_up_last_name, last_name, 'last_name')
        self.insert_text_to_element_css(SignUpLocators.sign_up_email, email, 'email')
        self.insert_text_to_element_css(SignUpLocators.sign_up_password, password, 'password')
        self.choose_first_element_of_hear_of_us()



    def choose_first_element_of_hear_of_us(self):
        self.click_element_css(SignUpLocators.sign_up_how_hear_button, 'hear_us_expand_button')
        items = self.get_multiple_elements(SignUpLocators.sign_up_how_hear_items, 'hear_us_items')
        items[0].click()

    def make_sure_submit_button_enabled(self):
        flag = self.get_element_css(SignUpLocators.sign_up_submit_button, 'sign_up_submit_button').is_enabled()
        return flag


