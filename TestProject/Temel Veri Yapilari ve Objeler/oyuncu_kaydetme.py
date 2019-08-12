print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun Adı:")
soyad = input("Oyuncunun Soyadı:")
takım = input("Oyuncunun Takımı:")

bilgiler = [ad, soyad, takım]

print("Bilgiler kaydediliyor")

print("Ad: {}\nSoyad:{}\ndTakım:{}\n".format(bilgiler[0], bilgiler[1], bilgiler[2]))
