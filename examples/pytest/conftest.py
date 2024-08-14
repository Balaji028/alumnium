import pytest
from alumni import Alumni
from selenium.webdriver import Chrome


@pytest.fixture(scope="session", autouse=True)
def driver():
    driver = Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def al(driver):
    al = Alumni(driver)
    yield al
    al.quit()
