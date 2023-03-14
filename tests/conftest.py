import json
import pytest
from driver.driver_factory import DriverFactory

CONFIG_PATH = "config.json"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]
DEFAULT_WEBSITE = "http://www.google.com/"


@pytest.fixture(scope='session')
def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)


@pytest.fixture(scope="session")
def browser_setup(config):
    if "browser" not in config:
        raise Exception('The config file does not contain "browser"')
    elif config["browser"] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config["browser"]


@pytest.fixture(scope='session')
def wait_time_setup(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def website_setup(config):
    return config['tested_page'] if 'tested_page' in config else DEFAULT_WEBSITE


def accept_cookies(driver):
    accept_coockies_button = '#wt-cli-accept-all-btn'
    driver.execute_script(f"document.querySelector(\'{accept_coockies_button}\').click()")


@pytest.fixture()
def setup(request, config):
    driver = DriverFactory.get_driver(config["browser"], config["headless_mode"])
    driver.implicitly_wait(config["timeout"])
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    if config["browser"] == "firefox":
        driver.maximize_window()
    driver.get(config["tested_page"])

    yield
    # if request.session.testsfailed != before_failed:
        # driver.screenshot('fail.png')
    driver.quit()
