
n = int(input("Введіть кількість рядків: "))

best = ""
max_count = 0

for i in range(n):
    s = input("Введіть рядок: ")
    count_max = 0

    for c in s:
        count = s.count(c)
        if count > count_max:
            count_max = count

    if count_max > max_count:
        max_count = count_max
        best = s

print("Рядок з найбільшою кількістю однакових символів:", best)