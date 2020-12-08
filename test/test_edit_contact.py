# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Igor", middle_name="Igorevich", last_name="Ivanov",
                                   nickname="IvanIgor", title="Title", company="CompanyA",
                                   address="Russia, Moscow", home_phone="9898000000000", mobile_phone="8926222222222",
                                   work_phone="88888888888888", fax="None", email="someemail@qa.com",
                                   home_page="None", bmonth="August", byear="1988", bday="1",
                                   aday="1", amonth="February", ayear="1999", address2="Russia, Moscow",
                                   secondary_phone="+780000000000000", notes="some notes"))
    app.open_main_page()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact = Contact(first_name="E_Igor", middle_name="E_Igorevich", last_name="E_Ivanov",
                          nickname="E_IvanIgor", title="E_Title", company="E_CompanyA",
                          address="E_Russia, Moscow", home_phone="098981111111111", mobile_phone="08926222222222",
                          work_phone="088888888888888", fax="E_None", email="E_someemail@qa.com",
                          home_page="E_None", bmonth="May", byear="1999", bday="12",
                          aday="10", amonth="February", ayear="1988", address2="E_Russia, Moscow",
                          secondary_phone="+0780000000000000", notes="E_some notes")
    index = old_contacts.index(contact)
    app.contact.modify_contact_by_index(index, new_contact)
    new_contact.contact_id = contact.contact_id
    new_contacts = db.get_contact_list()
    old_contacts[old_contacts.index(contact)] = new_contact
    assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.contact_id_or_max) == sorted(app.contact.get_contact_list(),
                                                                             key=Contact.contact_id_or_max)
