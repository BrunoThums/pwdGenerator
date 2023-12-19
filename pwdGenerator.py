#!/usr/bin/python
import sys
from termcolor import colored # Add color to text

def processar_login(login, adiciona_prefixo, adiciona_sufixo, capitalizar_primeira_letra):
    # Adiciona o sufixo ao final do login, se adiciona_sufixo não for None
    if adiciona_prefixo:
        login = adiciona_prefixo + login
    
    # Adiciona o prefixo ao início do login, se adiciona_prefixo não for None
    if adiciona_sufixo:
        login = login + adiciona_sufixo

    # Torna a primeira letra maiúscula, se capitalizar_primeira_letra for True
    if capitalizar_primeira_letra:
        login = login.capitalize()

    return login


def main():
    # Nome do arquivo de logins
    arquivo_de_saida = "logins_processados.txt"
    adiciona_sufixo = None
    adiciona_prefixo = None
    capitalizar_primeira_letra = False
    
    if len(sys.argv) < 2:
        print("Usage: python pwdGenerator logins.txt")
        print(colored("       [-s ou -sufixo] sufixo ", "green", attrs=['bold']),end="")
        print("-> adiciona ao final do login a palavra desejada")
        print(colored("       [-p ou -prefixo] prefixo ", "green", attrs=['bold']),end="")
        print("-> adiciona ao início do login a palavra desejada")
        print(colored("       [-c ou -capitalizar] ", "green", attrs=['bold']),end="")
        print("-> torna a primeira letra maiúscula")
        print(colored("       [-o ou -output] arquivo_saida.txt", "green", attrs=['bold']),end="")
        print("-> define o nome do arquivo de saída")
        sys.exit(1)

    arquivo_logins_entrada = sys.argv[1]
    i = 2
    # Verifica os argumentos opcionais
    while i <len(sys.argv):
        arg = sys.argv[i]
        if arg == "-p" or arg == "-prefixo":
            i += 1
            if i < len(sys.argv):
                adiciona_prefixo = sys.argv[i]
            else:
                print("Erro: Argumento -p requer um prefixo.")
                sys.exit(1)
        elif arg == "-s" or arg == "-sufixo":
            i += 1
            if i < len(sys.argv):
                adiciona_sufixo = sys.argv[i]
            else:
                print("Erro: Argumento -s requer um sufixo.")
                sys.exit(1)
        elif arg == "-c" or arg == "-capitalizar":
            capitalizar_primeira_letra = True
        elif arg == "-o" or arg == "-output":
            i += 1
            if i < len(sys.argv):
                arquivo_de_saida = sys.argv[i]
        else:
            print(f"Erro: Argumento desconhecido: {arg}")
            sys.exit(1)

        i += 1

    try:
        # Abre o arquivo de entrada em modo de leitura
        with open(arquivo_logins_entrada, 'r') as entrada:
            # Lê cada linha do arquivo
            linhas = entrada.readlines()

            # Processa cada linha
            logins_processados = [processar_login(linha.strip(), adiciona_prefixo, adiciona_sufixo, capitalizar_primeira_letra) for linha in linhas]

        # Abre o arquivo de saída em modo de escrita
        with open(arquivo_de_saida, 'w') as saida:
            # Escreve os logins processados no arquivo de saída
            for login_processado in logins_processados:
                saida.write(login_processado + "\n")

        print(f"Logins processados e salvos em {arquivo_de_saida}")

    except FileNotFoundError:
        print(f"Arquivo de logins não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()

    
