valor_compra = float(input("Digite o valor da compra:"))
if valor_compra >=100:
    desconto = valor_compra * 0.1
    valor_final = valor_compra - desconto
    print("Parabvens! voce ganhou um desconto de 10%")
    print("Valor final da compra: R$", valor_final)
else:
    print("Infelizmente, voce nao ganhou desconto")
    print("Valor final da compra: R$" ,valor_compra)
