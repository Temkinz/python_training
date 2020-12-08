from model.contact import Contact
import random


def test_delete_first_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Igor", middle_name="Igorevich", last_name="Ivanov",
                                   nickname="IvanIgor", title="Title", company="CompanyA",
                                   address="Russia, Moscow", home_phone="89898000000", mobile_phone="8926222222222",
                                   work_phone="88888888888888", fax="None", email="someemail@qa.com",
                                   home_page="None", bmonth="August", byear="1988", bday="1",
                                   aday="1", amonth="February", ayear="1999", address2="Russia, Moscow",
                                   secondary_phone="+780000000000000", notes="some notes"))
    app.open_main_page()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.contact_id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.contact_id_or_max) == sorted(app.contact.get_contact_list(),
                                                                             key=Contact.contact_id_or_max)
