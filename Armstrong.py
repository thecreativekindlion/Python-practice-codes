
for number in range(100,120): #100 ve 999 dahil arası
    first=number//100
    second=(number-(first*100))//10
    third=number%10
  
    sum=first**3+second**3+third**3
    if number==sum:
        print(f"{number} ARMSTRONG")
        
