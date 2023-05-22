import hashlib

def hash_password(password):
    hash_object = hashlib.md5(bytes(str(password), encoding='utf-8'))
    return hash_object.hexdigest()
