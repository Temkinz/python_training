from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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
        self.contact_cache = None

    def fill_form(self, contact):
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
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
        self.change_field_value("phone2", contact.secondary_phone)
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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_main_page()
        self.select_contact_by_index(index)
        # click delete button
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept alert
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector('div.msgbox')
        self.app.open_main_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_main_page()
        self.select_edit_contact_by_index(index)
        # edit the form
        self.fill_form(contact)
        # click submit button
        wd.find_element_by_name("update").click()
        # return to main page
        self.return_to_main_page()
        wd.current_url.endswith("/addressbook/")
        self.contact_cache = None

    def return_to_main_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_main_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_main_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                contact_id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                first_name = cells[2].text
                last_name = cells[1].text
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, contact_id=contact_id,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.app.open_main_page()
        self.select_edit_contact_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, contact_id=id, home_phone=home_phone,
                       work_phone=work_phone, mobile_phone=mobile_phone, secondary_phone=secondary_phone,
                       address=address, email=email, email2=email2, email3=email3)

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_main_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, secondary_phone=secondary_phone)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                            contact.secondary_phone]))))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.email, contact.email2, contact.email3]))))
