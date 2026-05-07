import os
os.system("cls")

file = open("kichik_harf.txt")

text = file.read().split()

for i in text:
    print(i.capitalize(), end=" ")