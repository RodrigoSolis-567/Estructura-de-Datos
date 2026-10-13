import tkinter as tk
from tkinter import messagebox

class PilaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador Gráfico de Pila (Stack)")
        self.root.geometry("500x600")
        self.root.config(bg="#f0f2f5")
        ancho, alto = 500, 600
        x = (self.root.winfo_screenwidth() - ancho) // 2
        y = (self.root.winfo_screenheight() - alto) // 2
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")

        #tamaño de pila
        self.pila = []
        self.CAPACIDAD_MAX = 8

        # Título
        titulo = tk.Label(root, text="Pila \n Último en entrar, primero en salir", font=("Arial", 16, "bold"), bg="#f0f2f5", fg="#333")
        titulo.pack(pady=15)
        titulo = tk.Label(root, text="inserte un valor en el recuadro", font=("Arial", 12), bg="#f0f2f5", fg="#333")
        titulo.pack(pady=15)

        #Entrada y Botones
        control_frame = tk.Frame(root, bg="#f0f2f5")
        control_frame.pack(pady=10)

        self.entry_valor = tk.Entry(control_frame, font=("Arial", 14), width=12)
        self.entry_valor.grid(row=0, column=0, padx=5)
        self.entry_valor.bind("<Return>", lambda event: self.push())

        btn_push = tk.Button(control_frame, text="colocar en la pila ", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", width=15, command=self.push)
        btn_push.grid(row=0, column=1, padx=5)

        btn_pop = tk.Button(control_frame, text="Desapilar", font=("Arial", 11, "bold"), bg="#f44336", fg="white", width=12, command=self.pop)
        btn_pop.grid(row=1, column=0, padx=5, pady=8)

        btn_peek = tk.Button(control_frame, text="Consultar ultimo valor", font=("Arial", 11, "bold"), bg="#ff9800", fg="white", width=17, command=self.peek)
        btn_peek.grid(row=1, column=1, padx=5, pady=8)

        # pila gráfica
        self.canvas_frame = tk.Frame(root, bg="white", bd=2, relief="solid")
        self.canvas_frame.pack(pady=10)

        self.canvas = tk.Canvas(self.canvas_frame, width=250, height=350, bg="white", highlightthickness=0)
        self.canvas.pack()

        # Estado
        self.lbl_estado = tk.Label(root, text="Pila vacía", font=("Arial", 11, "italic"), bg="#f0f2f5", fg="#666")
        self.lbl_estado.pack(pady=5)

        self.actualizar_dibujo()

    def push(self):
        valor = self.entry_valor.get().strip()
        if not valor:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un valor.")
            return
        
        if len(self.pila) >= self.CAPACIDAD_MAX:
            messagebox.showerror("Error", "¡La pila está llena ! No se pueden agregar más elementos.")
            return

        self.pila.append(valor)
        self.entry_valor.delete(0, tk.END)
        self.lbl_estado.config(text=f"Elemento '{valor}' agregado con Push.")
        self.actualizar_dibujo()

    def pop(self):
        if not self.pila:
            messagebox.showerror("Error", "¡La pila está vacía ! No hay elementos para desapilar.")
            return
        
        valor = self.pila.pop()
        self.lbl_estado.config(text=f"Elemento '{valor}' eliminado con Pop.")
        self.actualizar_dibujo()

    def peek(self):
        if not self.pila:
            messagebox.showinfo("Información", "La pila está vacía.")
        else:
            tope = self.pila[-1]
            messagebox.showinfo("Informacion",f"El elemento en el tope de la pila es: {tope}")

    def actualizar_dibujo(self):
        self.canvas.delete("all")
        
        # Coordenadas iniciales de la caja base de la pila
        x1, y1, x2, y2 = 50, 300, 200, 330
        ancho_caja = x2 - x1
        alto_caja = y2 - y1
        espacio = 5

        # Dibujar estructura base contenedora abierta por arriba
        self.canvas.create_line(40, 355, 40, 50, width=3, fill="#333")
        self.canvas.create_line(40, 355, 210, 355, width=3, fill="#333")
        self.canvas.create_line(210, 355, 210, 50, width=3, fill="#333")
        
        self.canvas.create_text(125, 25, text="TOPE DE LA PILA", font=("Arial", 10, "bold"), fill="#d32f2f")

        # Dibujar los elementos desde el fondo hasta el tope
        for i, elemento in enumerate(self.pila):
            actual_y2 = y2 - (i * (alto_caja + espacio))
            actual_y1 = actual_y2 - alto_caja

            # Elemento del tope
            color_relleno = "#4CAF50" if i == len(self.pila) - 1 else "#2196F3"

            # Dibujar rectángulo
            self.canvas.create_rectangle(x1, actual_y1, x2, actual_y2, fill=color_relleno, outline="black", width=2)

            # Dibujar texto dentro del bloque
            self.canvas.create_text((x1 + x2) / 2, (actual_y1 + actual_y2) / 2, text=str(elemento), font=("Arial", 12, "bold"), fill="white")

        if not self.pila:
            self.canvas.create_text(125, 180, text="[ Pila Vacía ]", font=("Arial", 11), fill="#999")

if __name__ == "__main__":
    root = tk.Tk()
    app = PilaApp(root)
    root.mainloop()