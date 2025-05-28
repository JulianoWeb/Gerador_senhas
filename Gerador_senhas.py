import random
import string
import sys
from colorama import init, Fore, Style

# Inicializar o colorama
init(autoreset=True)

def gerar_senha(tamanho=12, usar_numeros=True, usar_simbolos=True):
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation

    caracteres = letras
    if usar_numeros:
        caracteres += numeros
    if usar_simbolos:
        caracteres += simbolos

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def menu():
    while True:
        print(Fore.CYAN + "\n=== Gerador de Senhas Seguras ===")
        print(Fore.YELLOW + "1. Gerar nova senha")
        print(Fore.RED + "2. Sair")
        opcao = input(Fore.WHITE + "Escolha uma opção (1/2): ")

        if opcao == '1':
            try:
                tamanho = int(input(Fore.WHITE + "Tamanho da senha (padrão 12): ") or 12)
            except ValueError:
                print(Fore.RED + "Valor inválido. Usando tamanho padrão (12).")
                tamanho = 12

            incluir_numeros = input(Fore.WHITE + "Incluir números? (s/n, padrão s): ").lower() or 's'
            incluir_simbolos = input(Fore.WHITE + "Incluir símbolos? (s/n, padrão s): ").lower() or 's'

            senha = gerar_senha(
                tamanho,
                usar_numeros=incluir_numeros == 's',
                usar_simbolos=incluir_simbolos == 's'
            )

            print(Fore.GREEN + f"\n🔐 Sua senha gerada:\n{senha}")

        elif opcao == '2':
            print(Fore.MAGENTA + "Saindo... Até mais!")
            sys.exit()
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
