import pyodbc
import datetime

#   ALTERAR CAMINHO DO ACCESS ------------------------ DESENVOLVER CAMINHO AUTOMATICO---------------------
connection_string = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\higor\OneDrive\Área de Trabalho\Projeto\material_back_end\DataBase_Cadastro.accdb;"


def executar_consulta(nome_consulta):
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        cursor.execute(f"{{CALL {nome_consulta}}}")
        conn.commit()

        print(f"Consulta '{nome_consulta}' executada com sucesso.")
    except pyodbc.Error as e:
        print(f"Erro ao executar a consulta '{nome_consulta}':", e)
    finally:
        cursor.close()
        conn.close()


def inserir_dados():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        nome = input("\nNome: ")
        sobrenome = input("Sobrenome: ")
        idade = input("Idade: ")
        cpf = input("CPF: ")
        Email= input("Email: ")
        
        data_cadastro = datetime.datetime.now().strftime("%Y-%m-%d")

        sql = """
        INSERT INTO [Cliente Cadastrados] ( CPF,Nome, Sobrenome, Idade, Email, [Data de Cadastro] )
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (cpf,nome,sobrenome,idade,Email,data_cadastro ))
        conn.commit()
        print("\nDados inseridos com sucesso!")
    except Exception as e:
        print("Erro ao inserir os dados:", e)
    finally:
        cursor.close()
        conn.close()

def inserir_MaquinasCadastradas():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        nomedamaquina = input("\nNome da maquina: ")
        preço = input("preço: ")
    
        data_cadastro = datetime.datetime.now().strftime("%Y-%m-%d")

        sql = """
        INSERT INTO [Todas as Maquinas] ( [Nome da maquina], preço)
        VALUES (?, ?)
        """
        cursor.execute(sql, (nomedamaquina,preço ))
        conn.commit()
        print("\nDados inseridos com sucesso!")
    except Exception as e:
        print("Erro ao inserir os dados:", e)
    finally:
        cursor.close()
        conn.close()
        

def cadastrar_login():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        email = input("Digite seu email para cadastro: ")
        senha = input("Digite sua senha para cadastro: ")
    
        #Checa se o e-mail já foi cadastrado
        cursor.execute("SELECT * FROM [Tabela Login] WHERE email = ?", email)
        if cursor.fetchone() is not None:
            print("Email já registrado!")
            return
        cursor.execute("INSERT INTO [Tabela Login] (Email, Senha) VALUES (?, ?)", email, senha)
        conn.commit()
        print("Cadastro realizado com sucesso!")
    except pyodbc.Error as e:
        print("Erro no cadastro:", e)
    finally:
        cursor.close()
        conn.close()

def realizar_login():
    while True:
        try:
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            cursor.execute("SELECT senha FROM [Tabela Login] WHERE Email = ?", email)
            row = cursor.fetchone()
            if row is not None:
                stored_senha = row[0]
                if senha == stored_senha:
                    print("Login realizado com sucesso!")
                    return True
                else:
                    print("Senha incorreta, tente novamente.")
            else:
                print("Email não encontrado, tente novamente.")
        except pyodbc.Error as e:
            print("Erro no login:", e)
        finally:
            cursor.close()
            conn.close()

def login_menu():
    while True:
        print("\n" + "=" * 50)
        print("LOGIN".center(50))
        print("=" * 50)
        opcao_login = input("\n[1] Cadastrar Login\n[2] Fazer Login\n[3] Sair\n\nEscolha uma opção: ")
        if opcao_login == "1":
            cadastrar_login()
        elif opcao_login == "2":
            if realizar_login():
                return True
        elif opcao_login == "3":
            return False
        else:
            print("Opção inválida, tente novamente.")

if not login_menu():
    print("Encerrando programa...")
    exit()

# Menu principal ----------------------------------------------------------------------------------
while True:
    print("\n" + "=" * 50)
    print("MENU PRINCIPAL".center(50))
    print("=" * 50)
    opcao = input(
        "\n[C]Cadrastrar Cliente\n[M]Cadastrar Maquina\n[S]air\n\nEscolha uma opção: ").upper()

    if opcao == "C":
        inserir_dados()
    elif opcao == "M":
        inserir_MaquinasCadastradas()
    elif opcao == "S":
        print("\nSaindo do sistema...")
        break
    else:
        print("\nOpção inválida! Tente novamente.")