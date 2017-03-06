# magic=0xAD1312
key = bytearray([0xAD, 0x13, 0x12])

newfile = open("xord", "wb")
arr = []

with open("thelady.xml", "rb") as f:
    i = 0
    fb = bytearray(f.read())

    for byte in fb:
        arr.append(byte ^ key[i])
        i += 1
        if i > 2:
            i = 0

newfile.write(bytearray(arr))
newfile.close()

fi = open("xord", "r")
d = open("decoded", "w")
decoded = fi.read().decode("base64")

d.write(decoded)
