import pyodbc
import datetime

#   ALTERAR CAMINHO DO ACCESS ------------------------ DESENVOLVER CAMINHO AUTOMATICO---------------------
connection_string = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\higor\OneDrive\Área de Trabalho\Trabalho topicos integradores 2\DataBase_Cadastro.accdb;"
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


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

        # 1 = cliente 2 = funcionario
        categoria_input = input(
            "Digite 1 para 'Cliente' ou 2 para 'Funcionario': ")
        if categoria_input == "1":
            categoria = "Cliente"
        elif categoria_input == "2":
            categoria = "Funcionario"
        else:
            print("Opção inválida. Categoria definida como 'Cliente' por padrão.")
            categoria = "Cliente"

        # data atual para coluna data
        data_cadastro = datetime.datetime.now().strftime("%Y-%m-%d")

        # add dados para Cadastro_temp
        sql = """
        INSERT INTO Cadastro_temp (Nome, Sobrenome, idade, cpf, [data de cadastro], Categoria)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (nome, sobrenome, idade,
                       cpf, data_cadastro, categoria))
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
        "\n[I]nserir dados\n[C]onsultar registros\n[A]pagar Cadastro Temp e executar acréscimo\n[S]air\n\nEscolha uma opção: ").upper()

    if opcao == "I":
        inserir_dados()
    elif opcao == "C":
        print("\nExecutando consultas do tipo acréscimo...")

        for consulta in ("Filtra_Funcionario", "Filtra_Cliente"):
            executar_consulta(consulta)
    elif opcao == "A":  # tem q manter a ordem, 1° add cadastro hist 2° apagar cadastro!!!
        print("\nExecutando consulta de acréscimo: ADD_Cadastro_HIST...")
        executar_consulta("ADD_Cadastro_HIST")
        print("\nExecutando consulta de exclusão: Apagar_Cadastro_Temp...")
        executar_consulta("Apagar_Cadastro_Temp")
    elif opcao == "S":
        print("\nSaindo do sistema...")
        break
    else:
        print("\nOpção inválida! Tente novamente.")
