from sys import maxsize


class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, home_phone=None, nickname=None, title=None,
                 company=None, address=None, mobile_phone=None, work_phone=None, fax=None, email=None, email2=None,
                 email3=None, home_page=None, bmonth=None, byear=None, bday=None, aday=None, amonth=None, ayear=None,
                 address2=None, secondary_phone=None, notes=None, contact_id=None, name=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None, all_phones_from_db=None,
                 all_emails_from_db=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.home_page = home_page
        self.bmonth = bmonth
        self.byear = byear
        self.bday = bday
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.secondary_phone = secondary_phone
        self.notes = notes
        self.contact_id = contact_id
        self.name = name
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_phones_from_db = all_phones_from_db
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_emails_from_db = all_emails_from_db

    def __repr__(self):
        return "%s:%s:%s%s%s%s%s%s%s:%s:%s:%s:%s:%s:%s:%s:%s:%s;%s:%s:%s:%s:%s:%s" % (
            self.contact_id, self.first_name, self.middle_name, self.last_name, self.home_phone, self.nickname,
            self.title, self.company, self.address, self.mobile_phone, self.work_phone, self.fax, self.email,
            self.email2, self.email3, self.home_page, self.address2, self.secondary_phone, self.bday, self.bmonth,
            self.byear, self.aday, self.amonth, self.ayear)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id) \
               and self.first_name == other.first_name and self.last_name == other.last_name

    def contact_id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
