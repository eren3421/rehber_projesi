def numara_sil():
    import ast
    dosya=open("rehber.txt","r")
    t=[]
    for x in dosya.readlines():
        y=ast.literal_eval(x)
        t.append(y)
    dosya.close()
    isim=input("Silmek istedğiniz adı ve soyadı 1 boşluk bırakarak girin.")
    b=False
    for x in range(len(t)):
        if(str(t[x]["ad"].lower()+" "+t[x]["soyad"].lower())==isim.lower()):
            t.pop(x)
            print("Kişi silindi.")
            b=True
            break
    if b==False:
        print("Kişi bulunamadı.")
    dosya=open("rehber.txt","w")
    for y in t:
        dosya.write(str(y)+"\n")
    dosya.close()
        
    
        
    
