import tkinter as tk
from tkinter import messagebox, filedialog

class MenuBarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MAINTAINANCE DEVICE")
        self.root.geometry("600x400")

        self.create_menubar()

    def create_menubar(self):
        menubar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=1)
        file_menu.add_command(label="New", command=lambda: self.menu_action("New File"))
        file_menu.add_command(label="Save", command=lambda: self.menu_action("Save File"))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Open menu
        open_menu = tk.Menu(menubar, tearoff=1)
        open_menu.add_command(label="Open File...", command=self.open_file)
        open_menu.add_command(label="Open Folder...", command=self.open_folder)
        menubar.add_cascade(label="Open", menu=open_menu)

        # View menu
        view_menu = tk.Menu(menubar, tearoff=1)
        view_menu.add_command(label="Zoom In", command=lambda: self.menu_action("Zoom In"))
        view_menu.add_command(label="Zoom Out", command=lambda: self.menu_action("Zoom Out"))
        menubar.add_cascade(label="View", menu=view_menu)

        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=1)
        tools_menu.add_command(label="Options", command=lambda: self.menu_action("Options"))
        menubar.add_cascade(label="Tools", men=tools_menu)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=1)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    def menu_action(self, action):
        messagebox.showinfo("Menu Action", f"You selected: {action}")

    def open_file(self):
        filename = filedialog.askopenfilename(title="Open File")
        if filename:
            messagebox.showinfo("Open File", f"Selected file: {filename}")

    def open_folder(self):
        foldername = filedialog.askdirectory(title="Open Folder")
        if foldername:
            messagebox.showinfo("Open Folder", f"Selected folder: {foldername}")

    def show_about(self):
        messagebox.showinfo("About", "Menu Bar Example\nCreated with tkinter in Python.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuBarApp(root)
    root.mainloop()
