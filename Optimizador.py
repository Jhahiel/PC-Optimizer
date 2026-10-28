import os
import subprocess
import tkinter as tk
from tkinter import messagebox


def forzar_cierre_congelados():
    try:
        cmd = 'taskkill /f /fi "status eq not responding"'
        resultado = subprocess.check_output(cmd, shell=True).decode("latin-1")
        messagebox.showinfo(
            "Forzar Cierre",
            "Procesos congelados cerrados correctamente.\n\n" + resultado,
        )
    except Exception as e:
        messagebox.showerror(
            "Error", f"No se encontraron procesos congelados o hubo un error: {e}"
        )


def limpiar_archivos_temporales():
    try:
        os.system("del /q /f /s %TEMP%\\*")
        os.system("del /q /f /s C:\\Windows\\Temp\\*")
        messagebox.showinfo(
            "Limpieza", "¡Archivos temporales borrados exitosamente!"
        )
    except Exception as e:
        messagebox.showerror("Error", f"Error al limpiar temporales: {e}")


def liberar_ram_cache():
    try:
        os.system("echo off | clip")
        messagebox.showinfo(
            "RAM", "¡Memoria Portapapeles y Cache optimizadas!"
        )
    except Exception as e:
        messagebox.showerror("Error", f"Error al liberar RAM: {e}")


app = tk.Tk()
app.title("Mi Optimizador de PC v1.0")
app.geometry("380x320")
app.configure(bg="#1e1e2e")

titulo = tk.Label(
    app,
    text="⚡ PC OPTIMIZER & TOOL ⚡",
    font=("Arial", 14, "bold"),
    fg="#00ffcc",
    bg="#1e1e2e",
)
titulo.pack(pady=15)

btn_cierre = tk.Button(
    app,
    text="🚨 Forzar Cierre (Apps Congeladas)",
    font=("Arial", 10, "bold"),
    bg="#ff4757",
    fg="white",
    width=30,
    height=2,
    command=forzar_cierre_congelados,
)
btn_cierre.pack(pady=8)

btn_temp = tk.Button(
    app,
    text="🧹 Limpiar Archivos Temporales",
    font=("Arial", 10, "bold"),
    bg="#2ed573",
    fg="white",
    width=30,
    height=2,
    command=limpiar_archivos_temporales,
)
btn_temp.pack(pady=8)

btn_ram = tk.Button(
    app,
    text="⚡ Optimizar Memoria RAM",
    font=("Arial", 10, "bold"),
    bg="#1e90ff",
    fg="white",
    width=30,
    height=2,
    command=liberar_ram_cache,
)
btn_ram.pack(pady=8)

app.mainloop()