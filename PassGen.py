import itertools
import string
import hashlib
import time

chars = string.ascii_letters + string.digits + "-" + "_"


def gen():
    start = time.time()
    for pass_len in range(6, 10):
        for pwd in itertools.product(chars, repeat=pass_len):
            pwd = ''.join(pwd)
            hashpwd = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
            if hashpwd == (passHash1[1] or passHash2[1] or passHash3[1] or
                           passHash4[1] or passHash5[1]):
                for e in passHash:
                    for j, k in passHash(e):
                        if hashpwd == passHash(e(k)):
                            user = passHash(e(j))
                end = time.time()
                print(pwd)
                with open("cracked.txt", "a", encoding='utf-8') as cracked:
                    cracked.write("Username: " + user + " Password: " + val + " Time: " + (end-start) + "\n")


passHash1 = ('diego38-zpU', '07b8be9ba2686ea94c80836d1d1a4926476a6ed0')
passHash2 = ('mary38-zpU', 'eeeb6b75308a524fcf050c64204dbba1cc6b45f9')
passHash3 = ('sofia38-zpU', 'e1f26599aa0d78e5072c4c6ef52ff41dd9cf9ff3')
passHash4 = ('james38-zpU', '2dec061b79860ffb97efa22a58c632fbe85550ee')
passHash5 = ('santiago38-zpU', '8794b1a8f46dcbb626cfa4d2510d1998e12cd08d')

passHash = (passHash1, passHash2, passHash3, passHash4, passHash5)

gen()
