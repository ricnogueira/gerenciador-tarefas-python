from custom.crud import *
import pprint
from custom.formatar_data import formatar_data

while True:

    print("ESCOLHA A OPÇÃO DESEJADA:")
    print("[1] Para adicionar tarefa")
    print("[2] Para editar uma tarefa")
    print("[3] Para listar as tarefas")
    print("[4] Para apagar uma tarefa")
    print("Outro opcão sairá do programa")
    opcao = input("Digite a opção: ")

    if opcao not in ["1", "2", "3", "4"]:
        # print(46 * '#')
        print(f'\nOPÇÃO "{opcao}" NÃO ENCONTRADA. TENTE NOVAMENTE COM UMA DAS OPÇÕES VÁLIDAS!\n')
        # print(46 * '#')
        break
    elif opcao == "1":
        CONTADOR += int(1)
        data_inicio = input("Digite a data inicial (DDmmAAAA): ")
        data_inicio = formatar_data(data_inicio)
        data_termino = input("Digite a data do término (DDmmAAAA): ")
        data_termino = formatar_data(data_termino)
        descricao = input("Digite a descrição da tarefa: ")
        prioridade = input("Digite a prioridade da tarefa (0, 1 ou 2): ")
        status = input("digite a status da tarefa (Iniciada, Pendente, Cancelada, Concluída): ")
        observacao = input("Digite uma observação: ")

        dados_tarefa = {
            "id": CONTADOR,
            "data_inicio": data_inicio,
            "data_termino": data_termino,
            "descricao": descricao,
            "prioridade": prioridade,
            "status": status,
            "observacao": observacao,
        }

        TAREFA = dados_tarefa
        salvar(TAREFA)

    elif opcao == "2":
        if not contar_tarefas():
            id = int(input("Digite o ID para editar: "))
            editar(id)
        else:
            print("\nNão há tarefas cadastradas!\n")

    elif opcao == "3":
        listar()

    elif opcao == "4":
        if not contar_tarefas():
            id = int(input("Digite o ID da tarefa a ser apagada: "))
            deletar(id)
        else:
            print("\nNão há tarefas cadastradas!\n")
