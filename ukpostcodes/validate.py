import re


VALID_REGEX = r"^([A-Za-z][A-Ha-hK-Yk-y]?[0-9][A-Za-z0-9]? [0-9][A-Za-z]{2}|[Gg][Ii][Rr] 0[Aa]{2})$"
VALID_REGEX_WITHOUT_SPACE = r"^([A-Za-z][A-Ha-hK-Yk-y]?[0-9][A-Za-z0-9]? ?[0-9][A-Za-z]{2}|[Gg][Ii][Rr] ?0[Aa]{2})$"


def validate_postcode(postcode, without_space=False):

    if without_space:
        regex = VALID_REGEX_WITHOUT_SPACE
    else:
        regex = VALID_REGEX

    match = re.match(regex, postcode)

    if match:
        return True
    else:
        return False
