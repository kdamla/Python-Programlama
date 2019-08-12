"""
Problem 2
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""

kilo = float(input("Kilo giriniz:"))
boy = float(input("Boy(m) giriniz"))

sonuc = kilo / (boy ** 2) #(boyun karesi)

print("Beden kitle indeksi: {}".format(sonuc))