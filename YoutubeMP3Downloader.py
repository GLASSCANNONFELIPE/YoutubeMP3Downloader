import os
import threading
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import yt_dlp


CARPETA_DESCARGAS = "descargas_mp3"
IMAGEN_FONDO = "fondo.png"


class ConsolaLogger:
    def __init__(self, consola):
        self.consola = consola

    def debug(self, msg):
        if msg.strip():
            self.escribir(msg)

    def warning(self, msg):
        self.escribir(f"ADVERTENCIA: {msg}")

    def error(self, msg):
        self.escribir(f"ERROR: {msg}")

    def escribir(self, msg):
        self.consola.after(0, lambda: self._insertar(msg))

    def _insertar(self, msg):
        self.consola.insert(tk.END, msg + "\n")
        self.consola.see(tk.END)


def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)

    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


def descargar_audio():
    url = entrada_url.get().strip()

    if not url:
        messagebox.showwarning("Falta URL", "Pega una URL de YouTube.")
        return

    boton_descargar.config(state=tk.DISABLED)
    consola.insert(tk.END, "\n> Iniciando descarga...\n")
    consola.see(tk.END)

    hilo = threading.Thread(target=proceso_descarga, args=(url,), daemon=True)
    hilo.start()


def proceso_descarga(url):
    os.makedirs(CARPETA_DESCARGAS, exist_ok=True)

    logger = ConsolaLogger(consola)

    opciones = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(CARPETA_DESCARGAS, "%(title)s.%(ext)s"),
        "logger": logger,
        "progress_hooks": [mostrar_progreso],
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])

        consola.after(0, lambda: consola.insert(tk.END, f"\n> Listo. Archivo guardado en: {CARPETA_DESCARGAS}\n"))
        consola.after(0, lambda: messagebox.showinfo("Descarga completa", "El audio se descargó correctamente."))

    except Exception as e:
        consola.after(0, lambda: consola.insert(tk.END, f"\n> ERROR: {e}\n"))
        consola.after(0, lambda: messagebox.showerror("Error", str(e)))

    finally:
        consola.after(0, lambda: boton_descargar.config(state=tk.NORMAL))


def mostrar_progreso(d):
    if d["status"] == "downloading":
        porcentaje = d.get("_percent_str", "").strip()
        velocidad = d.get("_speed_str", "").strip()
        eta = d.get("_eta_str", "").strip()

        texto = f"> Descargando... {porcentaje} | Velocidad: {velocidad} | ETA: {eta}"
        consola.after(0, lambda: escribir_linea_progreso(texto))

    elif d["status"] == "finished":
        consola.after(0, lambda: consola.insert(tk.END, "\n> Descarga terminada. Convirtiendo a MP3...\n"))


def escribir_linea_progreso(texto):
    consola.insert(tk.END, texto + "\n")
    consola.see(tk.END)


def cargar_fondo():
    global imagen_fondo_tk

    imagen = Image.open(IMAGEN_FONDO)
    imagen_fondo_tk = ImageTk.PhotoImage(imagen)

    fondo_label.config(image=imagen_fondo_tk)



ventana = tk.Tk()
ventana.title("DESCARGADOR YT to MP3")
ventana.iconbitmap("icono.ico")
centrar_ventana(ventana, 720, 420)

fondo_label = tk.Label(ventana)
fondo_label.place(x=0, y=0)
cargar_fondo()

espacio_titulo = tk.Label(
    ventana,
    text="",
    bg="#101010",
    height=1
)
espacio_titulo.pack()


entrada_url = tk.Entry(
    ventana,
    width=80,
    bg="#181818",
    fg="#ffffff",
    insertbackground="#ffffff",
    font=("Consolas", 11)
)
entrada_url.pack(pady=(57, 8))


boton_descargar = tk.Button(
    ventana,
    text="DESCARGAR MP3",
    command=descargar_audio,
    bg="#00aa66",
    fg="#ffffff",
    activebackground="#008855",
    activeforeground="#ffffff",
    font=("Consolas", 11, "bold"),
    relief=tk.FLAT,
    padx=12,
    pady=8
)
boton_descargar.pack(pady=8)

consola = tk.Text(
    ventana,
    bg="#000000",
    fg="#00ff88",
    insertbackground="#00ff88",
    font=("Consolas", 10),
    height=14,
    width=86,
    relief=tk.FLAT
)
consola.pack(pady=10)

consola.insert(tk.END, "> Consola lista amigo supremo.\n")
consola.insert(tk.END, f"> Los MP3 descargados se guardarán en la carpeta: {CARPETA_DESCARGAS}\n")

ventana.mainloop()
