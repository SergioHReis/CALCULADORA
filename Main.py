import tkinter as tk

# Funções para as operações matemáticas
def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
        historico_lista.insert(0, f"{expressao} = {resultado}")
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Função para adicionar um caractere à entrada
def adicionar_caractere(caractere):
    entrada.insert(tk.END, caractere)

# Função para limpar a entrada
def limpar():
    entrada.delete(0, tk.END)

# Função para somar à memória
def adicionar_memoria():
    global memoria
    try:
        valor = float(entrada.get())
        memoria += valor
    except ValueError:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")
        
# Função para subtrair da memória
def subtrair_memoria():
    global memoria
    try:
        valor = float(entrada.get())
        memoria -= valor
    except ValueError:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Função para exibir o valor da memória no visor
def mostrar_memoria():
    entrada.delete(0, tk.END)
    entrada.insert(0, str(memoria))

# Configurar a janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("500x600")

# Criar a entrada de texto
entrada = tk.Entry(janela, font=("Arial", 24))
entrada.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Criar um frame para os botões
frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

# Configurar o layout da grade para o frame de botões
for i in range(6):
    frame_botoes.grid_rowconfigure(i, weight=1)
    frame_botoes.grid_columnconfigure(i, weight=1)

# Adicionar os botões numéricos e de operações
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

row, col = 1, 0
for caractere in botoes:
    tk.Button(frame_botoes, text=caractere, command=lambda c=caractere: adicionar_caractere(c), font=("Arial", 20)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Adicionar os botões de memória
tk.Button(frame_botoes, text="M+", command=adicionar_memoria, font=("Arial", 20)).grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
tk.Button(frame_botoes, text="M-", command=subtrair_memoria, font=("Arial", 20)).grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
tk.Button(frame_botoes, text="MR", command=mostrar_memoria, font=("Arial", 20)).grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

# Adicionar o botão de igual
igual_button = tk.Button(frame_botoes, text="=", command=calcular, font=("Arial", 20))
igual_button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

# Adicionar o botão de limpar
limpar_button = tk.Button(frame_botoes, text="C", command=limpar, font=("Arial", 20))
limpar_button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

# Configurar o rótulo de resultado
resultado_label = tk.Label(janela, text="", font=("Arial", 24))
resultado_label.grid(row=2, column=0, columnspan=5)

# Histórico de cálculos
historico_label = tk.Label(janela, text="Histórico de Cálculos", font=("Arial", 16))
historico_label.grid(row=3, column=0, columnspan=5)
historico_lista = tk.Listbox(janela, font=("Arial", 14), selectbackground="yellow")
historico_lista.grid(row=4, column=0, columnspan=5)

# Assinatura
assinatura_label = tk.Label(janela, text="Feito por Sérgio Henrique Reis Sá", font=("Arial", 12))
assinatura_label.grid(row=6, column=0, columnspan=5)

# Variável de memória
memoria = 0

# Iniciar a interface gráfica
janela.mainloop()

