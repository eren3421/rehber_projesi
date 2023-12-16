def arama():
    import ast
    dosya=open("rehber.txt","r")
    t=[]
    for x in dosya.readlines():
        z=ast.literal_eval(x)
        t.append(z)
    dosya.close()
    b=False
    abc=input("Arama çubuğuna girin.")
    for x in range(len(t)):
        if((abc.lower() in t[x]["ad"].lower()) or (abc.lower() in t[x]["soyad"].lower())):
           b=True
           print(str(t[x]))
    if b==False:
        print("Kişi bulunamadı.")
