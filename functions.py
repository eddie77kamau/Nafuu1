import re
def checkpassword(password):
    if len(password)< 6:
        return "Your password is too short"
    elif re.search(r"[A-Z]", password):
        return "Atleast 1 uppercase letter"
    elif re.search(r[a-z], password):
        return "Atleast one lowercase"
    elif re.search(r"[0-9]", password):
        return "Atleast one digit"
    elif re.search(r"[@#$%^&*]", password):
        return "Atleast one special character"
    else:
        True