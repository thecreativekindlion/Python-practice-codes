işlem=input("İşlemi giriniz:")
sayi1=int(input("sayi1:"))
sayi2=int(input("sayi2:"))

if işlem =="1":
    sonuç=int(sayi1)+int(sayi2)
    print("Sonuc:",str(sonuç))

elif işlem =="2":
    sonuç=int(sayi1)-int(sayi2)
    print("Sonuc:",str(sonuç))

elif işlem =="3":
    sonuç=int(sayi1)*int(sayi2)
    print("Sonuç:",str(sonuç))
elif işlem =="4":
    sonuç=int(sayi1)/int(sayi2)
    print("Sonuç:",str(sonuç))