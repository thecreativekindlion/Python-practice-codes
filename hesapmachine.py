

sayi1=int(input("Sayi1 girin: "))
sayi2=int(input("Sayi2 girin: "))
while True:
    print("1-Topla")
    print("2-Çıkar")
    print("3-Çarp")
    print("4-Böl")
    print("0-Çıkış")
    tercih=int(input("Tercihinizi giriniz: "))
    if tercih==0:
        print("Güle gülee")
        break
    elif tercih==1:
        sonuc=sayi1+sayi2
        print(f"{sayi1} ile {sayi2} toplanırsa {sonuc} elde edilir.")
        input("Menüye dönmek için bir tuşa basınız.")

    elif tercih==2:
        sonuc=sayi1-sayi2
        print(f"{sayi1} den {sayi2} çıkarılırsa {sonuc} elde edilir.")
        input("Meüye dönmek için bir tuşa basınız.")
    elif tercih==3:
        sonuc=sayi1*sayi2
        print(f"{sayi1} ile {sayi2} çarpılırsa {sonuc} elde edilir.")
        input("Menüye dönmek için bir tuşa basınız.")
    elif tercih==4:
        if sayi2==0:
            print("Sıfır bölme hatası")
        else:
        sonuc=sayi1/sayi2
        print(f"{sayi1} ,{sayi2} ye bölünürse {sonuc} elde edilir.")
        input("Menüye dönmek için bir tuşa basınız.")
    else:
        print("Hatalı bir tuşa bastınız.")