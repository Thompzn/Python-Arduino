import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import serial
import datetime

arduino = None
evento_em_andamento = False
dados_evento = []
hora_inicio_real = ""
logs_armazenados = []
sistema_ligado = False

def conectar_arduino():
    try:
        return serial.Serial('COM3', 9600, timeout=1)
    except:
        atualizar_tela("Erro ao conectar com o Arduino.")
        return None

def atualizar_tela(texto):
    texto_log.insert(tk.END, texto + "\n")
    texto_log.yview(tk.END)

def salvar_log_em_arquivo():
    if not logs_armazenados:
        return
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text Files", "*.txt")],
                                                   title="Salvar log como")
    if caminho_arquivo:
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write("\n\n".join(logs_armazenados))
        atualizar_tela("Log salvo com sucesso.")

def limpar():
    texto_log.delete(1.0, tk.END)

def iniciar():
    global arduino, sistema_ligado
    if not sistema_ligado:
        arduino = conectar_arduino()
        if arduino:
            sistema_ligado = True
            atualizar_tela("Conectado ao Arduino. Sistema ligado.")
            botao_iniciar.config(state=tk.DISABLED)  
            botao_desligar.config(state=tk.NORMAL)
            leitura_arduino_tick()
        else:
            atualizar_tela("Erro ao conectar com o Arduino.")
    else:
        atualizar_tela("Sistema já está ligado.")

def desligar():
    global sistema_ligado
    if sistema_ligado:
        sistema_ligado = False
        atualizar_tela("Sistema desligado. Clique em 'Iniciar Atualização' para ligar novamente.")
        botao_desligar.config(state=tk.DISABLED)  
        botao_iniciar.config(state=tk.NORMAL)
    else:
        atualizar_tela("Sistema já está desligado.")

def leitura_arduino_tick():
    global evento_em_andamento, dados_evento, hora_inicio_real

    if arduino and arduino.in_waiting > 0:
        try:
            linha = arduino.readline().decode('utf-8').strip()

            if linha == "INICIO":
                evento_em_andamento = True
                dados_evento = []
                hora_inicio_real = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            elif linha == "FIM" and evento_em_andamento:
                hora_fim_real = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if len(dados_evento) >= 3:
                    tempo_inicio = int(dados_evento[0])
                    tempo_fim = int(dados_evento[1])
                    distancias = dados_evento[2]
                    hora_inicio_real =(datetime.datetime.now()-datetime.timedelta(0, (tempo_fim-tempo_inicio)/1000)).strftime("%Y-%m-%d %H:%M:%S")

                    log = f"Data: {hora_inicio_real.split()[0]}\n"
                    log += f"Hora inicial: {hora_inicio_real.split()[1]}\n"
                    log += f"Hora término: {hora_fim_real.split()[1]}\n"
                    log += f"Distâncias: {distancias}\n"

                    logs_armazenados.append(log)
                    atualizar_tela(log)

                evento_em_andamento = False

            elif evento_em_andamento:
                dados_evento.append(linha)

        except Exception as e:
            print(f"Erro na leitura serial: {e}")

    if sistema_ligado:
        janela.after(100, leitura_arduino_tick)

janela = tk.Tk()
janela.title("Logs do Sensor de Distância")

texto_log = scrolledtext.ScrolledText(janela, width=60, height=20)
texto_log.pack(padx=10, pady=10)

botao_iniciar = tk.Button(janela, text="Iniciar Atualização", command=iniciar)
botao_iniciar.pack(pady=5)

botao_desligar = tk.Button(janela, text="Desligar Sistema", command=desligar, state=tk.DISABLED)
botao_desligar.pack(pady=5)

botao_salvar = tk.Button(janela, text="Salvar Log em Arquivo", command=salvar_log_em_arquivo)
botao_salvar.pack(pady=5)

botao_limpar = tk.Button(janela, text="Limpar Histórico", command=limpar)
botao_limpar.pack(pady=5)

janela.mainloop()