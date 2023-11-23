import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_button_click(driver):
    driver.get("https://qalan.kz/")
    time.sleep(5)
    button = driver.find_element(By.CSS_SELECTOR, '.button.register-button')
    button.click()
    assert "Qalan" in driver.title

def test_fill_field(driver):
    time.sleep(3)  

    input_name = driver.find_element(By.NAME, "firstname")
    input_name.send_keys("Test")

    input_surname = driver.find_element(By.NAME, "surname")
    input_surname.send_keys("User")

    input_tel=driver.find_element(By.CLASS_NAME, "form-control")
    input_tel.send_keys("7012345678")
    time.sleep(2)

    input_pass=driver.find_element(By.NAME,"password")
    input_pass.send_keys("1234")

    repeat_pass=driver.find_element(By.NAME,"repeatPassword")
    repeat_pass.send_keys("1234")
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(3)

    radio_student = driver.find_element(By.XPATH, '//label[text()="Мен оқушымын"]/input')
    radio_student.click()
    time.sleep(2)

    register = driver.find_element(By.CSS_SELECTOR, '.button.register-button')
    register.click()
    time.sleep(5)

    assert "Qalan" in driver.title

if __name__ == "__main__":
    pytest.main(["-v", "example.py"])
