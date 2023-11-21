import tkinter as tk
from tkinter import filedialog, scrolledtext
from tkinter import font,simpledialog
class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor by Omkar Shelke || codeclause")
        self.root.geometry("700x500")

        self.text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, undo=True)
        self.text_widget.pack(expand=True, fill='both')

        # Menu Bar
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        self.file_menu.add_command(label="Save As", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.destroy, accelerator="Alt+F4")

        # Edit Menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_widget.edit_undo, accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Redo", command=self.text_widget.edit_redo, accelerator="Ctrl+Y")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
        self.edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
        self.edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="Ctrl+V")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=self.select_all_text, accelerator="Ctrl+A")
        
        # format menu 
        self.format_menu=tk.Menu(self.menu_bar,tearoff=0)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_command(label='Word wrap',command=self.text_wrap,accelerator="Ctrl+W")
        self.format_menu.add_command(label='Font',command=self.set_font,accelerator="Ctrl+F")

        # Binding keyboard shortcuts
        root.bind_all("<Control-n>", lambda event: self.new_file())
        root.bind_all("<Control-o>", lambda event: self.open_file())
        root.bind_all("<Control-s>", lambda event: self.save_file())
        root.bind_all("<Control-Shift-s>", lambda event: self.save_as_file())
        root.bind_all("<Control-z>", lambda event: self.text_widget.edit_undo())
        root.bind_all("<Control-y>", lambda event: self.text_widget.edit_redo())
        root.bind_all("<Control-x>", lambda event: self.cut_text())
        root.bind_all("<Control-c>", lambda event: self.copy_text())
        root.bind_all("<Control-v>", lambda event: self.paste_text())
        root.bind_all("<Control-a>", lambda event: self.select_all_text())
        root.bind_all("<Control-a>", lambda event: self.select_all_text())
        root.bind_all("<Control-w>", lambda event: self.text_wrap())
        root.bind_all("<Control-f>", lambda event: self.set_font())

    def new_file(self):
        self.text_widget.delete(1.0, tk.END)
        self.root.title("Text Editor")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(tk.END, content)
            self.root.title(f"Text Editor - {file_path}")

    def save_file(self):
        if self.root.title() == "Text Editor":
            self.save_as_file()
        else:
            file_path = self.root.title()[13:]
            content = self.text_widget.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(content)

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            content = self.text_widget.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(content)
            self.root.title(f"Text Editor - {file_path}")

    def cut_text(self):
        self.text_widget.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_widget.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_widget.event_generate("<<Paste>>")

    def select_all_text(self):
        self.text_widget.tag_add(tk.SEL, "1.0", tk.END)

    
    def text_wrap(self):
        current_wrap_status = self.text_widget.cget("wrap")
        if current_wrap_status == "none":
            self.text_widget.config(wrap="word")
        else:
            self.text_widget.config(wrap="none")

    def set_font(self):
        font_string = simpledialog.askstring("Font", "Enter font (e.g., Arial 12):")
        if font_string:
            self.text_widget.config(font=font_string)
            
if __name__ == "__main__":
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()

# it is very similar to notepad in windows 
# let's run the program 