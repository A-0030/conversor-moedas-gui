"""
Conversor de Moedas - Interface Gráfica
-----------------------------------------
Converte valores entre diferentes moedas usando taxas de câmbio fixas
(definidas localmente). Construído com Tkinter.

Nota: as taxas abaixo são valores de exemplo para fins de demonstração.
Para um cenário real, integre este projeto a uma API de cotações
(ex.: exchangerate.host, awesomeapi.com.br) substituindo TAXAS por uma
chamada HTTP.
"""

import tkinter as tk
from tkinter import ttk, font as tkfont

# --------------------------------------------------------------------------- #
# Lógica de negócio
# --------------------------------------------------------------------------- #

TAXAS = {
    "USD": 1.00,
    "EUR": 0.85,
    "BRL": 5.20,
    "GBP": 0.75,
    "AOA": 920.00,  # Kwanza angolano, incluído como exemplo de moeda local
}

NOMES_MOEDAS = {
    "USD": "Dólar Americano",
    "EUR": "Euro",
    "BRL": "Real Brasileiro",
    "GBP": "Libra Esterlina",
    "AOA": "Kwanza Angolano",
}


def converter(valor: float, moeda_origem: str, moeda_destino: str) -> float:
    """Converte um valor de uma moeda para outra usando TAXAS.

    Lança ValueError se alguma das moedas não existir na tabela de taxas.
    """
    if moeda_origem not in TAXAS or moeda_destino not in TAXAS:
        raise ValueError("Moeda inválida.")

    valor_em_usd = valor / TAXAS[moeda_origem]
    return valor_em_usd * TAXAS[moeda_destino]


# --------------------------------------------------------------------------- #
# Interface gráfica
# --------------------------------------------------------------------------- #


class ConversorApp(tk.Tk):
    COR_FUNDO = "#10131a"
    COR_CARTAO = "#1b2030"
    COR_TEXTO = "#f4f4f6"
    COR_DESTAQUE = "#34d1bf"

    def __init__(self):
        super().__init__()
        self.title("Conversor de Moedas")
        self.resizable(False, False)
        self.configure(bg=self.COR_FUNDO, padx=24, pady=24)

        self.fonte_titulo = tkfont.Font(family="Segoe UI", size=16, weight="bold")
        self.fonte_resultado = tkfont.Font(family="Segoe UI", size=20, weight="bold")

        self._aplicar_estilo_combobox()
        self._montar_interface()

    def _aplicar_estilo_combobox(self):
        estilo = ttk.Style(self)
        estilo.theme_use("default")
        estilo.configure(
            "TCombobox",
            fieldbackground=self.COR_CARTAO,
            background=self.COR_CARTAO,
            foreground=self.COR_TEXTO,
        )

    def _montar_interface(self):
        titulo = tk.Label(
            self,
            text="💱 Conversor de Moedas",
            font=self.fonte_titulo,
            bg=self.COR_FUNDO,
            fg=self.COR_TEXTO,
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 16))

        # Valor
        tk.Label(self, text="Valor", bg=self.COR_FUNDO, fg=self.COR_TEXTO).grid(
            row=1, column=0, sticky="w"
        )
        self.entrada_valor = tk.Entry(self, font=("Segoe UI", 12), width=18, justify="right")
        self.entrada_valor.insert(0, "1.00")
        self.entrada_valor.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 12))

        # Moeda de origem
        tk.Label(self, text="De", bg=self.COR_FUNDO, fg=self.COR_TEXTO).grid(
            row=3, column=0, sticky="w"
        )
        self.combo_origem = ttk.Combobox(
            self, values=self._opcoes_moeda(), state="readonly", width=24
        )
        self.combo_origem.set(self._opcoes_moeda()[0])
        self.combo_origem.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(0, 12))

        # Botão inverter
        botao_inverter = tk.Button(
            self,
            text="⇅ Inverter",
            command=self._inverter_moedas,
            relief="flat",
            bg=self.COR_CARTAO,
            fg=self.COR_TEXTO,
        )
        botao_inverter.grid(row=5, column=0, columnspan=2, pady=(0, 12))

        # Moeda de destino
        tk.Label(self, text="Para", bg=self.COR_FUNDO, fg=self.COR_TEXTO).grid(
            row=6, column=0, sticky="w"
        )
        self.combo_destino = ttk.Combobox(
            self, values=self._opcoes_moeda(), state="readonly", width=24
        )
        self.combo_destino.set(self._opcoes_moeda()[1])
        self.combo_destino.grid(row=7, column=0, columnspan=2, sticky="ew", pady=(0, 16))

        # Botão converter
        botao_converter = tk.Button(
            self,
            text="Converter",
            command=self._ao_converter,
            relief="flat",
            bg=self.COR_DESTAQUE,
            fg="#0a0a0a",
            font=("Segoe UI", 11, "bold"),
        )
        botao_converter.grid(row=8, column=0, columnspan=2, sticky="ew", pady=(0, 16))

        # Resultado
        self.label_resultado = tk.Label(
            self,
            text="",
            font=self.fonte_resultado,
            bg=self.COR_FUNDO,
            fg=self.COR_DESTAQUE,
        )
        self.label_resultado.grid(row=9, column=0, columnspan=2)

        self.entrada_valor.bind("<Return>", lambda e: self._ao_converter())

    @staticmethod
    def _opcoes_moeda():
        return [f"{codigo} - {nome}" for codigo, nome in NOMES_MOEDAS.items()]

    @staticmethod
    def _extrair_codigo(opcao: str) -> str:
        return opcao.split(" - ")[0]

    def _inverter_moedas(self):
        origem, destino = self.combo_origem.get(), self.combo_destino.get()
        self.combo_origem.set(destino)
        self.combo_destino.set(origem)

    def _ao_converter(self):
        texto_valor = self.entrada_valor.get().replace(",", ".").strip()

        try:
            valor = float(texto_valor)
        except ValueError:
            self.label_resultado.config(text="⚠️ Valor inválido", fg="#ff6b6b")
            return

        codigo_origem = self._extrair_codigo(self.combo_origem.get())
        codigo_destino = self._extrair_codigo(self.combo_destino.get())

        try:
            resultado = converter(valor, codigo_origem, codigo_destino)
        except ValueError as erro:
            self.label_resultado.config(text=f"⚠️ {erro}", fg="#ff6b6b")
            return

        self.label_resultado.config(
            text=f"{valor:,.2f} {codigo_origem} = {resultado:,.2f} {codigo_destino}",
            fg=self.COR_DESTAQUE,
        )


if __name__ == "__main__":
    app = ConversorApp()
    app.mainloop()
