import hashlib

email='saimun@gmail.com'
pasw='BiggestHero'

pass_encode=pasw.encode()
pwd_hash=hashlib.md5(pass_encode).hexdigest()

encript=hashlib.md5(pasw.encode()).hexdigest()
print(pwd_hash)
print(encript)
