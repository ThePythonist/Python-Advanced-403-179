import hashlib

hash_object = hashlib.md5(b'a')
print(hash_object.hexdigest())
