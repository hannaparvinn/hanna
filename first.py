#import random
#print a random number btw 0 and 1
#print(random.random())
#print a random number btw 0 and 10
#print(random.uniform(0,10))
#print(random.randint(5,15))


#import random
#a = input("Do you want generate a OTP ? (YES/NO) :").lower()
#if a=='yes':
    #otp=random.randint(100000,999999)
    #print("otp generated :yes",otp)
#else:
    #print("No otp")

#write a program to create a random phone no?
#* phone no must be start with number 6/7/8/9
#* phone no should be in format 9xx-xxx-xxx
#import random
#one=random.randint(6,9)
#two=random.randint(10,99)
#three=random.randint(100,999)
#four=random.randint(1000,9999)
#print(f'Your phone Number = {one}{two}-{three}-{four}')


#mport random
#colors=['Blue','Red','Green','Orange','White','Yellow','Black','Brown']
#print(random.choice(colors))
#print(random.sample(colors , k=3))


#a=['Hi',"Jhone",'Welcome','To','Python']
#print(" ".join(a))


import random
import string
#print(string.ascii_lowercase)
#print(string.ascii_uppercase)
#print(string.digits)
#print(string.ascii_letters)
#print(string.punctuation)


content=list(string.ascii_letters)+list(string.digits)+list(string.punctuation)
l=int(input("Enter your password length:"))
password=random.sample(content , k=l)
final="".join(password)
print(f"Your password :{final}")


