def listele():
        try:
           dosya=open("rehber.txt","r")
           a=1
           print("═════════════Kayıt-Listesi═════════════")
           for kayit in dosya.readlines():
               print(a,kayit)
               a=a+1
           print("═══════════════════════════════════════")
           dosya.close()
        except:
            print("Dosya yok")

