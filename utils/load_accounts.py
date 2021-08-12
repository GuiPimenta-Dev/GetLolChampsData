from pages.base.base_page import BasePage

class AccountPage(BasePage):
    def get_accounts(self):
        self.driver.get('https://web.whatsapp.com/')
        files = self.driver.find_elements_by_xpath('//div[@class="tm2tP copyable-area"]//div//button')
        for i in files:
            i.click()


x = AccountPage().get_accounts()