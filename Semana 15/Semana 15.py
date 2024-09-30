import tkinter as tk


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista de tareas
        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.entry_task = tk.Entry(root, width=50)
        self.entry_task.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

        # Botón para añadir tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=5, pady=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

        # Botón para marcar tarea como completada
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

        # Llenar la lista de tareas (para propósitos de demostración)
        self.tasks = ["Tarea 1", "Tarea 2", "Tarea 3"]
        self.update_task_list()

        # Evento de presionar Enter para añadir tarea
        self.entry_task.bind("<Return>", lambda event: self.add_task())

    def add_task(self):
        """Añade una nueva tarea a la lista."""
        new_task = self.entry_task.get()
        if new_task:
            self.tasks.append(new_task)
            self.update_task_list()
            self.entry_task.delete(0, tk.END)

    def complete_task(self):
        """Marca la tarea seleccionada como completada."""
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            task = self.tasks[index]
            # Modificar la tarea para mostrar que está completada (por ejemplo, añadiendo un prefijo)
            self.tasks[index] = f"[Completada] {task}"
            self.update_task_list()

    def delete_task(self):
        """Elimina la tarea seleccionada."""
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        """Actualiza la lista de tareas en la interfaz gráfica."""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Crear la ventana principal de la aplicación
root = tk.Tk()
app = TodoApp(root)
root.mainloop()