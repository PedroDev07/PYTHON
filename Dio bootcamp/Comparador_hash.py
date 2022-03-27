import hashlib



arquivo1 = 'Arq1.txt'
arquivo2 = 'Arq2.txt'

hash_1 = hashlib.new('ripemd160')

hash_1.update(open(arquivo1, 'rb').read())

hash_2 = hashlib.new('ripemd160')
hash_2.update(open(arquivo2, 'rb').read())


if hash_1.digest() == hash_2.digest():
    print("arquivo igual")
else:
    print("arquivo igual")