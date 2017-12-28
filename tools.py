

def encode(s):
    ret = ""
    for i in s:
        ret += str(hex(ord(i)))[2:]
    return ret

def decode(s, letter_only = False):
    now = 0
    xor_plain = ""
    while now < len(s):
        now_str = s[now:now + 2]
        now_char = chr(int(now_str, 16))

        if letter_only:
            if "a" <= now_char <= "z" or "A" <= now_char <= "Z":
                xor_plain += now_char
            else:
                xor_plain += "?"
        else:
            if " " <= now_char <= "~":
                xor_plain += now_char
            else:
                xor_plain += "?"

        now += 2

    return xor_plain

def hex_xor(s1, s2, cutoff = False):
  ret = ""
  now = 0
  while now < min(len(s1), len(s2)):
    num1 = int(s1[now], 16)
    num2 = int(s2[now], 16)
    num = num1 ^ num2
    ret += str(hex(num))[2:]
    now += 1

  if cutoff:
      return ret

  if now < len(s1):
    ret += s1[now:]
  if now < len(s2):
    ret += s2[now:]

  return ret

def str_xor(s1, s2):
    s1_encode = encode(s1)
    s2_encode = encode(s2)
    ret = hex_xor(s1, s2)
    return ret

