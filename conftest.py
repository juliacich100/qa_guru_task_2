
import pytest
from selene.support.shared import browser


@pytest.fixture()
def open_google():
    browser.open('https://google.com')
    browser.config.window_height = 800
    browser.config.window_width = 1000