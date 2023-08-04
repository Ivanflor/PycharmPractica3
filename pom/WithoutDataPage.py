from selenium.webdriver.common.by import By


class WithoutData:
    def __init__(self, driver):
        self.driver = driver
        self.btnregister = (By.XPATH, "//a[text()='REGISTER']")
        self.txtFirstName = (By.XPATH, "//input[@name='firstName']")
        self.txtLastName = (By.XPATH, "//input[@name='lastName']")
        self.txtPhone = (By.XPATH, "//input[@name='phone']")
        self.txtEmail = (By.XPATH, "//input[@name='userName']")
        self.txtAdress = (By.XPATH, "//input[@name='address1']")
        self.txtCity = (By.XPATH, "//input[@name='city']")
        self.txtState = (By.XPATH, "//input[@name='state']")
        self.txtPostalCode = (By.XPATH, "//input[@name='postalCode']")
        self.btnSubmit = (By.XPATH, "//input[@name='submit']")
    def clickregister(self):
        self.driver.find_element(*self.btnregister).click()
    def writeFirstName (self, firstName):
        self.driver.find_element(*self.txtFirstName).send_keys(firstName)
    def writeLastName(self, lastName):
        self.driver.find_element(*self.txtLastName).send_keys(lastName)

    def writePhone(self, phone):
        self.driver.find_element(*self.txtPhone).send_keys(phone)

    def writeEmail(self, email):
        self.driver.find_element(*self.txtEmail).send_keys(email)

    def writeAdress(self, adress):
        self.driver.find_element(*self.txtAdress).send_keys(adress)

    def writeCity(self, city):
        self.driver.find_element(*self.txtCity).send_keys(city)

    def writeState(self, state):
        self.driver.find_element(*self.txtState).send_keys(state)

    def writePostal(self, postal):
        self.driver.find_element(*self.txtPostalCode).send_keys(postal)
    def clickSubmit(self):
        self.driver.find_element(*self.btnSubmit).click()
