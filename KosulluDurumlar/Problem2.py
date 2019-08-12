"""
Problem 2
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""

a = int(input("1. sayı:"))
b = int(input("2. sayı:"))
c = int(input("3. sayı:"))

if a >= b and a >= c:
    print("En büyük sayı:",a)
elif b >= a and b >= c:
    print("En büyük sayı:",b)
elif c >= a and c >= b:
    print("En büyük sayı:",c)

"""enBuyuk = None
if sayi1 > sayi2:
    if sayi1 > sayi3:
        enBuyuk = sayi1
    else:
        enBuyuk = sayi3
elif sayi2 > sayi3:
    enBuyuk = sayi2
else:
    enBuyuk = sayi3

print("En büyük sayı: {}".format(enBuyuk))"""