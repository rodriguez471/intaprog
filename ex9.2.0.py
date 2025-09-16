número=int(input("digite um número:"))
cont=0
divisor=1
while divisor>=número:
    if número+divisor:
     cont+=1
     if número<=divisor:
      divisor=+1
    if cont==2:
        print("o numero é primo!")
else:
        print("o número não é primo!")
        
