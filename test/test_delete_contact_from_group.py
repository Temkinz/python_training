from model.contact import Contact
import random
from model.group import Group


def test_delete_user_from_group(app, orm):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="f_test", last_name="l_test"))
    if app.group.count() == 0:
        app.group.create(Group(name="Test_name", header="Test_header", footer="Test_footer"))
    groups = orm.get_group_list()
    group = random.choice(groups)
    contacts_in_group = orm.get_contacts_in_group(group)
    if len(contacts_in_group) == 0:
        all_users = orm.get_contact_list()
        user = random.choice(all_users)
        app.contact.add_user_to_group(user.contact_id, group.id)
    contacts_in_group = orm.get_contacts_in_group(group)
    deleted_user = random.choice(contacts_in_group)
    app.contact.delete_contact_from_group(deleted_user.contact_id, group.id)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert deleted_user not in contacts_in_group