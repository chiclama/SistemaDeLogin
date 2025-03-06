#criar um sistema de login e registro
#usuário, senha, email, telefone

class login:
     def __init__(self,usuario,senha,email,telefone):
        self.usuario = usuario
        self.senha = senha
        self.email = email
        self.telefone = telefone
     def opcoes(self):
        while True:
            print("-"*30)
            print("SEJA BEM VINDO A PLATAFORMA")
            print("-"*30)
            print("Seleciona a opção desejada")
            print("-"*30)
            print("lista das suas informações(list)")
            print("-"*30)
            print("Seu número de telefone (NT)")
            print("-"*30)
            print("Seu email (@)")
            print("-"*30)
            print("Sua senha (pass)")
            print("-"*30)
            print("seu usuário (user)")
            print("-"*30)
            print("Sair do programa(sair)")
            print("-"*30)
            querer = input("qual opção?")
            if querer in["NT", "nt", "Nt"]:
                print("-"*30)
                print(Conta.telefone)
                print("-"*30)
                print("Opção de voltar(VL)")
                print("-"*30)
                print("Opção de sair(sair)")
                otv = input("Qual opção? ")
                print("-"*30)
                print("-"*30)
                if otv == "VL":
                    pass
                else:
                    break
            if querer == "@":
                print("-"*30)
                print(Conta.email)
                print("-"*30)
                print("Opção de voltar(VL)")
                print("-"*30)
                print("Opção de sair(sair)")
                otv = input("Qual opção? ")
                print("-"*30)
                print("-"*30)
                if otv == "VL":
                    pass
                else:
                    break
            if querer in ["user", "User", "USER"]:
                print("-"*30)
                print(Conta.usuario)
                print("-"*30)
                print("Opção de voltar(VL)")
                print("-"*30)
                print("Opção de sair(sair)")
                otv = input("Qual opção? ")
                print("-"*30)
                print("-"*30)
                if otv == "VL":
                    pass
                else:
                    break
            if querer in ["PASS", "pass", "Pass"]:
                print("-"*30)
                print(Conta.senha)
                print("-"*30)
                print("Opção de voltar(VL)")
                print("-"*30)
                print("Opção de sair(sair)")
                otv = input("Qual opção? ")
                print("-"*30)
                print("-"*30)
                if otv == "VL":
                    pass
                else:
                    break
            if querer in ["LIST", "list", "List"]:
                print("-"*30)
                print(Conta.__dict__)
                print("-"*30)
                print("Opção de voltar(VL)")
                print("-"*30)
                print("Opção de sair(sair)")
                otv = input("Qual opção? ")
                print("-"*30)
                print("-"*30)
                if otv == "VL":
                    pass
                else:
                    break
            else:
                pass
            if querer == "sair":
                break
    
     def verificarLogin(self):
        user = input("Qual é o seu usuário? ")
        senha = input("Qual é a sua senha? ")
        if self.usuario == user and self.senha == senha:
            print(f"seja bem vindo {self.usuario}!!")
            Conta.opcoes()
        else:
            print("usuário ou senha incorreto")
            
resposta = input("Olá, seja bem vindo!. Você ja tem uma conta? ").casefold()
if resposta in ["não", "nao",]:
    user = input("fale seu nome: ")
    senha = input("crie uma senha: ")
    email = input("Qual é o seu email? ")
    telefone = input("Qual é o seu telefone? ")
else:
    pass
Conta = login(user,senha,email,telefone)

desejo = input("Deseja logar agora? ").casefold()
if desejo in ["sim"]:
    Conta.verificarLogin()
else:
    pass




    



    

       

     
    

    
    

