class Asserts:

    def __init__(self, driver):
        self.driver = driver
        self.alerta_nombre = "//*[@id='auth-customerName-missing-alert']/div/div"
        self.alerta_email = "//*[@id='auth-email-missing-alert']/div/div"
        self.alerta_dato_is = "//*[@id='auth-email-missing-alert']/div/div"
        self.alerta_pass_is = "//*[@id='auth-password-missing-alert']/div/div"
        self.alerta_error_pass = "//*[@id='auth-error-message-box']/div/div/ul/li/span"

    def alertname(self):
        self.driver.find_element_by_xpath(self.alerta_nombre)
    def alrtmail(self):
        self.driver.find_element_by_xpath(self.alerta_email)
    def alertisnombre(self):
        self.driver.find_element_by_xpath(self.alerta_dato_is)
    def alertaispass(self):
        self.driver.find_element_by_xpath(self.alerta_pass_is)
    def alerta_pass(self):
        self.driver.find_element_by_xpath(self.alerta_error_pass)
