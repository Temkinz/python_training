# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    app.open_main_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Igor", last_name="Ivanov",
                      nickname="IvanIgor", title="Title", company="CompanyA",
                      address="Russia, Moscow", home="Moscow", mobile="8926222222222",
                      work="CompanyA", fax="None", email="someemail@qa.com",
                      home_page="None", bmonth="August", byear="1988", bday="1",
                      aday="1", amonth="February", ayear="1999", address2="Russia, Moscow",
                      phone2="+780000000000000", notes="some notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)
