<div align="center">

  <p>｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ──────────── ꒰ 🩺 ꒱ ──────────── ⋆｡ﾟ☾ ﾟ｡⋆｡☁︎｡ﾟ</p>

  <h1>˚₊‧꒰ა 🫧 Python Health Insurance Calculator 🫧 ໒꒱‧₊˚</h1>

  <p>
    <i>✧･ﾟ: *✧･ﾟ:* Command-line Python application that computes health insurance monthly fees by applying tiered rate multipliers across age brackets *:･ﾟ✧*:･ﾟ✧</i>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-FFB7C5?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Logic-Conditional%20Rules-E6E6FA?style=for-the-badge&logoColor=555555" alt="Conditional Logic" />
    <img src="https://img.shields.io/badge/Console-CLI%20Script-FFD1DC?style=for-the-badge&logoColor=white" alt="CLI Script" />
  </p>

</div>

<br/>

<p align="center">‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾. ─────────────────────── ‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾.</p>

### ╰┈➤ ꒰ 🩹 ꒱ Business Rules

The monthly fee multiplier is determined dynamically according to the client's age bracket:

| 🪷 Age Bracket | 💊 Rate Multiplier |
| :--- | :---: |
| `0` to `18` years | `1.0x` *(Base rate)* |
| `19` to `28` years | `1.5x` |
| `29` to `38` years | `2.25x` |
| `39` to `48` years | `2.4x` |
| `49` to `58` years | `3.5x` |
| `59` years or older | `6.0x` |

<p align="center">‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾. ─────────────────────── ‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾.</p>

### ╰┈➤ ꒰ 🤍 ꒱ How It Was Built

* **₊˚🫧 Input Handling & Type Casting:** Captured user base rates and age inputs via CLI (`input`) and parsed them into numeric types (`float` and `int`).
* **₊˚🩺 Tiered Conditional Logic:** Implemented chained `if / elif / else` decision branches to map each age interval to its respective multiplier.
* **₊˚🫧 Formatted Output:** Used Python `f-strings` to display the calculated monthly fee cleanly in the terminal.

<br/>

<div align="center">
  <p>°•. 🫧 .•° ────── ꒰ 💗 ꒱ ────── °•. 🫧 .•°</p>
  <p><i>made with 💗 by <b>Maria Eduarda Gonçalves</b></i></p>
</div>
