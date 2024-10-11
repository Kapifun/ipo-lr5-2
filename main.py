spisok1=input("Введите первую строку:")
spisok2=input("Введите вторую строку:")

sort_spisok1 = sorted(spisok1.lower())
sort_spisok2 = sorted(spisok2.lower())
                  
if sort_spisok1 == sort_spisok2:
    print("Строки анаграммны")
else:
    print("Строки не анаграммны")