import pprint

TAREFA = []
CONTADOR = 0


def listar():
    # print(type(TAREFA))
    if not TAREFA:
        return print("\nNão há tarefas cadastradas!\n")
        # return None

    else:
        for row in TAREFA:
            print(row)
            # print(
            #    f"ID: {row['id']}  | DataInicio: | DataFim: | Descrição:  | Prioridade:  | Status:  | Obs: "
            # )


def salvar(tarefa):
    try:
        TAREFA.append(tarefa)
        print("\nTarefa salva com sucesso!\n")
    except Exception as e:
        CONTADOR -= 1
        print(e)


def editar(id):
    listar()
    for i, row in enumerate(TAREFA):
        if row["id"] == id:
            print(f"Editando a tarefa {id} com a seguinte descrição: {row['descricao']}.")
            data_inicio = input("Digite a data inicial: ")
            data_termino = input("Digite a data do término: ")
            descricao = input("Digite a descrição da tarefa: ")
            prioridade = input("Digite a prioridade da tarefa (1, 2 ou 3): ")
            status = input(
                "digite a status da tarefa (Iniciada, Pendente, Cancelada, Concluída): "
            )
            observacao = input("Digite uma observação: ")
            TAREFA[i] = {
                "id": id,
                "data_inicio": data_inicio,
                "data_termino": data_termino,
                "descricao": descricao,
                "prioridade": prioridade,
                "status": status,
                "observacao": observacao,
            }
            print("Tarefa editada com sucesso!")
            #return
        else:
            print("Não há tarefas cadastradas com esse ID!")


def deletar(id):
    # ele pega o iterável e a sua posição dentro dela
    for i, row in enumerate(TAREFA):
        if row["id"] == id:
            try:
                del TAREFA[i]
                id_deletado = row["id"]
                descricao = row["descricao"]
                # print(f"deletado TAREFA {TAREFA[i+1]}")
                print(
                    f"Tarefa com ID {id_deletado} ({descricao}) deletada com sucesso!"
                )
            except Exception as e:
                print(e)
                break


def contar_tarefas():
    if len(TAREFA) == 0:
        return True

