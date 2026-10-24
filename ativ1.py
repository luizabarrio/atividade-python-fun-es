def verificar_acesso(usuario, senha):
    usuario_correto = "admin"
    senha_correta = "1234"

    if usuario == usuario_correto and senha == senha_correta:
        return "Acesso permitido"
    elif usuario != usuario_correto and senha != senha_correta:
        return "Usuário e senha incorretos"
    elif usuario != usuario_correto:
        return "Usuário incorreto"
    else:
        return "Senha incorreta"


usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

print(verificar_acesso(usuario, senha))