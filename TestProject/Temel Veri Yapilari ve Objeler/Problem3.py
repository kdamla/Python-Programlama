"""
Problem 3
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünün toplam ne kadar ödemesini gerektiğini hesaplayın.
"""

yakit = float(input("Aracın kilometrede yaktığı yakıt tutarı:"))
yol = float(input("Kaç km yol kat edildi?"))

print("Ödenmesi gereken tutar: {} TL".format(yakit*yol))