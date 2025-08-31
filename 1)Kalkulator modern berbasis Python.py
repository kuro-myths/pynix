import tkinter as tk
from tkinter import messagebox
import math

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Modern")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#1e1e1e')
        
        # Variabel untuk menyimpan ekspresi
        self.expression = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # Setup UI
        self.create_display()
        self.create_buttons()
        
        # Bind keyboard events
        self.root.bind('<Key>', self.key_press)
        self.root.focus_set()
    
    def create_display(self):
        # Frame untuk display
        display_frame = tk.Frame(self.root, bg='#1e1e1e', pady=20)
        display_frame.pack(fill='x', padx=20)
        
        # Display hasil
        self.display = tk.Label(
            display_frame,
            textvariable=self.result_var,
            font=('Arial', 32, 'bold'),
            bg='#2d2d2d',
            fg='#ffffff',
            anchor='e',
            padx=20,
            pady=20,
            relief='flat',
            bd=0
        )
        self.display.pack(fill='x', ipady=10)
        
        # Display ekspresi
        self.expression_display = tk.Label(
            display_frame,
            text="",
            font=('Arial', 14),
            bg='#1e1e1e',
            fg='#888888',
            anchor='e',
            padx=20
        )
        self.expression_display.pack(fill='x', pady=(10, 0))
    
    def create_buttons(self):
        # Frame untuk tombol
        button_frame = tk.Frame(self.root, bg='#1e1e1e')
        button_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Konfigurasi grid
        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1, uniform="row")
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1, uniform="col")
        
        # Definisi tombol dengan warna berbeda
        buttons = [
            # Row 0 - Fungsi khusus
            ('C', 0, 0, '#ff6b6b', '#ffffff', self.clear),
            ('⌫', 0, 1, '#ff9f43', '#ffffff', self.backspace),
            ('√', 0, 2, '#5f27cd', '#ffffff', lambda: self.operation('sqrt')),
            ('÷', 0, 3, '#5f27cd', '#ffffff', lambda: self.operation('/')),
            
            # Row 1
            ('7', 1, 0, '#3d3d3d', '#ffffff', lambda: self.input_number('7')),
            ('8', 1, 1, '#3d3d3d', '#ffffff', lambda: self.input_number('8')),
            ('9', 1, 2, '#3d3d3d', '#ffffff', lambda: self.input_number('9')),
            ('×', 1, 3, '#5f27cd', '#ffffff', lambda: self.operation('*')),
            
            # Row 2
            ('4', 2, 0, '#3d3d3d', '#ffffff', lambda: self.input_number('4')),
            ('5', 2, 1, '#3d3d3d', '#ffffff', lambda: self.input_number('5')),
            ('6', 2, 2, '#3d3d3d', '#ffffff', lambda: self.input_number('6')),
            ('-', 2, 3, '#5f27cd', '#ffffff', lambda: self.operation('-')),
            
            # Row 3
            ('1', 3, 0, '#3d3d3d', '#ffffff', lambda: self.input_number('1')),
            ('2', 3, 1, '#3d3d3d', '#ffffff', lambda: self.input_number('2')),
            ('3', 3, 2, '#3d3d3d', '#ffffff', lambda: self.input_number('3')),
            ('+', 3, 3, '#5f27cd', '#ffffff', lambda: self.operation('+')),
            
            # Row 4
            ('±', 4, 0, '#3d3d3d', '#ffffff', self.toggle_sign),
            ('0', 4, 1, '#3d3d3d', '#ffffff', lambda: self.input_number('0')),
            ('.', 4, 2, '#3d3d3d', '#ffffff', lambda: self.input_number('.')),
            ('=', 4, 3, '#00d2d3', '#ffffff', self.calculate),
            
            # Row 5 - Fungsi tambahan
            ('sin', 5, 0, '#5f27cd', '#ffffff', lambda: self.operation('sin')),
            ('cos', 5, 1, '#5f27cd', '#ffffff', lambda: self.operation('cos')),
            ('tan', 5, 2, '#5f27cd', '#ffffff', lambda: self.operation('tan')),
            ('π', 5, 3, '#5f27cd', '#ffffff', lambda: self.input_number(str(math.pi))),
        ]
        
        # Buat tombol
        self.buttons = {}
        for text, row, col, bg_color, fg_color, command in buttons:
            btn = tk.Button(
                button_frame,
                text=text,
                font=('Arial', 18, 'bold'),
                bg=bg_color,
                fg=fg_color,
                activebackground=self.lighten_color(bg_color),
                activeforeground=fg_color,
                relief='flat',
                bd=0,
                command=command,
                cursor='hand2'
            )
            btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
            self.buttons[text] = btn
            
            # Efek hover
            self.add_hover_effect(btn, bg_color, fg_color)
    
    def lighten_color(self, color):
        """Membuat warna lebih terang untuk efek hover"""
        color_map = {
            '#3d3d3d': '#4d4d4d',
            '#5f27cd': '#7c4ddb',
            '#ff6b6b': '#ff8e8e',
            '#ff9f43': '#ffb366',
            '#00d2d3': '#33dde0'
        }
        return color_map.get(color, '#4d4d4d')
    
    def add_hover_effect(self, button, normal_color, text_color):
        """Menambahkan efek hover pada tombol"""
        hover_color = self.lighten_color(normal_color)
        
        def on_enter(e):
            button.config(bg=hover_color)
        
        def on_leave(e):
            button.config(bg=normal_color)
        
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
    
    def input_number(self, number):
        """Input angka atau titik desimal"""
        if self.result_var.get() == "0" and number != ".":
            self.result_var.set(number)
        else:
            current = self.result_var.get()
            if number == "." and "." in current.split()[-1]:
                return  # Mencegah multiple decimal points
            self.result_var.set(current + number)
        
        self.expression += number
        self.update_expression_display()
    
    def operation(self, op):
        """Handle operasi matematika"""
        try:
            current = self.result_var.get()
            
            if op in ['sin', 'cos', 'tan']:
                # Fungsi trigonometri
                value = float(current)
                if op == 'sin':
                    result = math.sin(math.radians(value))
                elif op == 'cos':
                    result = math.cos(math.radians(value))
                elif op == 'tan':
                    result = math.tan(math.radians(value))
                
                self.result_var.set(str(round(result, 8)))
                self.expression = f"{op}({current})"
                
            elif op == 'sqrt':
                # Akar kuadrat
                value = float(current)
                if value < 0:
                    messagebox.showerror("Error", "Tidak dapat menghitung akar kuadrat dari bilangan negatif")
                    return
                result = math.sqrt(value)
                self.result_var.set(str(round(result, 8)))
                self.expression = f"√({current})"
                
            else:
                # Operasi aritmatika biasa
                self.expression += f" {op} "
                self.result_var.set("0")
            
            self.update_expression_display()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error dalam operasi: {str(e)}")
    
    def calculate(self):
        """Menghitung hasil ekspresi"""
        try:
            if not self.expression:
                return
            
            # Replace operator symbols
            expr = self.expression.replace('×', '*').replace('÷', '/')
            
            # Evaluasi ekspresi
            result = eval(expr)
            
            # Format hasil
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 8)
            
            self.result_var.set(str(result))
            self.expression = str(result)
            self.update_expression_display()
            
        except ZeroDivisionError:
            messagebox.showerror("Error", "Tidak dapat membagi dengan nol")
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", f"Ekspresi tidak valid: {str(e)}")
            self.clear()
    
    def clear(self):
        """Membersihkan semua input"""
        self.result_var.set("0")
        self.expression = ""
        self.update_expression_display()
    
    def backspace(self):
        """Menghapus karakter terakhir"""
        current = self.result_var.get()
        if len(current) > 1:
            new_value = current[:-1]
            self.result_var.set(new_value)
            if self.expression:
                self.expression = self.expression[:-1]
        else:
            self.result_var.set("0")
            self.expression = ""
        self.update_expression_display()
    
    def toggle_sign(self):
        """Mengubah tanda positif/negatif"""
        current = self.result_var.get()
        if current != "0":
            if current.startswith('-'):
                new_value = current[1:]
            else:
                new_value = '-' + current
            self.result_var.set(new_value)
            # Update expression juga
            if self.expression and self.expression[-len(current):] == current:
                self.expression = self.expression[:-len(current)] + new_value
        self.update_expression_display()
    
    def update_expression_display(self):
        """Update tampilan ekspresi"""
        display_expr = self.expression.replace('*', '×').replace('/', '÷')
        self.expression_display.config(text=display_expr)
    
    def key_press(diri, peristiwa):
        """ Menangani papan ketik masukan """
 kunci = peristiwa.char
        
        # Angka dan titik
        if key.isdigit() atau kunci == '.':
 self.masuk_nomor(key)
        
        # Operasi
        elif kunci == '+':
 self.operasi('+')
        elif kunci == '-':
 self.operasi('-')
        elif kunci == '*':
 self.operasi('*')
        elif kunci == '/':
 self.operasi('/')
        
        # Masuk keuntuk hitung
        elif event.keysym == ' Return ':
 self.menghitung()
        
        # Escape atau Hapus untuk jelas
        elif event.keysym di [' Escape ', ‘Hapus’]:
 self.jelas()
        
        # Ruang Belakang
        elif event.keysym == ' BackSpace ':
 self.backspace()

def utama():
 root = tk.Tk()
 kalkulator = Kalkulator Modern(root)
    
    # Set icon (opsional)
    try:
 root.ikonbitmap("kalkulator.ico")  # Ikon file ada Rika
 kecuali:
        pass
    
 root.mainloop()

if __nama__ == "__utama__":
    utama()
