from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Igor", middle_name="Igorevich", last_name="Ivanov",
                               nickname="IvanIgor", title="Title", company="CompanyA",
                               address="Russia, Moscow", home="Moscow", mobile="8926222222222",
                               work="CompanyA", fax="None", email="someemail@qa.com",
                               home_page="None", bmonth="August", byear="1988", bday="1",
                               aday="1", amonth="February", ayear="1999", address2="Russia, Moscow",
                               phone2="+780000000000000", notes="some notes"))
    app.contact.delete_first_contact()
