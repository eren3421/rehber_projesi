import ekle
import liste
import duzenle
import sil
import ara
def anamenu():
    print("╔═════════════════════╗")
    print("║   REHBER PROGRAMI   ║")
    print("║1- Rehbere Ekle      ║")
    print("║2- Numara Listele    ║")
    print("║3- Numara Sil        ║")
    print("║4- Numara  Düzenle   ║")
    print("║5- Kişi Ara          ║")
    print("║6- Çıkış             ║")
    print("╚═════════════════════╝")
    secim=input("Seçimini yap:")
    if(secim=='1'):
        ekle.rehbere_ekle()
        liste.listele()
        anamenu()
    elif(secim=='2'):
        liste.listele()
        anamenu()
    elif(secim=='3'):
        sil.numara_sil()
        liste.listele()
        anamenu()
    elif(secim=='4'):
        duzenle.numara_duzenle()
        liste.listele()
        anamenu()
    elif(secim=='5'):
        ara.arama()
        anamenu()
    elif(secim=='6'):
        print("Çıkış yapılıyor...")
#anamenu()
