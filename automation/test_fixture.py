import pytest
from selenium import webdriver

driver = None


@pytest.fixture()
def setup(request):
    global driver
    print("initiating chrome driver")
    driver = webdriver.Chrome(executable_path="D:/Softwares/drivers/chromedriver.exe")
    driver.get("http://seleniumeasy.com/test")
    driver.maximize_window()

    yield driver
    driver.close()
    driver.quit()
    driver = None


@pytest.mark.usefixtures("setup")
class TestOne(object):

    def test_ajay1(self):

        driver.get("https://www.google.com")

    # def test_ajay2(self):
    #     self.driver.get("https://www.google.com")
    #     print(self.driver.get_title())


@pytest.mark.usefixtures("setup")
class TestTwo(object):

    # def test_ajay1(self):
    #     self.driver.get("https://www.google.com")

    def test_ajay2(self):
        driver.get("https://www.google.com")
        title =driver
