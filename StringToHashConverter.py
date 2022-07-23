import hashlib
import time


print("HASH CONVERTER \n")
a = input("Enter Your String : ")

print("Processing......")
time.sleep(3)

c = hashlib.md5(a.encode())
g = c.hexdigest()
print("\nMD5 Value : "+g)

c = hashlib.sha1(a.encode())
g = c.hexdigest()
print("\nSHA1 Value : "+g)

c = hashlib.sha224(a.encode())
g = c.hexdigest()
print("\nSHA224 Value : "+g)