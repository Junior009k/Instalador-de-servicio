import tkinter as tk

# Función para mostrar el primer frame
def show_frame1():
    frame1.pack(fill=tk.BOTH, expand=True)
    frame2.pack_forget()

# Función para mostrar el segundo frame
def show_frame2():
    frame1.pack_forget()
    frame2.pack(fill=tk.BOTH, expand=True)

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz con dos pantallas")
root.geometry("400x300")

# Crear los dos frames
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

# Agregar widgets al primer frame
label1 = tk.Label(frame1, text="Pantalla 1", font=("Arial", 24))
button1 = tk.Button(frame1, text="Cambiar a pantalla 2", command=show_frame2, font=("Arial", 18))
label1.pack(pady=50)
button1.pack(pady=10)

# Agregar widgets al segundo frame
label2 = tk.Label(frame2, text="Pantalla 2", font=("Arial", 24))
button2 = tk.Button(frame2, text="Cambiar a pantalla 1", command=show_frame1, font=("Arial", 18))
label2.pack(pady=50)
button2.pack(pady=10)

# Mostrar el primer frame al inicio
show_frame1()

root.mainloop()
