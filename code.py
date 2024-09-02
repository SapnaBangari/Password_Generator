import random

symbols_length=int(input("Enter the length of symbols:"))
digits_length=int(input("Enter the length of digits:"))
letter_length=int(input("Enter the number of letters:"))


letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digits=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','_','+']

for i in range(0, symbols_length):
    print(random.choice (symbols),end="")
for i in range(0,digits_length):
    print(random.choice(digits),end="")
for i in range(0,letter_length):
    print(random.choice(letters),end="")
    