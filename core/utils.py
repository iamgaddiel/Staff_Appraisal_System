from random import choices
from string import ascii_letters, digits, ascii_uppercase
from django.contrib.auth.hashers import check_password, make_password


def generate_shool_id(id_length: int) -> str:
    ID_FORMAT  = "SCH/FCULT/DPT/SD/"
    school_id = ID_FORMAT + "".join(choices(ascii_letters+ascii_uppercase+digits, k=id_length))
    return school_id


def generate_password(password: str) -> str:
    return  make_password(password)


def generate_underscore_separator(string: str) -> str: return string.replace(" ", "_")


def validate_password(password: str, hash: str) -> bool:
    return check_password(password, hash)


def get_password(password):
    print(password)

if __name__ == '__main__':
    print(validate_password("1q2wd3ef4r", "pbkdf2_sha256$320000$o460ocGPrT3lrH5uhrUwfG$5YrkP6IMwp2LbRnKkspZrxQIKgzPiovee1wgOXKAZU0="))
