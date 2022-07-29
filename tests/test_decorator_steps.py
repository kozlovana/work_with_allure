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
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'kozlovana')
@allure.feature('Testing github')
@allure.story('Check that Issue with specific number is visible on the page')
@allure.link('https://github.com/kozlovana', name='Decorator steps')
def test_github_with_decorator_steps():
    open_main_page()
    search_for_repository()
    go_to_repository()
    open_issues_tab()
    check_availability_of_issue_with_number()


@allure.step('Open the main page')
def open_main_page():
    browser.open(url)


@allure.step('Search for the ' + repository)
def search_for_repository():
    s(search_element).click()
    s(search_element).send_keys(repository)
    s(search_element).submit()


@allure.step('Open link of the ' + repository)
def go_to_repository():
    s(by.link_text(repository)).click()


@allure.step('Open the tab "Issues"')
def open_issues_tab():
    s(issue_tab).click()


@allure.step('Check for the Issue #' + issue_value)
def check_availability_of_issue_with_number():
    s(by.partial_text(issue_value)).should(be.visible)
