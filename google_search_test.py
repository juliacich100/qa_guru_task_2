from selene.support.shared import browser
from selene import be, have


def test_positive(open_google):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))


def test_negative(open_google):
    browser.element('[name="q"]').should(be.blank).type('dmnrthjdfopcs').press_enter()
    browser.element('[id="result-stats"]').should(have.text('примерно 0'))