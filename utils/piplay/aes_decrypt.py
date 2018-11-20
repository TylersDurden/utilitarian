import hashlib, os, sys
from Crypto.Cipher import AES


def swap(fname, destroy):
    data = ''
    for line in open(fname, 'r').readlines():
        data += line
    if destroy:
        os.system('rm '+fname)
    return data


def aes_decrypt(ctext, password, iv):
    key = hashlib.sha256(password).hexdigest()[0:16]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.decrypt(bytes(ctext))


def main():
    psswd = sys.argv[1]
    fname = sys.argv[2]
    data = swap(fname, True)
    iv = data.pop(0)
    decrypted = aes_decrypt(data, psswd, iv)
    print decrypted


if __name__ == '__main__':
    main()