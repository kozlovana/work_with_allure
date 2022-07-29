from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


url = 'https://github.com'
search_element = '.header-search-input'
repository = 'kozlovana/work_with_files'
issue_tab = '#issues-tab'
issue_value = '#1'


def test_github():
    browser.open(url)

    s(search_element).click()
    s(search_element).send_keys("kozlovana/work_with_files")
    s(search_element).submit()

    s(by.link_text(repository)).click()

    s(issue_tab).click()

    s(by.partial_text(issue_value)).should(be.visible)