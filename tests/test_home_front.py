import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from django.urls import reverse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='module')
def browser():
    # Configura el servicio de geckodriver
    service = Service(executable_path=GeckoDriverManager().install())
    options = Options()
    options.add_argument('--headless')  # Ejecuta en modo headless si no quieres abrir una ventana del navegador
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

@pytest.mark.django_db
def test_home_page_paragraph_and_image(browser, live_server):
    # URL del servidor en vivo de Django
    url = live_server.url + reverse('home')
    browser.get(url)

    # Espera a que la página cargue completamente
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.top-image img'))
    )

    # Verifica que al menos un párrafo esté presente
    paragraphs = browser.find_elements(By.CSS_SELECTOR, '.top-image .content')
    assert len(paragraphs) > 0, "No paragraphs found on the page"

    # Verifica que la imagen se carga
    image = browser.find_element(By.CSS_SELECTOR, '.top-image img')
    assert image.is_displayed(), "Image is not displayed"

    # Verifica que la URL de la imagen no esté vacía
    image_url = image.get_attribute('src')
    assert image_url.startswith('http'), "Image URL is not valid"
