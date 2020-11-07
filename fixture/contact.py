from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # open contacts page
        wd.find_element_by_link_text("add new").click()
        # fill the form
        self.fill_form(contact)
        # click submit button
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.go_to_home_page()

    def fill_form(self, contact):
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("homepage", contact.home_page)
        self.choose_option("bday", contact.bday, "//option[@value='1']")
        self.choose_option("bmonth", contact.bmonth, "//option[@value='August']")
        self.change_field_value("byear", contact.byear)
        self.choose_option("aday", contact.aday, "(//option[@value='1'])[2]")
        self.choose_option("amonth", contact.amonth, "(//option[@value='February'])[2]")
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def choose_option(self, field_name, option, locator):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        Select(wd.find_element_by_name(field_name)).select_by_visible_text(option)
        wd.find_element_by_xpath(locator).click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_main_page()
        # choose the first contact
        wd.find_element_by_name("selected[]").click()
        # click delete button
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept alert
        wd.switch_to_alert().accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_main_page()
        # choose the first contact
        wd.find_element_by_name("selected[]").click()
        # click update button
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit the form
        self.fill_form(contact)
        # click submit button
        wd.find_element_by_name("update").click()
        # return to main page
        self.return_to_main_page()

    def return_to_main_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_main_page()
        return len(wd.find_elements_by_name("selected[]"))
