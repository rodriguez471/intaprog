somavalor=0
v_negativo=0
for i in range(20):
    valor=int(input("digite o valor: "))
    if valor>=0:
        somavalor+=valor
    else:
        v_negativo+=1
print("a soma dos valores positivo e:", somavalor) 
print("a quantidade de valores negativo e:", v_negativo)       