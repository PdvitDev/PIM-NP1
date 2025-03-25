import os
import platform

#apenas para estetica
def limpar_terminal():
    sistema = platform.system()

    if sistema == "Windows":
        os.system('cls')

    else:  # Linux ou macOS
        os.system('clear')

def quiz(perguntas):
    pontuacao = 0
    #percorre o array
    for pergunta in perguntas:
        print(pergunta["pergunta"])

        #percorre os dicts dentro do array
        for i, alternativa in enumerate(pergunta["alternativas"]):
            print(f"{i + 1}. {alternativa}")#formata as alternativas
        resposta_usuario = int(input("Sua resposta (digite o numero): "))

        if resposta_usuario == pergunta["resposta_correta"]:
            limpar_terminal()
            print("Resposta correta!")
            pontuacao += 1
        else:
            limpar_terminal()
            print("Resposta incorreta!")

    print(f"Voce acertou {pontuacao} de {len(perguntas)} perguntas!")

def main():
    #array onde dentro de cada index tem um dict
    perguntas = [{
        "pergunta" : "Qual operador lógico em Python é usado para negar uma condição?",
        "alternativas" :["and", "or", "not"],
        "resposta_correta": 3,
    },
    {
        "pergunta" : "Qual das seguintes estruturas de controle de fluxo é usada para repetir um bloco de código várias vezes em Python?",
        "alternativas" :["if", "for", "else"],
        "resposta_correta": 2,
    },
    ]

    quiz(perguntas)
main()
