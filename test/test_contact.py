from random import randrange


def test_contact_on_home_page_db(app, db):
    contact_list_on_home_page = app.contact.get_contact_list()
    for contact_from_home_page in contact_list_on_home_page:
        contact_from_db = db.get_contact_by_id(contact_from_home_page.contact_id)[0]
        assert contact_from_home_page.first_name == contact_from_db.first_name
        assert contact_from_home_page.last_name == contact_from_db.last_name
        assert contact_from_home_page.address == contact_from_db.address
        assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(
            contact_from_db)
        assert contact_from_home_page.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(
            contact_from_db)


def test_contact_on_home_page_edit_page(app):
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(
        contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(
        contact_from_edit_page)
