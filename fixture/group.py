class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        # open group's page
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill the form
        self.fill_form(group)
        # click submit button
        wd.find_element_by_name("submit").click()
        # open group's page
        self.return_to_groups_page()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        # choose the first group
        wd.find_element_by_name("selected[]").click()
        # click delete button
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        # choose the first group
        wd.find_element_by_name("selected[]").click()
        # click edit button
        wd.find_element_by_name("edit").click()
        # fill the form
        self.fill_form(group)
        # click update button
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def fill_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
