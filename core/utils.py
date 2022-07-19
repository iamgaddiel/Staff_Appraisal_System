from random import choices
from string import ascii_letters, digits, ascii_uppercase
from django.contrib.auth.hashers import make_password


def generate_shool_id(id_length: int) -> str:
    ID_FORMAT  = "SCH/FCULT/DPT/SD/"
    school_id = ID_FORMAT + "".join(choices(ascii_letters+ascii_uppercase+digits, k=id_length))
    return school_id


def generate_password(password: str) -> str:
    return  make_password(password)

if __name__ == '__main__':
    # id = generate_shool_id(8)
    pswd = generate_password("test.123")
    print(pswd)
