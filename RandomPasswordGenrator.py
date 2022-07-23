import random
import time

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
Symbol = "(){}[]\|:;,.<>?/!@#%^&*-+=_"

all = lower + upper + digits + Symbol
length = 15

print("RANDOM PASSWORD GENRATOR\n")

print("Genrating password")
time.sleep(3)

password = "".join(random.sample(all,length))
print("Random password is : "+password)