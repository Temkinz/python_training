import random
import string
from model.contact import Contact
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits(maxlen):
    digits = string.digits
    return "".join([random.choice(digits) for i in range(random.randrange(maxlen))])


def random_date():
    return str(random.randrange(1, 12, 1))


def random_year():
    return str(random.randrange(1900, 2020, 1))


def random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    email_name = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return email_name + ".gmail.com"


def random_month():
    months = ["September", "October", "November", "May", "June"]
    month = random.choice(months)
    return month


testdata = [
    Contact(first_name=random_string("FN", 10), middle_name=random_string("MN", 5), last_name=random_string("LN", 15),
            nickname=random_string("N", 10), title=random_string("T", 10), company=random_string("C", 10),
            address=random_string("C", 20), home_phone=random_digits(11), mobile_phone=random_digits(11),
            work_phone=random_digits(13), fax=random_digits(9), email=random_email(10),
            home_page=random_string("HP", 10), address2=random_string("C", 25),
            secondary_phone=random_digits(12), notes=random_string("C", 25), bday=random_date(),
            bmonth=random_month(), byear=random_year(), aday=random_date(), amonth=random_month(),
            ayear=random_year())
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
