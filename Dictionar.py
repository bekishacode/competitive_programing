# Accesing Dictionary
n = int(input())
phoneBook = {}
for i in range(n):
    key, value = input().split(' ')
    phoneBook[key] = value
for j in range(n):
    name = input()
    if phoneBook.get(name):
         print(name+'='+phoneBook.get(name))
    else:
         print('Not found')
