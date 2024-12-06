import tkinter as tk
from tkinter import messagebox
from conversor import converter_moeda 

def exibir_erro(mensagem):
    messagebox.showerror("Erro", mensagem)

def realizar_conversao():
    try:
        moeda_origem = entrada_moeda_origem.get()
        moeda_destino = entrada_moeda_destino.get()
        valor = float(entrada_valor.get())

        if valor <= 0:
            exibir_erro("O valor deve ser maior que zero.")
            return

        resultado = converter_moeda(moeda_origem, moeda_destino, valor)

        label_resultado.config(text=f"Resultado: {resultado:.2f} {moeda_destino.upper()}")
    except ValueError as ve:
        exibir_erro(f"Erro na conversão: {ve}")
    except Exception as e:
        exibir_erro(f"Erro inesperado: {e}")

janela = tk.Tk()
janela.title("Conversor de Moedas")

janela.geometry("500x500")
janela.config(bg="#f0f0f0")

titulo = tk.Label(janela, text="Conversor de Moedas", font=("Arial", 20, "bold"), bg="#f0f0f0")
titulo.pack(pady=20)

label_moeda_origem = tk.Label(janela, text="Moeda de origem (ex: USD, EUR, BRL):", font=("Arial", 12), bg="#f0f0f0")
label_moeda_origem.pack(pady=5)
entrada_moeda_origem = tk.Entry(janela, font=("Arial", 12), width=20, bg="#e0e0e0")
entrada_moeda_origem.pack(pady=5)

label_moeda_destino = tk.Label(janela, text="Moeda de destino (ex: USD, EUR, BRL):", font=("Arial", 12), bg="#f0f0f0")
label_moeda_destino.pack(pady=5)
entrada_moeda_destino = tk.Entry(janela, font=("Arial", 12), width=20, bg="#e0e0e0")
entrada_moeda_destino.pack(pady=5)

label_valor = tk.Label(janela, text="Valor a ser convertido:", font=("Arial", 12), bg="#f0f0f0")
label_valor.pack(pady=5)
entrada_valor = tk.Entry(janela, font=("Arial", 12), width=20, bg="#e0e0e0")
entrada_valor.pack(pady=5)

botao_converter = tk.Button(janela, text="Converter", font=("Arial", 14), bg="#4CAF50", fg="white", command=realizar_conversao)
botao_converter.pack(pady=20)

label_resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 14), bg="#f0f0f0")
label_resultado.pack(pady=10)

janela.mainloop()
