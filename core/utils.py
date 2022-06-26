from random import choices


def generate_shool_id(id_length: int) -> str:
    letter = "1234567890"
    counter = 1
    id = ""
    while counter <= id_length:
        id += choices(letter)
        counter += 1
    return id