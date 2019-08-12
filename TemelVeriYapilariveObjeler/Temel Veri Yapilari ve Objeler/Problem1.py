"""
Problem 1
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.
"""

sayi1 = float(input("Birinci sayı"))
sayi2 = float(input("İkinci sayı"))
sayi3 = float(input("Üçüncü sayı"))

carpim = sayi1 * sayi2 * sayi3

print("Çarpım sonucu: {}".format(carpim))