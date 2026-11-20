# Exibe mensagem de boas-vindas
print("Bem-vindo(a) ao Sistema de Maria Eduarda Gonçalves!")

# Obtém a entrada do usuário para o valor base e a idade do cliente
valor_base = float(input("Informe o valor base do plano: R$ "))
idade = int(input("Informe a idade do cliente: "))

# Valida a idade e calcula a mensalidade com base nas faixas etárias
if idade < 0:
    print("Idade inválida.")
else:
    if idade < 19:
        valor_mensal = valor_base
    elif idade < 29:
        valor_mensal = valor_base * 1.5
    elif idade < 39:
        valor_mensal = valor_base * 2.25
    elif idade < 49:
        valor_mensal = valor_base * 2.4
    elif idade < 59:
        valor_mensal = valor_base * 3.5
    else:
        valor_mensal = valor_base * 6

    # Exibe o valor mensal final calculado
    print(f"O valor mensal do plano é: R$ {valor_mensal:.2f}")
