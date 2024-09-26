import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

def test_navbar():
    # Configura el servicio de geckodriver
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    
    try:
        # Abre la página del proyecto
        driver.get('http://127.0.0.1:8000')  # Cambia la URL si es necesario

        # Abre el menú
        menu_toggle = driver.find_element(By.ID, 'menuToggle')
        menu_toggle.click()

        # Espera a que el menú sea visible
        time.sleep(1)

        # Verifica que el menú esté visible
        menu = driver.find_element(By.ID, 'menu')
        assert menu.is_displayed()

        # Cierra el menú con el botón de cerrar
        close_menu = driver.find_element(By.ID, 'closeMenu')
        close_menu.click()

        # Espera a que el menú se cierre
        time.sleep(1)

        # Verifica que el menú esté cerrado
        assert not menu.is_displayed()

        # Abre el menú nuevamente
        menu_toggle.click()
        time.sleep(1)
        assert menu.is_displayed()

        # Simula clic fuera del menú
        close_menu = driver.find_element(By.TAG_NAME, 'body')

        # Espera a que el menú se cierre
        time.sleep(4)

        # Verifica que el menú esté cerrado
        print(f"Menu visible: {menu.is_displayed()}")
        assert not menu.is_displayed()

    finally:
        # Cierra el navegador después de la prueba
        driver.quit()


if __name__ == "__main__":
    test_navbar()
