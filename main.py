Numero1 = int (input("Digite um numero"))
Numero2 = int (input("Digite o segundo numero"))

print("SELECIONE A OPÇÃO DESEJADA")
print("+ para Adição")
print("- para Subtração")
print("* para multiplicação")
print("/ para divisão")

operacao = input("/nQual operação você deseja realizar?")

if operacao == "+":
    adição = Numero1 + Numero2
    print("O resultado é:" + str(adição))

if  operacao == "-":
    subtração = Numero1 - Numero2
    print("O resultado é:" + str(subtração))

if operacao == "*":
    multiplicação = Numero1 *  Numero2
    print("O resultado é:" + str(multiplicação))

if operacao == "/":
    divisão = Numero1 /  Numero2
    print("O resultado é:" + str(divisão))

print("tmj")