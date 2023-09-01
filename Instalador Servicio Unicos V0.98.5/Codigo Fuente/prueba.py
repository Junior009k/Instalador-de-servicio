import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
root = tk.Tk()

# Crear función para mostrar popup con un label
def show_popup():
    # Crear una ventana Toplevel
    popup = tk.Toplevel(root)
    popup.title("Título de la ventana emergente")

    # Crear un label
    label = tk.Label(popup, text="Este es el contenido del label")

    # Añadir el label a la ventana
    label.pack(pady=10)

    # Crear un botón para cerrar la ventana
    button = tk.Button(popup, text="Cerrar", command=popup.destroy)
    button.pack()

# Crear botón para mostrar popup
button = tk.Button(root, text="Mostrar popup", command=show_popup)
button.pack(pady=10)

# Ejecutar la ventana principal
root.mainloop()
 