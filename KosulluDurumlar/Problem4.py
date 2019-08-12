"""
Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
"""

print("Geometrik şekil hesaplama işlemi")

girdiSekil = input("Üçgenin tipini hesaplamak istiyorsanız Üçgen, Dörtgenin tipini hesaplamak istiyorsanız Dörtgen yazınız")
sekil = None

if girdiSekil == "Üçgen" or girdiSekil == "üçgen":
    sekil = "üçgen"
elif girdiSekil == "Dörtgen" or girdiSekil == "dörtgen":
    sekil = "dörtgen"
else:
    print("Girilen şekil geçersiz.")

if sekil == "üçgen":
    a = int(input("1. kenar:"))
    b = int(input("2. kenar:"))
    c = int(input("3. kenar:"))

    ucgenOlusabilir = False

    if abs(a - b) < c < abs(a + b):
        ucgenOlusabilir = True
    elif abs(a - c) < b < abs(a + c):
        ucgenOlusabilir = True
    elif abs(b - c) < a < abs(b + c):
        ucgenOlusabilir = True
    else:
        ucgenOlusabilir = False

    if ucgenOlusabilir:
        if a == b and a == c:
            print("Eşkenar üçgen")
        elif a == b or a == c or b == c:
            print("İkizkenar üçgen")
        else:
            print("Çeşitkenar üçgen")
    else:
        print("Verilen değerler üçgen belirtmiyor.")

elif sekil == "dörtgen":
    a = int(input("1.kenar:"))
    b = int(input("2.kenar:"))
    c = int(input("3.kenar:"))
    d = int(input("4.kenar:"))

    if a == b and b == c and c == d:
        print("Kare")
    elif a == b or b == c or c == d or a == c or a == d or b == d:
        print("Dikdörtgen")
    else:
        print("Dörtgen")

print("Program sonu")