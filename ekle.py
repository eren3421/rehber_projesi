def rehbere_ekle():
        dosya=open("rehber.txt","a")
        ad=input("Ad:")
        soyad=input("Soyad:")
        numara=input("numara")
        yazilacak={'ad':ad,'soyad': soyad,'numara': numara}
        dosya.write(str(yazilacak)+"\n")
        dosya.close()
