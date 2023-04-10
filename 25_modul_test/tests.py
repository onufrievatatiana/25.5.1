import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:/Users/Acer/Desktop/Tanja/25_modul_test/chromedriver_win32/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   pytest.driver.implicitly_wait(10)
   pytest.driver.find_element(By.ID,'email').send_keys('student1000@mail.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID,'pass').send_keys('cxz1')
   # Нажимаем на кнопку входа в аккаунт
   WebDriverWait(pytest.driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
   pytest.driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.CSS_SELECTOR, 'h1').text == "PetFriends"

   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

   try:
      for i in range(len(names)):
         assert images[i].get_attribute('src') != ''
         assert names[i].text != ''
         assert descriptions[i].text != ''
         assert ', ' in descriptions[i]
         parts = descriptions[i].text.split(", ")
         assert len(parts[0]) > 0
         assert len(parts[1]) > 0
   except AssertionError:
      print('Нет фото/ имени/возраста у одной из карточек питомца')

