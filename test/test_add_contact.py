# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Igor", middle_name="Igorevich", last_name="Ivanov",
                               nickname="IvanIgor", title="Title", company="CompanyA",
                               address="Russia, Moscow", home="Moscow", mobile="8926222222222",
                               work="CompanyA", fax="None", email="someemail@qa.com",
                               home_page="None", bmonth="August", byear="1988", bday="1",
                               aday="1", amonth="February", ayear="1999", address2="Russia, Moscow",
                               phone2="+780000000000000", notes="some notes"))
    app.go_to_home_page()
    app.session.logout()