import pytest

from pageobj.form import Form
from testsdata.DATAS import Data
from utilities.Bassclass import Bass


class TestRegister(Bass):

    def test_process(self, textdata):
        log = self.getLogger()
        fill = Form(self.driver)
        log.info("Frist_name: " + textdata["fname"])
        fill.frist_fname().send_keys(textdata["fname"])
        log.info("Last_name: " + textdata["lname"])
        fill.last_lname().send_keys(textdata["lname"])
        log.info("Address: " + textdata["address"])
        fill.address_add().send_keys(textdata["address"])
        log.info("Email: " + textdata["email"])
        fill.email().send_keys(textdata["email"])
        log.info("Phone Number: " + textdata["pnum"])
        fill.phone_number().send_keys(textdata["pnum"])
        gender = fill.radio_button()

        for i in gender:
            if i.get_attribute("value") == "Male":
                i.click()

        hobbies = fill.hob_hobby()

        for hob in hobbies:
            if hob.get_attribute("value") == "Movies":
                hob.click()

        fill.getlang().click()
        language = fill.getling()
        for lang in language:
            if lang.text == "English":
                lang.click()

        log.info("Skill: " + textdata["skill"])
        self.selecttag(fill.getskill(), textdata["skill"])
        log.info("country: " + textdata["country"])
        self.selecttag(fill.getcountry(), textdata["country"])
        fill.getbox().click()
        fill.getconname().send_keys("Ne")
        con = fill.getscon()
        for coun in con:
            if coun.text == "New Zealand":
                coun.click()

        log.info("Year: " + textdata["year"])
        self.selecttag(fill.getyear(), textdata["year"])
        log.info("Month: " + textdata["month"])
        self.selecttag(fill.getmonth(), textdata["month"])
        log.info("Day: " + textdata["day"])
        self.selecttag(fill.getday(), textdata["day"])
        log.info("Password: " + textdata["password"])
        fill.getpassword().send_keys(textdata["password"])
        log.info("Confirm Password: " + textdata["cpassword"])
        fill.getconpassword().send_keys(textdata["cpassword"])
        fill.subm().click()
        self.driver.refresh()

@pytest.fixture(params=Data.pg_data)
def textdata(request):
    return request.param
