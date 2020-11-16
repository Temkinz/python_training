# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Igor", middle_name="Igorevich", last_name="Ivanov",
                               nickname="IvanIgor", title="Title", company="CompanyA",
                               address="Russia, Moscow", home="Moscow", mobile="8926222222222",
                               work="CompanyA", fax="None", email="someemail@qa.com",
                               home_page="None", bmonth="August", byear="1988", bday="1",
                               aday="1", amonth="February", ayear="1999", address2="Russia, Moscow",
                               phone2="+780000000000000", notes="some notes"))
    app.open_main_page()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="E_Igor", middle_name="E_Igorevich", last_name="E_Ivanov",
                                           nickname="E_IvanIgor", title="E_Title", company="E_CompanyA",
                                           address="E_Russia, Moscow", home="E_Moscow", mobile="08926222222222",
                                           work="E_CompanyA", fax="E_None", email="E_someemail@qa.com",
                                           home_page="E_None", bmonth="May", byear="1999", bday="2",
                                           aday="2", amonth="March", ayear="1988", address2="E_Russia, Moscow",
                                           phone2="+0780000000000000", notes="E_some notes")
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)
