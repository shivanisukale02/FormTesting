import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setUp():
    global movieName,Year,DirectorName,Distributor,Producer,driver
    movieName=input("Enter movie name")
    Year=input("Enter year of release")
    DirectorName=input("Enter DirectorName")
    Distributor=input("Enter Distributor")
    Producer=input("Enter Producer")
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)

def test_form2(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php/")
    time.sleep(1)
    driver.find_element_by_name("mname").send_keys(movieName)
    driver.find_element_by_name("myear").send_keys(Year)
    driver.find_element_by_name("mdirector").send_keys(DirectorName)
    driver.find_element_by_name("mdist").send_keys(Distributor)
    driver.find_element_by_name("mproducer").send_keys(Producer)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[3]").click()
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[7]/td[2]/button").click()
