from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Logo"))
    app.group.modify_first_group(Group(name="Edited name", header="Edited header", footer="Edited footer"))


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Logo"))
    app.group.modify_first_group(Group(name="New name"))


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Logo"))
    app.group.modify_first_group(Group(header="New header"))
