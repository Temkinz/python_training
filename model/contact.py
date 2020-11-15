from sys import maxsize


class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None,
                 address=None, home=None, mobile=None, work=None, fax=None, email=None, home_page=None,
                 bmonth=None, byear=None, bday=None, aday=None, amonth=None, ayear=None,
                 address2=None, phone2=None, notes=None, contact_id=None, name=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.home_page = home_page
        self.bmonth = bmonth
        self.byear = byear
        self.bday = bday
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.contact_id = contact_id
        self.name = name

    def __repr__(self):
        return "%s:%s:%s" % (self.contact_id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id)\
               and self.first_name == other.first_name and self.last_name == other.last_name

    def contact_id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
