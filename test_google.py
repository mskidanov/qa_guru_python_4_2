from selene.support.shared import browser
from selene import be, have


def test_google_positive(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_negative(open_browser):
    browser.element('[name="q"]').should(be.blank).type('jdjdjdjdjspo2342485t61212').press_enter()
    browser.element('[id="center_col"]').should(have.text('По запросу jdjdjdjdj spo2342485t61212 ничего не найдено.'))