from selenium.webdriver.common.by import By


class LogingPage:
    def __init__(self, diver):
        self.driver = diver
        self.btnsingon = (By.XPATH, "//a[@href='login.php']")
        self.txtuserName = (By.NAME, 'userName')
        self.txtpasword = (By.NAME, 'password')




    #definimos acciones de los elementos
    def clicksingon(self):
        self.driver.find_element(*self.btnsingon).click()
    def writeName(self, userName):
        self.driver.find_element(*self.txtuserName).send_keys(userName)
    def writePass(self, password):
        self.driver.find_element(*self.txtpasword).send_keys(password)



