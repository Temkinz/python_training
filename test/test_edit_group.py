from model.group import Group
import random

"""
def test_modify_first_group(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="Edited name", header="Edited header", footer="Edited footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
"""


def test_modify_some_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="Logo"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(name="New name", header="New header", footer="New footer")
    new_group.id = group.id
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[old_groups.index(group)] = new_group
    assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.group_id_or_max) == sorted(app.group.get_group_list(),
                                                                       key=Group.group_id_or_max)

"""
def test_modify_first_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
"""
