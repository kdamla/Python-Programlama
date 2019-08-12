"""
Problem 5
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""

sayi1 = float(input("Sayı1"))
sayi2 = float(input("Sayı2"))

sayi1, sayi2 = sayi2, sayi1

print("Yeni sayı1 {}, yeni sayı2 {}".format(sayi1, sayi2))
