from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from .base.base_element import BaseElement
from .base.base_page import BasePage
from .base.locator import Locator
import time
import random


class FacebookPage(BasePage):
    url = 'https://www.facebook.com'

    def login(self, email, password, codes):
        self.driver.get(self.url)
        user = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="email"]'))
        )
        passw = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="pass"]'))
        )

        login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@name='login']"))
        )
        user.send_keys(email)
        passw.send_keys(password)
        login_button.click()

        entered_text = 'Se você salvar este navegador, não precisará inserir um código quando se conectar a partir deste navegador novamente.'
        text = "Alguém tentou recentemente entrar na sua conta a partir de um navegador móvel ou computador desconhecido. Como você configurou a autenticação de dois fatores, sua conta foi temporariamente bloqueada. Conclua as etapas a seguir para obter novamente acesso à sua conta."
        for code in codes:
            aprrovals_code = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='approvals_code']"))
            )
            aprrovals_code.send_keys(code)
            self.driver.find_element_by_xpath("//button[@value='Continuar']").click()
            try:
                if self.driver.find_element_by_xpath("//*[contains(text(),'" + entered_text + "')]"):
                    self.driver.find_element_by_xpath("//button[@id='checkpointSubmitButton']").click()
                    try:
                        text = WebDriverWait(self.driver, 2).until(
                            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + text + "')]"))
                        )
                        if text:
                            self.driver.find_element_by_xpath("//button[@id='checkpointSubmitButton']").click()
                            it_was_me = WebDriverWait(self.driver, 2).until(
                                EC.presence_of_element_located((By.XPATH, "//button[@value='Fui eu']"))
                            )
                            it_was_me.click()
                            submit_button = WebDriverWait(self.driver, 2).until(
                                EC.presence_of_element_located((By.XPATH, "//button[@id='checkpointSubmitButton']"))
                            )
                            submit_button.click()
                    except:
                        pass
                    break
            except:
                pass

    def comment(self):
        self.driver.get("https://www.facebook.com/108943681463132/posts/119073403783493")
        comment = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[@class='hcukyx3x oygrvhab cxmmr5t8 kvgmc6g5']/span"))
        )
        comment.send_keys('Muito bom o produto!')
        comment.send_keys(Keys.RETURN)
        return "SUCCESS"
