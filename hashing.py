import hmac, hashlib

m = hmac.new(b'password', digestmod=hashlib.blake2s)
m.update(b'message')
print("Your encryption key is:", m.hexdigest())
