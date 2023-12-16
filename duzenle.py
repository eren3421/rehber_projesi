def numara_duzenle():
    import ast
    dosya=open("rehber.txt","r")
    t=[]
    for x in dosya.readlines():
        z=ast.literal_eval(x)
        t.append(z)
    dosya.close()
    b=False
    isim=input("Düzenlemek istedğiniz adı ve soyadı 1 boşluk bırakarak girin.")
    for x in range(len(t)):
        if(str(t[x]["ad"].lower()+" "+t[x]["soyad"].lower())==isim.lower()):
             b=True
             no=input("Yeni numarayı girin")
             t[x]["numara"]=no
             break
    if b== False:
        print("Kişi bulunamadı")
    dosya=open("rehber.txt","w")
    for y in t:
        dosya.write(str(y)+"\n")
    dosya.close()
