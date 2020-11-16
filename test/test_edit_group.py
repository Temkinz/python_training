from model.group import Group

"""
def test_modify_first_group(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="Edited name", header="Edited header", footer="Edited footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
"""


def test_modify_first_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="New name")
    group.group_id = old_groups[0].group_id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)


"""
def test_modify_first_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
"""
