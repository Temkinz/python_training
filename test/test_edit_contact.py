# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(first_name="E_Igor", middle_name="E_Igorevich", last_name="E_Ivanov",
                                           nickname="E_IvanIgor", title="E_Title", company="E_CompanyA",
                                           address="E_Russia, Moscow", home="E_Moscow", mobile="08926222222222",
                                           work="E_CompanyA", fax="E_None", email="E_someemail@qa.com",
                                           home_page="E_None", bmonth="May", byear="1999", bday="2",
                                           aday="2", amonth="March", ayear="1988", address2="E_Russia, Moscow",
                                           phone2="+0780000000000000", notes="E_some notes"))
