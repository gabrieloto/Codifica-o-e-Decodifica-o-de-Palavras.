from string import ascii_uppercase
letras = list(ascii_uppercase)
def code(message, key, option):
    code = ""
    for l in message:
        charUnicode = ord(l)-65
        code += letras[(charUnicode+key) %len(letras)] if l in letras else l
    if (option == 1):
        print(" mensagem codificada: ", end="")
    else:
        print(" mensagem decodificada: ", end="")        
    print(code, "\n")
def decode(message, key):
    code(message, len(letras)-key, option)
proceed = 1
option = 0
print("Codificação e descodificação de palavras")
while (proceed != 0):
    option = int(input("\n Quer codificar ou decodificar uma palavra?\nDigite\n1 para codificação\n2 para decodificação\nDigite: "))
    if (option == 1):
        code(input("\n qual a palavra que deseja codificar: ").upper(), int(input("coloque a key de codificação: ")), option)
    elif (option == 2):
        decode(input("\nqual a palavra que deseja decodificar: ").upper(), int(input("coloque a key de descodificação: ")))
    proceed = int(input("quer codificar ou decodificar outra palavra? Digite\n1 para sim\n2 para não\nEscolha sua opção: "))
