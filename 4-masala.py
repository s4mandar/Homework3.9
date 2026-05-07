import os
os.system("cls")

file = open("butun_sonlar.txt")

text = file.read()

sonlar = list(map(int, text.split()))

print(round(sum(sonlar) / len(sonlar)))