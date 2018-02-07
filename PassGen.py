import itertools
import string
import hashlib
import time

chars = string.ascii_letters + string.digits + string.punctuation


def gen():
    start = time.time()
    for pass_len in range(4, 10):
        for pwd in itertools.product(chars, repeat=pass_len):
            pwd = ''.join(pwd)
            hashpwd = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
            if hashpwd == passHash:
                print(pwd)
                end = time.time()
                print(end - start)
                return pwd


with open("randPwdFile38.txt", "r", encoding='utf-8') as passFile:
    for line in passFile:
        line = line.strip()
        line = line.split(',')
        passHash = line[1]
        uname = line[0]
        passHash = passHash.replace(' ', '')
        print(passHash)
        val = gen()
        with open("cracked.txt", "a", encoding='utf-8') as cracked:
            cracked.write("Username: " + uname + " Password: " + val + "\n")
