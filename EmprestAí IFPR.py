#introdução do trabalho
print("=== LISTA DE MATERIAIS ===")
print("Escolha um dos materiais para emprestar:")
print("lapis, caderno, caneta, apontador") #materiais no estoque

#inputs iniciais do código
A = input()
lapis = 10 #numero de estoque
caderno = 5
caneta = 25
apontador = 30


if A == "lapis":
    lapis -= 1 # código para quando o lapis for selecionado ele seja diminuido
    print("Lápis em estoque:", lapis)

elif A == "caderno":
    caderno -= 1 # código para quando o caderno for selecionado ele seja diminuido
    print("Caderno em estoque:", caderno)

elif A == "caneta":
    caneta -= 1 # código para quando o caneta for selecionado ele seja diminuido
    print("Caneta em estoque:", caneta)

elif A == "apontador":
    apontador -= 1 # código para quando o apontador for selecionado ele seja diminuido
    print("Apontador em estoque:", apontador)

else:
    print("Material inválido.") #código para se não escrever os materiais disponiveis ou numeros