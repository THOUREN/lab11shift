import random
from random import randint
ke = open("key.txt", 'w', encoding = 'utf-8')
ke.write(str(randint(100, 9999)))
ke.close()

print("Выберите действие: ")
print("	1. Вывести Исходный текст")
print("	2. Вывести ключь")
print(" 3. Вывести Зашифрованный текст")
print("	4. Вывести Расшифрованный текст")
dst = input()

s2 = ''
original = open("lab11original.txt", 'r')
s1 = original.read()
k = open("key.txt", 'r', encoding = 'utf-8')
key = k.read()
encrypted = open("lab11encrypted.txt", 'w', encoding = 'utf-8')
decrypted = open("lab11decrypted.txt", 'w', encoding = 'utf-8')
if int(dst) == 1:
	print("Исходный текст: ", s1)
for i in range(len(s1)):
	if ord(s1[i]) < 253:
		s2 = s2 + chr(ord(s1[i])+int(key[i%len(key)]))
	else:
		s2 = s2 + chr(ord(s1[i])+int(key[i%len(key)])-255)
encrypted.write(s2)
encrypted.close()
encrypted = open("lab11encrypted.txt", 'r', encoding = 'utf-8')
en = encrypted.read()
if	int(dst) == 2:
	print("Ключь: ", key)

if int(dst) == 3:
	print("Зашифрованная строка:", en)

s1 = ''
for i in range(len(s2)):
	if ord(s2[i]) < 253:
		s1 = s1 +chr(ord(s2[i])-int(key[i%len(key)]))
	else:
		s1 = s1 +chr(ord(s2[i])-int(key[i%len(key)])+255)
decrypted.write(s1)
decrypted.close()
decrypted = open("lab11decrypted.txt", 'r', encoding = 'utf-8')
de = decrypted.read()
if int(dst) == 4:
	print("Дешифрованная строка:", de)
print("----------------------------------------------")
