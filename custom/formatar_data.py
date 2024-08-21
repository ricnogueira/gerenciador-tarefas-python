def formatar_data(data_str):
    # Verifica se a string tem exatamente 8 caracteres
    if len(data_str) != 8:
        while True:
            print("A data deve ter exatamente 8 caracteres no formato 'ddmmyyyy'.")
            data_str = input("Digite a data (DDmmAAAA): ")
            if len(data_str) == 8:
                break
    
    # Divide a string nos componentes dia, mês e ano
    dia = data_str[:2]
    mes = data_str[2:4]
    ano = data_str[4:]

    # Formata a data no formato desejado
    data_formatada = f"{dia}/{mes}/{ano}"
    return data_formatada

