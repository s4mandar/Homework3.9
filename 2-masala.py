import os
os.system("cls")

user_search = input("So'z kiriting: ").lower()

file = open("malumot.txt")

text = file.read().lower()

check = text.find(user_search)

if check >= 0:
    print("Siz kiritgan so'z faylda bor")
else:
    print("Siz kiritgan so'z faylda yo'q")