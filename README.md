<div align="center">

  <p>─────────────────────── ✦ ───────────────────────</p>

  <h1>˚₊‧꒰ა ✦ Calculadora de Plano de Saúde em Python ✦ ໒꒱‧₊˚</h1>

  <p>
    <i>Aplicação em Python via linha de comando que calcula a mensalidade de plano de saúde aplicando multiplicadores escalonados por faixas etárias.</i>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-FFB7C5?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/L%C3%B3gica-Regras%20Condicionais-E6E6FA?style=for-the-badge&logoColor=555555" alt="Regras Condicionais" />
    <img src="https://img.shields.io/badge/Console-Script%20CLI-FFD1DC?style=for-the-badge&logoColor=white" alt="Script CLI" />
  </p>

</div>

<br/>

<p align="center">─────────────────────── · ───────────────────────</p>

### ╰┈➤ ✦ Visão Geral & Regras de Negócio

#### Resumo
Este projeto automatiza o cálculo de mensalidades de planos de saúde a partir de um valor base e da idade do beneficiário, resolvendo a necessidade de aplicar reajustes escalonados por faixa etária de forma rápida e livre de erros manuais diretamente no terminal. O código-fonte completo está disponível em [`calculadora.py`](./calculadora.py).

#### Tecnologias Utilizadas
- **Python 3.x:** Linguagem principal utilizada para a lógica de negócio e interação via console (sem necessidade de bibliotecas externas).

#### Regras de Negócio
O multiplicador da mensalidade é definido dinamicamente de acordo com a faixa etária do cliente:

| Faixa Etária | Multiplicador |
| :--- | :---: |
| `0` a `18` anos | `1.0x` *(Valor base)* |
| `19` a `28` anos | `1.5x` |
| `29` a `38` anos | `2.25x` |
| `39` a `48` anos | `2.4x` |
| `49` a `58` anos | `3.5x` |
| `59` anos ou mais | `6.0x` |

<p align="center">─────────────────────── · ───────────────────────</p>

### ╰┈➤ ✦ Como Foi Construído

- **Tratamento de Entradas e Conversão de Tipos:** Captura do valor base e da idade via CLI (`input`) com conversão para tipos numéricos (`float` e `int`).
- **Lógica Condicional Escalonada:** Implementação de ramificações `if / elif / else` encadeadas para associar cada intervalo de idade ao seu multiplicador correspondente.
- **Saída Formatada:** Uso de `f-strings` do Python para exibir a mensalidade calculada de forma limpa no terminal.

```python
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

    print(f"O valor mensal do plano é: R$ {valor_mensal:.2f}")
