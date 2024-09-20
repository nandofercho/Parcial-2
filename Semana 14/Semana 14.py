import tkinter as tk
from tkinter import ttk
import tkinter
from tkcalendar import Calendar


class AgendaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Agenda Personal")

        # Crear el contenedor principal
        self.main_frame = ttk.Frame(self.master, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Crear el TreeView para mostrar los eventos
        self.tree = ttk.Treeview(self.main_frame, columns=('Date', 'Time', 'Description'), show='headings')
        self.tree.heading('Date', text='Date')
        self.tree.heading('Time', text='Time')
        self.tree.heading('Description', text='Description')
        self.tree.pack(pady=10)

        # Crear el contenedor para los campos de entrada
        self.input_frame = ttk.Frame(self.main_frame)
        self.input_frame.pack(pady=10, fill=tk.BOTH)

        # Etiquetas y campos de entrada
        ttk.Label(self.input_frame, text="Date:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.date_entry = tk.Entry(self.input_frame)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.input_frame, text="Time:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.time_entry = tk.Entry(self.input_frame)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.input_frame, text="Description:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.description_entry = tk.Entry(self.input_frame)
        self.description_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        # Botones
        self.add_button = ttk.Button(self.main_frame, text="Add Event", command=self.add_event)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = ttk.Button(self.main_frame, text="Delete Selected Event", command=self.delete_event)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.exit_button = ttk.Button(self.main_frame, text="Exit", command=self.master.quit)
        self.exit_button.pack(side=tk.LEFT, padx=5)

    def add_event(self):
        date = self.date_entry.get()
        time = self.time_entry.get()
        description = self.description_entry.get()
        if date and time and description:
            self.tree.insert('', 'end', values=(date, time, description))
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
        else:
            tkinter.messagebox.showerror("Error", "Please fill in all fields")

    def delete_event(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirmation = tkinter.messagebox.askyesno("Confirm", "Are you sure you want to delete this event?")
            if confirmation:
                self.tree.delete(selected_item)
        else:
            tkinter.messagebox.showerror("Error", "Please select an event to delete")


def main():
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
