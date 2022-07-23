print("STRONG PASSWORD CHECKER\n")

print("*Disclamair : Password must be contains Uppercase, Lowercase, Special \n Symbols, Digits and Greater than 8 Characters \n")
password = input("Enter Your password : ")


upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
special = "(){}[]\|:;,.<>?/!@#%^&*-+=_"
digits = "0123456789"

length=len(password)

all = upper_case + lower_case + special + digits

if length <= 8 or password == all:
	print("password is not Strong & not Contains all things ! ")
	print("Try Again !")

else:
	print("\nPassword is Strong " +password)
