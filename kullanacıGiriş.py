evet = 1
hayır = 0

# Kullanıcının Kayıt Olduğu Kısım

kAdi = input("Kullanıcı Adınızı Belirleyiniz :")
kSifre = input("Şifreinizi Belirleyiniz : ")
print("Başarıyla Kayıt Oldunuz. Giriş İçin Yönlendiriliyorsunuz...")

# Kullanıcının Giriş Kısmı

girishakki = 3

while girishakki > 0:
    girishakki -= 1
    gkAdi = input("Kullanıcı Adınızı Giriinz : ")
    gSifre = input("Şifrenizi Giriniz : ")
    
    if gkAdi == kAdi and gSifre == kSifre:
        print(f"{kAdi} Hoş geldin... Anasayfa'ya Yönlendiriliyor...")
        break
    else:
        print(f"Kullanıcı Adı ya da Şifre Yanlış! Kalan Giriş Hakkınız {girishakki}.")
        if girishakki == 0:
            print("Şifre Sıfırlama İşlemi İçin Yönlendiriliyorsunuz...")
            continue
    
    # Kullanıcının Şireyi Sıfırlatma Yeri

while girishakki == 0:

    try:
        print("Şifrenizi Sıfırlamak İstiyor Musunuz? 1-Evet, 0-Hayır")
        cevap = int(input("Lütfen Birini Seçiniz :"))

        if cevap == evet:
            yenisifre = input("Yeni Şifenizi Giriniz :")
            yenisifre = kSifre.replace(kSifre, yenisifre)

            if yenisifre == kSifre:
                print("Yeni Şifreniz Eskisiyle Aynı Olamaz!")
            else:
                print("Şifreniz Başarıyla Değiştirildi... Ana Menüye Yönlendiriliyorsunuz...")
                break

        elif cevap == hayır:
            print("Hesap ile Bağlantınız Kesildi! Çıkış Yapılıyor...")
            break
        else:
            print("Geçersiz Giriş. Lütfen Kontrol Ediniz.")
        continue
    except:
        print("Geçersiz Tuşlama. Lütfen Kontrol Ediniz.")
        continue


