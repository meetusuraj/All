import random
import string

number_len = int(input("Please enter the number of password: "))
letter_len=int(input("Please enter the letter of password: "))

number_list=''.join(random.choice(string.digits) for i in range(number_len))
letter_list=''.join(random.choice(string.ascii_letters) for i in range(letter_len))

format_pass=number_list + letter_list + "@#$%^&*!"

if len(format_pass) < 6:
    print("Invalid password length,minimum 6")
result=random.sample(format_pass,len(format_pass))
password=''.join(result)
print('Your password is',password)
