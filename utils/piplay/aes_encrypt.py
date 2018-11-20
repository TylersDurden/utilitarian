import hashlib, os, sys
from Crypto.Cipher import AES
from Crypto import Random


def swap(fname,destroy):
    data = []
    for line in open(fname,'rb').readlines():
        data.append(line.replace('\n',''))
    if destroy:
        os.system('rm '+fname)
    return data


def aes_encrypt(password, message, iv):
    key = hashlib.sha256(password).hexdigest()[0:16]
    ciph = AES.new(key, AES.MODE_CFB, iv)
    return ciph.encrypt(bytes(message)), iv


def data_sealer(key, fname,fout):
    content = ''
    for line in swap(fname,False):
        content += line
    iv = Random.new().read(AES.block_size)
    open(fout, 'w').write(aes_encrypt(key, content, iv))


def main():
    psswd = sys.argv[1]
    fname = os.system('$PWD/'+sys.argv[2])
    data_sealer(psswd, fname, 'out.txt')


if __name__ == '__main__':
    main()

