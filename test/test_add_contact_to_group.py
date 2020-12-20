from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, orm):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Igor", middle_name="Igorevich", last_name="Ivanov",
                                   nickname="IvanIgor", title="Title", company="CompanyA",
                                   address="Russia, Moscow", home_phone="89898000000", mobile_phone="8926222222222",
                                   work_phone="88888888888888", fax="None", email="someemail@qa.com",
                                   home_page="None", bmonth="August", byear="1988", bday="1",
                                   aday="1", amonth="February", ayear="1999", address2="Russia, Moscow",
                                   secondary_phone="+780000000000000", notes="some notes"))
    if app.group.count() == 0:
        app.group.create(Group(name="Logo"))
    all_contacts = orm.get_contact_list()
    contact = random.choice(all_contacts)
    groups = orm.get_group_list()
    group_id = random.choice(groups).id
    app.contact.add_contact_to_group(contact.contact_id, group_id)
    new_contacts = orm.get_contacts_in_group(Group(id=group_id))
    assert contact in new_contacts
