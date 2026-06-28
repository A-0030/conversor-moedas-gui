# 💱 Conversor de Moedas GUI

Conversor de moedas com interface gráfica em **Python + Tkinter**, com botão de inversão rápida e tratamento de erros de entrada.

## ✨ Funcionalidades

- Conversão entre USD, EUR, BRL, GBP e AOA (Kwanza Angolano)
- Botão "Inverter" para trocar rapidamente moeda de origem/destino
- Validação de valores digitados (aceita `,` ou `.` como separador decimal)
- Interface escura e responsiva

## ⚠️ Nota importante

As taxas de câmbio neste projeto são **valores fixos de exemplo**, definidos no dicionário `TAXAS` em `app.py`. Para uso em produção, recomenda-se integrar com uma API de cotações em tempo real (ex.: [AwesomeAPI](https://docs.awesomeapi.com.br/) ou [exchangerate.host](https://exchangerate.host/)).

## 🖥️ Pré-requisitos

- Python 3.8+
- Tkinter (incluso na instalação padrão do Python)

## ▶️ Como executar

```bash
python app.py
```

## 📁 Estrutura do projeto

```
conversor-moedas-gui/
├── app.py        # Lógica + interface gráfica
└── README.md
```

## 🛠️ Tecnologias

- Python 3
- Tkinter

## 📌 Possíveis melhorias futuras

- Integração com API de cotações em tempo real
- Histórico de conversões
- Mais moedas e gráfico de variação cambial

---

Projeto desenvolvido como parte de um portfólio de aplicações Python.
