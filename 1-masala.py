import os
os.system("cls")

file = open("raqamlar.txt")

text = file.read().split()

file2 = open("gap.txt", "w")

for i in text:
    file2.write(chr(int(i)))