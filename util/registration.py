from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Registrtion():

    browser_driver = None

    @staticmethod
    def browser():
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument('--headless') 
        g = Service()
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://koshelek.ru/authorization/signup'
        driver.get(base_url)
        Registrtion.browser_driver = driver

    @staticmethod
    def chek(dict_reg):
        if not Registrtion.browser_driver:
            Registrtion.browser()
        driver = Registrtion.browser_driver
        driver.refresh()
        wait = WebDriverWait(driver, 10)
        shadow_host = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".remoteComponent")))

        shadow_root = shadow_host.shadow_root

        # Поля ввода данных
        element_form_input = shadow_root.find_elements(
            By.CSS_SELECTOR, "input")
        element_form_input[0].send_keys(dict_reg['user_name'])
        element_form_input[1].send_keys(dict_reg['email'])
        element_form_input[2].send_keys(dict_reg['pass'])
        element_form_input[3].send_keys(dict_reg['ref'])

        # Согласие с условием
        if dict_reg['acceptance']:
            element_form_input[4].click()

        try:
            form_submit_button = shadow_root.find_element(
                By.CSS_SELECTOR, 'div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div.k-btn-long-button > button')
            form_submit_button.click()
        except:
            print('Кнопка не активна')
        info_accept = shadow_root.find_element(
            By.CSS_SELECTOR, "div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div.k-checkbox-auth > div > div.v-input__control > div > div > span > svg")
        info_accept_html = driver.execute_script(
            "return arguments[0].outerHTML;", info_accept)
        info_name_user = shadow_root.find_element(
            By.CSS_SELECTOR, "div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(1) > div > div > div.v-text-field__details > div > div > div > div > div > span").text
        info_email = shadow_root.find_element(
            By.CSS_SELECTOR, "div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(2) > div > div > div.v-text-field__details > div > div > div > div > div > span").text
        info_pass = shadow_root.find_element(
            By.CSS_SELECTOR, "div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(3) > div > div > div > div > div.v-text-field__details > div > div > div > div > div > span").text
        info_ref = shadow_root.find_element(
            By.CSS_SELECTOR, "div.remoteApplication > div > div > div > div.css-grid.k-text-default > div:nth-child(2) > form > div > div:nth-child(4) > div > div > div.v-text-field__details > div > div > div > div > div > span").text
        response = {
            'user_name': info_name_user,
            'email': info_email,
            'pass': info_pass,
            'ref': info_ref,
            'acceptance': info_accept_html
        }
        return response

    @staticmethod
    def browse_close():
        Registrtion.browser_driver.close()
