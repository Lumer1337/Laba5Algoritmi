def Recurrence(cena, ves, vmestimost):
    a = [0] * (vmestimost + 1)
    for i in range(1, vmestimost + 1):
        for j in range(0, len(ves)):
            if (ves[j] <= i):
                a[i] = max(a[i], cena[j] + a[i - ves[j]])
            print(a[i], end=" ")
        print()
    print()
    return a[vmestimost]

def knapSack(vmestimost, ves, cena):
    a = [[0 for x in range(vmestimost + 1)] for x in range(len(cena) + 1)]
    for i in range(1, len(cena) + 1):
        for w in range(1, vmestimost + 1):
            if ves[i - 1] <= w:
                a[i][w] = max(cena[i - 1] + a[i - 1][w - ves[i - 1]], a[i - 1][w])
            else:
                a[i][w] = a[i - 1][w]
    print(a)
    print()
    return a[len(cena)][vmestimost]

cena = [5, 25, 6, 5, 2]
ves = [1, 4, 1, 7, 3]
print("Введите объём рюкзака:")
vmestimost = int(input())
print("Цена: \t")
for i in range(0, 5):
    print(cena[i], end=" ")

print("")
print("Вес:")
for i in range(0, 5):
    print(ves[i], end=" ")

print("")
print("Стоимость вещей при заполнении с повторениями: ")
print(Recurrence(cena, ves, vmestimost))
print("Стоимость вещей при заполнении без повторений: ")
print(knapSack(vmestimost, ves, cena))