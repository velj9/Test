import re

_EMAIL_RE = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def is_valid_email(email_str):
    """Return True if email_str is a well-formed email address, else False.

    Null-safe: None or empty input returns False. Surrounding whitespace is trimmed.
    """
    if not email_str:
        return False
    cleaned = email_str.strip()
    if not cleaned:
        return False
    return bool(_EMAIL_RE.fullmatch(cleaned))
