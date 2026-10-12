s = input("Введіть рядок слів: ")

words = s.split()
shortest = min(words, key=len)

if shortest == shortest[::-1]:
    print("Найкоротше слово є паліндромом:", shortest)
else:
    print("Найкоротше слово не є паліндромом:", shortest)