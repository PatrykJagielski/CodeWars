import re

def validate_pin(pin):
#     return True if re.search(r'(^\d\d\d\d$)|(^\d\d\d\d\d\d$)', pin) else False
    if len(pin) == 4:
        match = re.search(r'^\d\d\d\d$', pin)
        return True if match else False
    elif len(pin) == 6:
        match = re.search(r'^\d\d\d\d\d\d$', pin)
        return True if match else False
    return False
