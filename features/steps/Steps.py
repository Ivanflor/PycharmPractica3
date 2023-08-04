from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from pom.LoginPage import LogingPage
from pom.RegisterPage import RegisterPage
from pom.RegisterPassworPage import RegisterPasswordPage
from pom.WithoutDataPage import WithoutData

@given('usuario ingrea a la pagina demoguru')
def irDemoGuru(self):
    #intanciar driver
    self.driver = webdriver.Chrome()
    #inicializamos el navegador
    self.driver.get("https://demo.guru99.com/test/newtours")
    self.LoginPage = LogingPage(self.driver)
    self.RegisterPage = RegisterPage(self.driver)
    self.RegisterPassword = RegisterPasswordPage(self.driver)
    self.withoutData = WithoutData(self.driver)


@when("usuario da click en singon")
def clicksingon(self):

    self.LoginPage.clicksingon()

@step("usuario ingresa sus credenciales")
def step_impl(self):
    self.LoginPage.writeName("user1")
    self.LoginPage.writePass("pas321")


@step("click en submit")
def step_impl(self):
    self.LoginPage = LogingPage(self.driver)
    btnsubmit = self.driver.find_element(By.XPATH, "//input[@name='submit']")
    btnsubmit.click()
    self.driver.implicitly_wait(20)

@then('logeo exitoso')
def logeoExitoso(self):
    self.driver.implicitly_wait(20)
    #obtener titulo de la pagina
    tituloPagina = self.driver.title
    #validacion
    assert tituloPagina == "Login: Mercury Tours"

@when('click en register')
def clickregister(self):
    self.withoutData.clickregister()
    self.RegisterPage.clickregister()

@when('usuario ingresa sus datos')
def ingresaDatos(self):

    self.RegisterPasswordPage.writeuserName("ivanTest25")
    self.RegisterPasswordPage.writepassWord("pass321")
    self.RegisterPasswordPage.writeconfirmPass("pass321")

    self.RegisterPasswordPage.writeFirstName("Ivan")
    self.RegisterPasswordPage.writeLastName("test")
    self.RegisterPasswordPage.writePhone("551236978455")
    self.RegisterPasswordPage.writeEmail("test963@gmail.com")
    self.RegisterPasswordPage.writeAdress("circuito int N456")
    self.RegisterPasswordPage.writeCity("CDMX")
    self.RegisterPasswordPage.writeState("Coyoacan")
    self.RegisterPasswordPage.writePostal("046520")


@when('click en enviar')
def clickEnviar(self):

    self.RegisterPassword.clickSubmit()
    self.withoutData.clickSubmit()
    self.RegisterPage.clickSubmit()

@then('registro exitoso')
def registroExitoso(self):
    # obtener titulo de la pagina
    tituloPagina = self.driver.title
    # validacion
    assert tituloPagina == "Register: Mercury Tours"


@when("usuario ingresa dos contraseñas diferentes")
def step_impl(self):
    self.RegisterPage.writeFirstName("Ivan")
    self.RegisterPage.writeLastName("test")
    self.RegisterPage.writePhone("551236978455")
    self.RegisterPage.writeEmail("test963@gmail.com")
    self.RegisterPage.writeAdress("circuito int N456")
    self.RegisterPage.writeCity("CDMX")
    self.RegisterPage.writeState("Coyoacan")
    self.RegisterPage.writePostal("046520")
    self.RegisterPage.writeuserName("ivanTest25")
    self.RegisterPage.writepassWord("pass321")
    self.RegisterPage.writeconfirmPass("pass")


@then("permanece en la pagina de registro")
def step_impl(self):
    txtContac = self.driver.find_element(By.XPATH, "//font[contains(text(),'Contact')]")

    assert txtContac == "Contac"


@step("usuario no ingresa los campos obligatorios")
def step_impl(self):
    self.withoutData.writeFirstName("Ivan")
    self.withoutData.writeLastName("test")
    self.withoutData.writePhone("551236978455")
    self.withoutData.writeEmail("test963@gmail.com")
    self.withoutData.writeAdress("circuito int N456")
    self.withoutData.writeCity("CDMX")
    self.withoutData.writeState("Coyoacan")
    self.withoutData.writePostal("046520")