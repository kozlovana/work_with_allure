import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


url = 'https://github.com'
search_element = '.header-search-input'
repository = 'kozlovana/work_with_files'
issue_tab = '#issues-tab'
issue_value = '#1'


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'kozlovana')
@allure.feature('Testing github')
@allure.story('Check that Issue with specific number is visible on the page')
@allure.link('https://github.com/kozlovana', name='Dynamic steps')
def test_github_with_dynamic_steps():
    with allure.step("Open the main page"):
        browser.open(url)

    with allure.step("Search for the required repository"):
        s(search_element).click()
        s(search_element).send_keys(repository)
        s(search_element).submit()

    with allure.step("Open link of the required repository"):
        s(by.link_text(repository)).click()

    with allure.step('Open the tab "Issues"'):
        s(issue_tab).click()

    with allure.step("Check for the Issue #1"):
        s(by.partial_text(issue_value)).should(be.visible)
