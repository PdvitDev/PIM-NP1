import random

def quiz(perguntas):
    pontos= 0
    #percorre perguntas
    random.shuffle(perguntas)

    for pergunta in perguntas:
        print(pergunta["pergunta"])

        #percorre os dicts dentro de perguntas
        for i, alternativa in enumerate(pergunta["alternativas"]):
            i += 1
            print(f"{i}) {alternativa}")#mostra e formata as alternativas
        resposta_usuario = int(input("Sua resposta (digite o numero): "))

        #verificacao da resposta do usuario
        if resposta_usuario == pergunta["resposta_correta"]:
            print("Resposta correta!")
            pontos += 1
        else:
            print("Resposta incorreta!")
    print(f"Voce acertou {pontos} de {len(perguntas)} perguntas!")

def main():
    #list onde dentro de cada index tem um dict
    perguntas = [{
        "pergunta" : "Qual operador lógico em Python é usado para negar uma condição?",
        "alternativas" :["and", "or", "not"], #list
        "resposta_correta": 3,
    },
    {
        "pergunta" : "Qual das seguintes estruturas é usada para repetir um bloco de código várias vezes em Python?",
        "alternativas" :["if", "for", "else"],
        "resposta_correta": 2,
    },
    {
        "pergunta" : "Qual o nome do tipo de dado que respresenta numeros inteiros?",
        "alternativas" :["int", "float", "string"],
        "resposta_correta": 1,
    },
    {
        "pergunta" : "Qual das seguintes opcoe e a melhor pratica para proteger suas senhas?",
        "alternativas" : [
            "Usar a mesma senha para todas as suas contas online",
            "Anotar suas senhas em um papel e guarda-las em algum lugar seguro" ,
            "Criar senhas complexas e usar um gerenciador de senhas"
        ],
        "resposta_correta" : 3,
    },
    {
        "pergunta" : "Qual das seguintes opcoes podem ajudar a proteger computadores de malwares?" ,
        "alternativas" :[
            "Clicar em qualquer link e baixar qualquer arquivo que encontrar online",
            "Desativar o firewall do computador",
            "Manter softwares de antivirus atualizados e evitar baixar arquivos de fontes nao confiaveis"
        ] ,
        "resposta_correta" : 3,
    },
    ]
    escolha = input("Deseja iniciar o quiz? (S / N): ")

    if escolha == "S" or "s":
        quiz(perguntas)

main()
