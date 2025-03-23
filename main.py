import json
import bcrypt
import os
import platform

def armazenar_usuario(email, nome, senha, nome_arquivo="usuarios.json"):

    try:
        with open(nome_arquivo, "r") as arquivo:
            usuarios = json.load(arquivo)

    except FileNotFoundError:
        usuarios = []

    #Hash da senha
    senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    usuarios.append({
        "email": email,
        "nome": nome,
        "senha": senha_criptografada.decode('utf-8') #armazena hash como string
    })

    with open(nome_arquivo, "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4) #indentação


def ler_usuarios(nome_arquivo="usuarios.json"):

    try:
        with open(nome_arquivo, "r") as arquivo:
            usuarios = json.load(arquivo)
        return usuarios
    

    except FileNotFoundError:
        return []

def verificar_usuario(email, senha, nome_arquivo="usuarios.json"):
    usuarios = ler_usuarios(nome_arquivo)

    for usuario in usuarios:
        if usuario["email"] == email:
            senha_criptografada = usuario["senha"].encode('utf-8')
            return bcrypt.checkpw(senha.encode('utf-8'), senha_criptografada), print("-----USUARIO LOGADO COM SUCESSO-----")
        
    return False # caso de usuario não encontrado

def cadastro_usuario(arquivo_usuarios):
    print("-----CADASTRO DE USUARIO-----")
    email = input("Insira seu email:")
    nome = input("Insira seu nome:")
    senha = input("Insira sua senha:")
    armazenar_usuario(email, nome, senha, arquivo_usuarios)

def login_usuario():
    print("------LOGIN USUARIO------")
    email = input("Insira seu email:")
    senha = input("Insira sua senha:")
    verificar_usuario(email, senha)

def limpar_terminal():
    sistema = platform.system()

    if sistema == "Windows":
        os.system('cls')

    else:  # Linux ou macOS
        os.system('clear')


def main():
    arquivo_usuarios = "usuarios.json"

    cadastro_usuario(arquivo_usuarios)

    limpar_terminal()

    login_usuario()



main()
