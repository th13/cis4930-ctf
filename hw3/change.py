import telnetlib
import math

coins = [ 1000000, 500000, 100000, 50000, 10000, 5000, 2000, 1000, 500, 100, 50, 25, 10, 5, 1 ]

def make_change(amt):
    amt = int(round(amt * 100))

    change = []
    for c in coins:
        curr = amt / c
        amt -= curr * c
        change.append(curr)
    return change

tn = telnetlib.Telnet("104.236.253.250", "31337")

j = 0
while(True):
    if j == 400:
        break
    print "Iter #", j
    res = tn.read_until(":").split("\n")
    amount = float(res[0][1:])
    print res[0]
    prompt = res[1]

    change = make_change(amount)
    for i in range(0, 15):
        tn.write(str(change[i]) + "\n")
    tn.read_until("correct!\n")
    print "Change made: "
    for c in change:
        print c,
    print ""
    j += 1

print tn.read_all()
