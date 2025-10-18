import random
password = "QWERTYUIOPLKJMNHGBFVDCSXAZ0123456789mznxbcvlkfjhgdsaqpoiuytrwe"
length_password = int(input("Enter a length of password: "))
a = "".join(random.sample(password, length_password))
print(f"Your password is: {a}")
