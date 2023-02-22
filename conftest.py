import pytest
from selene.support.shared import browser


@pytest.fixture()
def set_browser_window_size():
    browser.config.window_width = 1280
    browser.config.window_height = 720


@pytest.fixture()
def open_browser(size_window_browser):
    browser.open('https://google.com')



