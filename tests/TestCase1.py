import pytest
from pages.SignUpPage import SignUpPage

@pytest.mark.usefixtures("setup", "website_setup")
class TestSignUp:

    def test_signup_button_if_inputs_valid_input(self, config):
        # vars for the test
        first_name = 'first_name'
        last_name = 'last_name'
        email = 'automation@email.com'
        password = 'Z4HJqmJiwCt2x8F_'




        signup_page = SignUpPage(self.driver)
        signup_page.wait_for_page_to_load()

        print("step1 :go_to_sign_up")
        signup_page.go_to_sign_up()

        print("step2 :click_contractor_type_and_next")
        signup_page.click_contractor_type_and_next()

        print("step3 :fill_sign_up")
        signup_page.fill_sign_up(first_name, last_name, email, password)

        print("step4 :make sure button enabled")
        flag = signup_page.make_sure_submit_button_enabled()

        if flag:
            assert True
        else:
            assert False













