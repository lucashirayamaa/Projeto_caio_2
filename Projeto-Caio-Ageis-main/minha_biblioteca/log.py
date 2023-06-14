
class SistemaLogin:
    def __init__(self):
        self.usuarios = []
        self.senhas = []
        self.logado = False

    def cadastrar_usuario(self):
        usuario = input("Digite o nome do usuário: ")
        senha = input("Digite a senha do usuário: ")
        self.usuarios.append(usuario)
        self.senhas.append(senha)
        with open('usuarios.txt', 'a') as arquivo_usuarios:
            arquivo_usuarios.write(usuario + ';' + senha)
            arquivo_usuarios.write('\n')

    def fazer_login(self):
        usuario_entrar = input("Digite o nome do usuário: ")
        senha_entrar = input("Digite a senha do usuário: ")
        with open('usuarios.txt', 'r') as senhas_usuario:
            for linha in senhas_usuario:
                usuario_senha = linha.split(';')
                usuario_senha[1] = usuario_senha[1].replace("\n", '')
                if usuario_entrar == usuario_senha[0] and senha_entrar == usuario_senha[1]:
                    self.logado = True
                    break

        if self.logado:
            print('Login realizado com sucesso')
        else:
            print('Usuário ou senha inválidos, tente novamente')


def menu():
    sistema = SistemaLogin()

    while True:
        menu = input("Digite '1' para cadastrar um usuário ou '2' para fazer login: ")

        if menu == '1':
            sistema.cadastrar_usuario()
        elif menu == '2':
            sistema.fazer_login()
            if sistema.logado:
                break
        else:
            print("Opção inválida. Tente novamente.")


menu()
