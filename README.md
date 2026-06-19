# 🎵 YouTube MP3 Downloader

Herramienta de escritorio con interfaz gráfica para descargar el audio de videos de YouTube y convertirlos a MP3 directamente, con consola de progreso en tiempo real.

---

## ✨ Funciones

- Descarga el audio de cualquier video de YouTube pegando su URL
- Convierte automáticamente a **MP3 a 192 kbps**
- Muestra progreso en tiempo real: porcentaje, velocidad y tiempo restante
- Consola integrada con log de todo el proceso
- Acceso directo a **Vocal Remover** para separar voces e instrumentales
- Ventana centrada y con fondo personalizable

---

## 📋 Requisitos

- Python 3.8 o superior
- [FFmpeg](https://ffmpeg.org/download.html) instalado y disponible en el PATH

### Dependencias Python

```bash
pip install yt-dlp pillow
```

---

## 🚀 Uso

1. Clona o descarga este repositorio
2. Asegúrate de tener FFmpeg instalado
3. Instala las dependencias
4. Ejecuta el script:

```bash
python YoutubeMP3Downloader.py
```

5. Pega la URL de YouTube en el campo de texto
6. Pulsa **DESCARGAR MP3**
7. El archivo quedará en la carpeta `descargas_mp3/`

---

## 📁 Estructura del proyecto

```
├── YoutubeMP3Downloader.py   # Script principal
├── fondo.png                 # Imagen de fondo de la ventana (opcional)
├── icono.ico                 # Ícono de la ventana (opcional)
└── descargas_mp3/            # Carpeta generada automáticamente con los MP3
```

> `fondo.png` e `icono.ico` son opcionales. Si no están presentes, el programa funciona igual.

---

## 🎙 Vocal Remover

El botón **VOCAL REMOVER** abre [vocalremover.org](https://vocalremover.org/) en tu navegador, una herramienta online gratuita para separar la voz de la música en cualquier MP3. Ideal para usar después de descargar el audio.

---

## ⚙️ Configuración

Las siguientes constantes al inicio del script se pueden modificar:

| Variable | Valor por defecto | Descripción |
|---|---|---|
| `CARPETA_DESCARGAS` | `descargas_mp3` | Carpeta donde se guardan los MP3 |
| `IMAGEN_FONDO` | `fondo.png` | Imagen de fondo de la ventana |

La calidad del MP3 se puede cambiar en la opción `preferredquality` dentro de `proceso_descarga` (por defecto: `192` kbps).

---

## 🛠 Tecnologías

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — descarga y extracción de audio
- [FFmpeg](https://ffmpeg.org/) — conversión a MP3
- [tkinter](https://docs.python.org/3/library/tkinter.html) — interfaz gráfica
- [Pillow](https://python-pillow.org/) — imagen de fondo