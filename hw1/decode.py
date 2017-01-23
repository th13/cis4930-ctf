#-------------------------------------------------------------------------------
# Homework 1, Problem 1
# Trevor Helms
# FSUID: th13
#-------------------------------------------------------------------------------

### Part 1
# Uses urllib to parse a URL encoded string.

import urllib

flag1 = urllib.unquote("%66%6c%61%67%7b%68%31%64%31%6e%67%5f%31%6e%5f%70%6c%34%31%6e%5f%73%31%74%33%7d")
print flag1


### Part 2
# Runs a base64 decode loop until we match the first 5 characters to "flag{"
# (the sign that we've found the flag).

flag2 = """Vm0xd1NtUXlWa1pPVldoVFlUSlNjRlJVVGtOamJGWnhVMjA1VlUxV2NIbFdiVEZIWVZaYWRW
RnNhRmRXTTFKUVZrZDRXbVF3TlZsalJsWk9WakZLTmxaclVrZFVNVXB5VFZaV1dHSkhhRlJW
YkZwM1ZGWlplVTFVVW1wTmF6VllWbGMxVjFaWFJqWldiRkpoVmpOb2FGUldXbHBrTWtaSldr
WlNUbGRGU2paV2FrbzBZekZhV0ZKdVVtcGxiWE01"""

while (flag2[:5] != "flag{"):
    flag2 = flag2.decode("base64")

print flag2
