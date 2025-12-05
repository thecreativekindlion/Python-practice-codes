import random
secenekler=("taş","kağıt","makas")
pcpuan,benpuan=0,0
bitecekpuan=int(input("Oyun kaçta bitsin?"))
while 1:
    pctercih=random.choice(secenekler)
    print(f"Skor tablosu : PC:{pcpuan} ve SİZ: {benpuan}")
    bentercih=input("Lütfen tercih yapınız: ")
    if bentercih in secenekler:
        #kontrol aşamam
        print(f"PC: {pctercih} SİZ: {bentercih}")
        if pctercih=="taş" and bentercih=="makas":
            print("PC kazandı")
            pcpuan=pcpuan+1
        elif pctercih=="taş" and bentercih=="kağıt":
            benpuan=benpuan+1 
            print("Siz kazandınız.")

        elif pctercih=="kağıt" and bentercih=="makas":
            print("Siz kazandınız.")
            benpuan=benpuan+1

        elif pctercih=="kağıt" and bentercih=="taş":
            print("PC kazandı.")
            pcpuan=pcpuan+1

        elif pctercih=="makas" and bentercih=="kağıt":
            print("PC kazandı")
            pcpuan=pcpuan+1

        elif pctercih=="makas" and bentercih=="taş":
            print("Siz kazandınız")
            benpuan=benpuan+1

        else:
            print("BERABERE")
            #PUANLARalındı bakalım kimse kazandı mı
        if pcpuan==bitecekpuan:
            print(f"Skor tablosu : PC:{pcpuan} ve SİZ: {benpuan}")
            print("Maçın galibi PC...")
            break
        if benpuan== bitecekpuan   :
            print(f"Skor tablosu : PC:{pcpuan} ve SİZ: {benpuan}")
            print( "Maçın galibi sizsiniz...")
            break
    else:
        print("Lütfen geçerli bir seçenek giriniz.")