from model.contact import Contact
from random import randrange


def test_delete_first_contact(app):
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
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)
