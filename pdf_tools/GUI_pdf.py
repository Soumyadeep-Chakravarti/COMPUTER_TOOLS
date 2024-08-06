import tkinter as tk
from tkinter import filedialog, messagebox
from pdf_tools import perform_conversion, conversions

class PDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Converter")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select an option:").pack(pady=10)
        self.option_var = tk.StringVar(value='1')
        for key, (description, _) in conversions.items():
            Radiobutton = tk.Radiobutton(self.root,
                                         text=description, 
                                         variable=self.option_var, 
                                         value=key)
            Radiobutton.pack(anchor='w')

        Select_file_button = tk.Button(self.root, 
                                       text="Select File", 
                                       command=self.select_file)
        
        Select_output_button = tk.Button(self.root,
                                         text="Select Output Path",
                                         command=self.select_output_path)
        
        Convert_button = tk.Button(self.root, 
                                   text="Convert", 
                                   command=self.convert)
        
        Select_file_button.pack(pady=5)
        Select_output_button.pack(pady=5)
        Convert_button.pack(pady=10)
        
        self.file_path = None
        self.output_path = None

    def select_file(self):
        self.pdf_path = filedialog.askopenfilename(title="Select File")
        if self.pdf_path:
            print(f"Selected file: {self.file_path}")

    def select_output_path(self):
        self.output_path = filedialog.askdirectory(title="Select Output Directory")
        if self.output_path:
            print(f"Selected output path: {self.output_path}")

    def convert(self):
        choice = self.option_var.get()
        if self.pdf_path and self.output_path:
            success, message = perform_conversion(choice, self.file_path, self.output_path)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showwarning("Warning", "Please select both an input file and an output path.")

def main():
    root = tk.Tk()
    app = PDFConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
