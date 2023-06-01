import tkinter as tk
from MemoryManager import MemoryManager
from PIL import Image, ImageTk

class MemoryManagerUI:
    def __init__(self):
        self.memory_manager = MemoryManager()

        self.window = tk.Tk()
        self.window.title("Memory Manager")
        self.window.configure(background='#1D7874')

        # Set the window size and center it on the screen
        window_width = 585
        window_height = 670
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        # Set custom styles for the widgets
        font_style = ('Arial', 10,"bold")
        font_style2 = ('Arial', 12)
        label_fg = '#000000'
        entry_bg = 'white'
        button_bg = '#F4C095'
        log_text_bg = 'white'


        self.title_label = tk.Label(self.window, text="Memory Management", font=("Arial", 20, "bold"), fg="white", bg="#1D7874")
        self.title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Create and configure the labels
        self.process_id_label = tk.Label(self.window, text="Process Id", bg=self.window.cget("background"),fg=label_fg ,font=font_style2)
        self.process_id_label.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        self.size_entry_label = tk.Label(self.window, text="Size of Process (KB)", bg=self.window.cget("background"), fg=label_fg,font=font_style2)
        self.size_entry_label.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        # Create and configure the entry fields
        self.process_id_entry = tk.Entry(self.window, bg=entry_bg, font=font_style)
        self.process_id_entry.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

        self.size_entry = tk.Entry(self.window, bg=entry_bg, font=font_style)
        self.size_entry.grid(row=5, column=2, padx=10, pady=10, sticky='nsew')

        # Create and configure the buttons
        button_style = ('Arial', 10, 'bold')

        self.allocate_button = tk.Button(self.window, text="Allocate", fg='white', bg=button_bg,
                                         command=self.allocate_memory, font=button_style)
        self.allocate_button.grid(row=6, column=2, padx=10, pady=10, sticky='nsew')

        self.release_button = tk.Button(self.window, text="Deallocate", fg='white', bg=button_bg,
                                        command=self.release_memory, font=button_style)
        self.release_button.grid(row=12, column=2, padx=10, pady=10, sticky='nsew')

        self.snapshot_button = tk.Button(self.window, text="Print Snapshot", fg='white', bg=button_bg,
                                         command=self.print_snapshot, font=button_style)
        self.snapshot_button.grid(row=6, column=1, padx=10, pady=10, sticky='nsew')

        self.clear_button = tk.Button(self.window, text="Clear Snapshot", fg='white', bg=button_bg,
                                         command=self.clear_snapshot, font=button_style)
        self.clear_button.grid(row=12, column=1, padx=10, pady=10, sticky='nsew')
        # Create the log text widget
        self.log_text = tk.Text(self.window, bg=log_text_bg, font=font_style)
        self.log_text.grid(row=24, column=1, columnspan=2, padx=10, pady=10, sticky='nsew')

    def allocate_memory(self):
        process_id = self.process_id_entry.get()
        size = int(self.size_entry.get())

        return_value = self.memory_manager.allocate_memory(process_id, size)
        if return_value == 1:
            self.log_text.insert(tk.END, f"Process {process_id} allocated {size}k of memory\n")
        else:
            self.log_text.insert(tk.END, f"Process {process_id} is not enough to allocate memory space\n")

    def release_memory(self):
        process_id = self.process_id_entry.get()

        return_value = self.memory_manager.release_memory(process_id)
        if return_value == 1:
            self.log_text.insert(tk.END, f"process {process_id} relesed memory\n")
        else:
            self.log_text.insert(tk.END, f"process {process_id} is not allocated any memory\n")

    def print_snapshot(self):
        self.log_text.insert(tk.END, "\n")
        snapshot = self.memory_manager.print_memory_snapshot()
        self.log_text.insert(tk.END, f"{snapshot}\n")

    def clear_snapshot(self):
        self.log_text.delete("1.0", tk.END)



    def run(self):
        self.window.mainloop()

