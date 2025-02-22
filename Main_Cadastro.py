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

        # input pelo terminal
        nome = input("\nNome: ")
        sobrenome = input("Sobrenome: ")
        idade = input("Idade: ")
        cpf = input("CPF: ")
        Email= input("Email: ")

        # data atual para coluna data
        data_cadastro = datetime.datetime.now().strftime("%Y-%m-%d")

        # add dados para Cadastro_temp
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

        # input pelo terminal
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
        

# Menu principal-------------------------------------------------------------------------------------------------------
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