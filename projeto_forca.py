#Nícolas Soares Telles e Lucas Vinícius dos Santos Almeida
# ADS - Turma B - 1°Semestre
print("BEM VINDO AO JOGO DA FORCA")
import requests
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
palavras = requests.get(url).text.split()
from random import choice
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
forca = ['''
+========+
         |
         |
         |
         |
         |
+========+''','''
  +======+
  |      |
         |
         |
         |
         |
+========+''','''
  +======+
  |      |
  O      |
         |
         |
         |
+========+''','''
  +======+
  |      |
  O      |
 /       |
         |
         |
+========+''','''
  +======+
  |      |
  O      |
 / \     |
         |
         |
+========+''','''
  +======+
  |      |
  O      |
 /|\     |
         |
         |
+========+''','''
  +======+
  |      |
  O      |
 /|\     |
 /       |
         |
+========+''','''
  +======+
  |      |
  O      |
 /|\     |
 / \     |
         |
+========+''']

#FUNÇÕES DO JOGO 

def jogar_novamente():
    print("Deseja iniciar o jogo?")
    print("1 - SIM ")
    print("2 - NÃO ")
    decisao = input()
    if decisao == "1":
        return True
    elif decisao == "2":
        return False
    else:
        print("Digite um número válido")
        jogar_novamente()

def desenha():
    print(forca[len(erradas)])
    cont = 0 
    for x in sorteada:
        if x in certas:
            cont += 1
            print(x,end = ' ')
        else:
            print('_', end = ' ')
    return cont
          

def escolhe():
    sorteada = choice(palavras)
    return sorteada


def chute(letras,x):
    if x in letras:
        letra = choice(alfabeto)
        print("Você ja digitou essa letra!")
        print('Tente com: ',letra)
        return('Tente com: ',letra)
        
def ganhou(certo,palavra):
    if certo == len(palavra):
        return True
    else:
        return False
    
def verifica(string):
    string = string.lower()
    if string in alfabeto and len(string)== 1:
        return True
    else:
        return False

jogar = jogar_novamente()
while(jogar):
    certas = erradas = ''
    resp = ""
    sorteada = escolhe()
    #sorteada = "carol"
    tamanho = len(sorteada)
    desenha()
    while len(erradas) < 7 :
        print("")
        letra = input("Digite uma letra: ")
        letra = letra.lower()
        continuar = verifica(letra)
        if (continuar):
            letras = certas+erradas
            if letra in certas+erradas:
                print("")
                result = chute(letras,letra)
            else:
                if letra in sorteada:
                    certas = certas + letra
                    #desenha()
                    certo = desenha()
                    resp = ganhou (certo,sorteada)
                    if resp:
                        break
                else:
                    erradas = erradas + letra
                    desenha()
        else:
            print("Digite uma letra válida!")
            

    if len(erradas)< 7:
        print("")
        print("") 
        print("Você ganhou !")
        print("A palavra sorteada era: ",sorteada)
        jogar = jogar_novamente()
    else:
        print("")
        print("")
        print("Você perdeu ! ")
        print("A palavra sorteada era: ",sorteada)
        jogar = jogar_novamente()
    
