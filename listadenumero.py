numero=[]
print("Sequêcia de números".upper())
valor=float(input("digite um número(0 programa encerrado)\n" .upper()))
n_formatado = "{:.3f}".format(valor)

while (valor!=0):
    numero.append(valor)
    print(*numero, sep="\n ")
    valor=float(input("digite um número(0 programa encerrado)\n" .upper()))
    
        
else:
    print(*numero, sep=("\n"))
    print("sequência encerrada".upper())
    
    
    
    
        
