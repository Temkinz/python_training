# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.quit)
    return fixture


def test_create_contact(app):
    app.login(username="admin", password="secret")
    app.complete_contacts_form(Contact(first_name="Igor", middle_name="Igorevich", last_name="Ivanov",
                                       nickname="IvanIgor", title="Title", company="CompanyA",
                                       address="Russia, Moscow", home="Moscow", mobile="8926222222222",
                                       work="CompanyA", fax="None", email="someemail@qa.com",
                                       home_page="None", bmonth="August", byear="1988", bday="1",
                                       aday="1", amonth="February", ayear="1999", address2="Russia, Moscow",
                                       phone2="+780000000000000", notes="some notes"))
    app.go_to_home_page()
