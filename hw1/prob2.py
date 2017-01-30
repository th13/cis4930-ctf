#-------------------------------------------------------------------------------
# Homework 1, Problem 2
# Trevor Helms
# FSUID: th13
#-------------------------------------------------------------------------------

# Beat race condition on website by parsing the webpage, evaluating the numeric
# expression, and passing it to the server (returning us the flag).
# FIXED: Request needed the PHP Session ID passed as a param.
# TODO: Seems like 50% of the time, the evaluated expression gives the wrong result.
# Not a huge problem because it works after a few runs and retrieves the flag,
# but it's weird.
# Also, why I didn't use BeautifulSoup or something to do the parsing I will never
# understand.

import requests
import math

pg = requests.get("http://ctf.hackucf.org:4000/calc/calc.php")
expr = pg.text[253:]

cookie = pg.headers["Set-Cookie"]

i = 1
j = 3
r = expr[i:j]

while (r != "</"):
    i += 1
    j += 1
    r = expr[i:j]

expr = expr[0:i]
expr = expr.replace("<br/>", "")

headers = { "Cookie": cookie  }
res = requests.post("http://ctf.hackucf.org:4000/calc/calc.php", data={ "answer": math.floor(eval(expr)) }, headers=headers)

print res.text

### Found flag:
### flag{you_should_have_solved_this_in_ruby}
