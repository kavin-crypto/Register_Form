from selenium.webdriver.common.by import By


class Form:
    fname = (By.XPATH,"//*[@ng-model='FirstName']")
    lname = (By.XPATH,"//*[@ng-model='LastName']")
    add = (By.XPATH,"//*[@ng-model='Adress']")
    mail = (By.XPATH,"//*[@ng-model='EmailAdress']")
    number = (By.XPATH,"//*[@ng-model='Phone']")
    button = (By.XPATH,"//*[@type='radio']")
    hobby = (By.XPATH,"//*[@type='checkbox']")
    lang = (By.XPATH,"//*[@id='msdd']")
    ling = (By.XPATH,"//*[contains(@class,'ui-widget-content')]/li/a")
    skill = (By.XPATH,"//*[@id='Skills']")
    country = (By.XPATH,"//*[@ng-model='country']")
    scon = (By.XPATH,"//*[contains(@class,'select2-results__option')]")
    box = (By.XPATH,"//*[@role='combobox']")
    conname = (By.XPATH,'//*[@type="search"]')
    yyyy = (By.XPATH,'//*[@id="yearbox"]')
    mm = (By.XPATH,'//*[@ng-model="monthbox"]')
    dd = (By.XPATH,'//*[@ng-model="daybox"]')
    password = (By.XPATH,'//*[@ng-model="Password"]')
    conpass = (By.XPATH,'//*[@ng-model="CPassword"]')
    submit = (By.XPATH,'//*[@id="submitbtn"]')


    def __init__(self,driver):
        self.driver = driver

    def frist_fname(self):
        return self.driver.find_element(*Form.fname)

    def last_lname(self):
        return self.driver.find_element(*Form.lname)

    def address_add(self):
        return self.driver.find_element(*Form.add)

    def email(self):
        return self.driver.find_element(*Form.mail)

    def phone_number(self):
        return self.driver.find_element(*Form.number)

    def radio_button(self):
        return self.driver.find_elements(*Form.button)

    def hob_hobby(self):
        return self.driver.find_elements(*Form.hobby)

    def getlang(self):
        return self.driver.find_element(*Form.lang)

    def getling(self):
        return self.driver.find_elements(*Form.ling)

    def getskill(self):
        return self.driver.find_element(*Form.skill)

    def getcountry(self):
        return self.driver.find_element(*Form.country)

    def getscon(self):
        return self.driver.find_elements(*Form.scon)

    def getbox(self):
        return self.driver.find_element(*Form.box)

    def getconname(self):
        return self.driver.find_element(*Form.conname)

    def getyear(self):
        return self.driver.find_element(*Form.yyyy)

    def getmonth(self):
        return self.driver.find_element(*Form.mm)

    def getday(self):
        return self.driver.find_element(*Form.dd)

    def getpassword(self):
        return self.driver.find_element(*Form.password)

    def getconpassword(self):
        return self.driver.find_element(*Form.conpass)

    def subm(self):
        return self.driver.find_element(*Form.submit)