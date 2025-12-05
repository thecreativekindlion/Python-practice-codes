
for sayi in range(100,120): #100 ve 999 dahil arası
    birinci=sayi//100
    ikinci=(sayi-(birinci*100))//10
    ucuncu=sayi%10
  
    kuptoplam=birinci**3+ikinci**3+ucuncu**3
    if sayi==kuptoplam:
        print(f"{sayi} ARMSTRONG")