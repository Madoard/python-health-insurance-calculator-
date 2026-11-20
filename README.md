<div align="center">

  <p>─────────────────────── ✦ ───────────────────────</p>

  <h1>˚₊‧꒰ა ✦ Calculadora de Plano de Saúde em Python ✦ ໒꒱‧₊˚</h1>

  <p>
    <i>Calcula a mensalidade de um plano de saúde no terminal aplicando multiplicadores escalonados por faixa etária.</i>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-FFB7C5?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/L%C3%B3gica-Regras%20Condicionais-E6E6FA?style=for-the-badge&logoColor=555555" alt="Regras Condicionais" />
    <img src="https://img.shields.io/badge/Console-Script%20CLI-FFD1DC?style=for-the-badge&logoColor=white" alt="Script CLI" />
  </p>

</div>

<br/>

<p align="center">─────────────────────── · ───────────────────────</p>

### ✦ Resumo

Este projeto automatiza o cálculo de mensalidades de planos de saúde a partir de um valor base e da idade do beneficiário, aplicando reajustes escalonados por faixa etária diretamente no terminal.

### ✦ Tecnologias

- **Python 3.x:** Linguagem principal para a lógica e interação via linha de comando (sem dependências externas).

### ✦ Regras

O multiplicador da mensalidade varia conforme a idade informada:

| Faixa Etária | Multiplicador |
| :--- | :---: |
| `0` a `18` anos | `1.0x` *(Valor base)* |
| `19` a `28` anos | `1.5x` |
| `29` a `38` anos | `2.25x` |
| `39` a `48` anos | `2.4x` |
| `49` a `58` anos | `3.5x` |
| `59` anos ou mais | `6.0x` |

<p align="center">─────────────────────── · ───────────────────────</p>

### ✦ Como Executar

1. **Pré-requisitos:** Tenha o **Python 3.x** instalado na máquina.
2. **Clone o repositório:**
   ```bash
   git clone https://github.com/Madoard/python-health-insurance-calculator-.git
   cd python-health-insurance-calculator-
   ```
3. **Execute o script (`calculadora.py`):**
   ```bash
   python calculadora.py
   ```

### ✦ Exemplo de Uso

```text
Informe o valor base do plano: R$ 200
Informe a idade do cliente: 25
O valor mensal do plano é: R$ 300.00
```

<p align="center">─────────────────────── · ───────────────────────</p>

### ✦ Como Foi Construído

O código completo está em [`calculadora.py`](./calculadora.py). Abaixo está a lógica principal e como cada parte funciona:

```python
valor_base = float(input("Informe o valor base do plano: R$ "))
idade = int(input("Informe a idade do cliente: "))

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
```

- **Entradas e conversão de tipos:** Recebe o valor base e a idade pelo terminal com `input()` e converte para `float` e `int`.
- **Condicionais encadeadas (`if / elif / else`):** Valida se a idade não é negativa e aplica o multiplicador correspondente à faixa etária.
- **Formatação de saída:** Usa `f-strings` com `:.2f` para mostrar o valor final formatado com duas casas decimais.

<br/>

<div align="center">
  <p>°•. ✦ .•° ────── ꒰ ✦ ꒱ ────── °•. ✦ .•°</p>
  <p><i>Feito por <b>Eduarda Gonçalves</b></i></p>
</div>
