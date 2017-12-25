text1 = "attack at dawn"
text1_ord = "".join(hex(ord(c))[2:] for c in text1)
text1_ord = int(text1_ord, 16)

cipher = 0x09e1c5f70a65ac519458e7e53f36
key = text1_ord ^ cipher

text2 = "attack at dusk"
text2_ord = "".join(hex(ord(c))[2:] for c in text2)
text2_ord = int(text2_ord, 16)

cipher = key ^ text2_ord

print hex(cipher)