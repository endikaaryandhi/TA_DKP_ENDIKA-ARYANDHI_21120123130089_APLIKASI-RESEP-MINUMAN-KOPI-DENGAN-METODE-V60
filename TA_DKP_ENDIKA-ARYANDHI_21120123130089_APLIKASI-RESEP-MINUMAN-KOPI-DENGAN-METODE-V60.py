import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import Scrollbar
import os

base_dir = os.path.dirname(__file__)

window = tk.Tk()
window.geometry("1024x768") 

window.title("Aplikasi Resep Minuman Kopi dengan Metode V60 oleh Endika Aryandhi - 21120123130089")

background_image_path = os.path.join(base_dir, "kopi1.jpg")
background_image = Image.open(background_image_path)
background_image = background_image.resize((1024, 768), Image.LANCZOS)  
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, width=1024, height=768)  

selection_frame = ttk.Frame(window, style="Transparent.TFrame")
selection_frame.place(relx=0.5, rely=0.5, anchor="center", width=600, height=600)

coffee_var = tk.BooleanVar()

illustration_image_path = os.path.join(base_dir, "ilus.png")
illustration_image = Image.open(illustration_image_path)
illustration_image = illustration_image.resize((200, 200), Image.LANCZOS)
illustration_photo = ImageTk.PhotoImage(illustration_image)
illustration_label = tk.Label(selection_frame, image=illustration_photo)
illustration_label.image = illustration_photo  
illustration_label.place(relx=0.5, rely=0.25, anchor="center", width=200, height=200)

gayo_button = tk.Radiobutton(selection_frame, text="Gayo", variable=coffee_var, value="gayo", command=lambda: display_recipe("gayo"))
gayo_button.place(relx=0.5, rely=0.5, anchor="center", y=0)

kerinci_button = tk.Radiobutton(selection_frame, text="Kerinci", variable=coffee_var, value="kerinci", command=lambda: display_recipe("kerinci"))
kerinci_button.place(relx=0.5, rely=0.5, anchor="center", y=40)

mandheling_button = tk.Radiobutton(selection_frame, text="Mandheling", variable=coffee_var, value="mandheling", command=lambda: display_recipe("mandheling"))
mandheling_button.place(relx=0.5, rely=0.5, anchor="center", y=80)

favorit = []

def push(stack, item):
    stack.append(item)

def pop(stack):
    if stack:
        return stack.pop()
    return None

def display_recipe(coffee):
    if coffee == "gayo":
        steps = [
            ("Biji yang digunakan sejumlah 15 gram", ""),
            ("Air yang digunakan sejumlah","350 ml"),
            ("Gunakan v60 dripper, paper filter, timbangan, server kopi",""),
            ("Letakkan paper filter ke dripper",""),
            ("Letakkan dripper ke atas server kopi",""),
            ("Letakkan server kopi ke atas timbangan",""),
            ("Basahi paper filter dengan air sebanyak", "100 ml"),
            ("Buang air di dalam server kopi dan mulai untuk tuangan pertama",""),
            ("Tuangan Pertama", "30 ml"),
            ("Tunggu selama 45 detik (blooming)", ""),
            ("Tuangan Kedua", "120 ml (total 150 ml)"),
            ("Tunggu hingga air mengalir habis", ""),
            ("Tuangan Ketiga", "50 ml (total 200 ml)"),
            ("Tunggu hingga air mengalir hampir habis", ""),
            ("Tuangan Keempat", "50 ml (total 250 ml)"),
            ("Tunggu hingga semua air mengalir habis", ""),
            ("Kopi siap disajikan", "")
        ]
    elif coffee == "kerinci" or coffee == "mandheling":
        steps = [
            ("Biji yang digunakan sejumlah 15 gram", ""),
            ("Air yang digunakan sejumlah","350 ml"),
            ("Gunakan v60 dripper, paper filter, timbangan, server kopi",""),
            ("Letakkan paper filter ke dripper",""),
            ("Letakkan dripper ke atas server kopi",""),
            ("Letakkan server kopi ke atas timbangan",""),
            ("Basahi paper filter dengan air sebanyak", "100 ml"),
            ("Buang air di dalam server kopi dan mulai untuk tuangan pertama",""),
            ("Tuangan Pertama (Pre-infusion)", "30 ml"),
            ("Tunggu selama 30-45 detik (blooming)", ""),
            ("Tuangan Kedua", "70 ml (total 100 ml)"),
            ("Tunggu hingga air mengalir habis", ""),
            ("Tuangan Ketiga", "75 ml (total 175 ml)"),
            ("Tunggu hingga air mengalir habis", ""),
            ("Tuangan Keempat", "75 ml (total 250 ml)"),
            ("Tunggu hingga semua air mengalir habis", ""),
            ("Kopi siap disajikan", "")
        ]

    for widget in selection_frame.winfo_children():
        widget.destroy()

    tree = ttk.Treeview(selection_frame, columns=("Cara", "Banyaknya Air"), show="headings")
    tree.heading("Cara", text="Cara")
    tree.heading("Banyaknya Air", text="Banyaknya Air")
    tree.column("Cara", width=400)
    tree.column("Banyaknya Air", width=200)

    for step in steps:
        tree.insert("", "end", values=step)

    tree.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

    kembali_button = tk.Button(selection_frame, text="Kembali", command=lambda: confirm_exit())
    kembali_button.place(relx=0.05, rely=0.85, relwidth=0.9, relheight=0.08)

    tambahkan_favorit_button = tk.Button(selection_frame, text="Tambahkan ke Favorit", command=lambda: tambahkan_favorit(coffee))
    tambahkan_favorit_button.place(relx=0.05, rely=0.77, relwidth=0.9, relheight=0.08)

def tambahkan_favorit(coffee):
    for favorite in favorit:
        if favorite[0] == coffee:
            messagebox.showinfo("Info", f"Resep {coffee} sudah ada di daftar favorit.")
            return

    if coffee == "gayo":
        steps = [
            ("Biji yang digunakan sejumlah 15 gram", ""),
            ("Air yang digunakan sejumlah","350 ml"),
            ("Gunakan v60 dripper, paper filter, timbangan, server kopi",""),
            ("Letakkan paper filter ke dripper",""),
            ("Letakkan dripper ke atas server kopi",""),
            ("Letakkan server kopi ke atas timbangan",""),
            ("Basahi paper filter dengan air sebanyak", "100 ml"),
            ("Buang air di dalam server kopi dan mulai untuk tuangan pertama",""),
            ("Tuangan Pertama", "30 ml"),
            ("Tunggu selama 45 detik (blooming)", ""),
            ("Tuangan Kedua", "120 ml (total 150 ml)"),
            ("Tunggu hingga air mengalir habis", ""),
            ("Tuangan Ketiga", "50 ml (total 200 ml)"),
            ("Tunggu hingga air mengalir hampir habis", ""),
            ("Tuangan Keempat", "50 ml (total 250 ml)"),
            ("Tunggu hingga semua air mengalir habis", ""),
            ("Kopi siap disajikan", "")
        ]
    elif coffee == "kerinci" or coffee == "mandheling":
        steps = [
            ("Biji yang digunakan sejumlah 15 gram", ""),
            ("Air yang digunakan sejumlah","350 ml"),
            ("Gunakan v60 dripper, paper filter, timbangan, server kopi",""),
            ("Letakkan paper filter ke dripper",""),
            ("Letakkan dripper ke atas server kopi",""),
            ("Letakkan server kopi ke atas timbangan",""),
            ("Basahi paper filter dengan air sebanyak", "100 ml"),
            ("Buang air di dalam server kopi dan mulai untuk tuangan pertama",""),
            ("Tuangan Pertama (Pre-infusion)", "30 ml"),
            ("Tunggu selama 30-45 detik (blooming)", ""),
            ("Tuangan Kedua", "70 ml (total 100 ml)"),
            ("Tunggu hingga air mengalir habis", ""),
            ("Tuangan Ketiga", "75 ml (total 175 ml)"),
            ("Tunggu hingga air mengalir habis", ""),
            ("Tuangan Keempat", "75 ml (total 250 ml)"),
            ("Tunggu hingga semua air mengalir habis", ""),
            ("Kopi siap disajikan", "")
        ]

    push(favorit, (coffee, steps))
    messagebox.showinfo("Info", f"Resep {coffee} berhasil ditambahkan ke daftar favorit.")

def reset_menu():
    for widget in selection_frame.winfo_children():
        widget.destroy()

    illustration_image_path = os.path.join(base_dir, "ilus.png")
    illustration_image = Image.open(illustration_image_path)
    illustration_image = illustration_image.resize((200, 200), Image.LANCZOS)
    illustration_photo = ImageTk.PhotoImage(illustration_image)
    illustration_label = tk.Label(selection_frame, image=illustration_photo)
    illustration_label.image = illustration_photo  
    illustration_label.place(relx=0.5, rely=0.25, anchor="center", width=200, height=200)

    gayo_button = tk.Radiobutton(selection_frame, text="Gayo", variable=coffee_var, value="gayo", command=lambda: display_recipe("gayo"))
    gayo_button.place(relx=0.5, rely=0.5, anchor="center", y=0)

    kerinci_button = tk.Radiobutton(selection_frame, text="Kerinci", variable=coffee_var, value="kerinci", command=lambda: display_recipe("kerinci"))
    kerinci_button.place(relx=0.5, rely=0.5, anchor="center", y=40)

    mandheling_button = tk.Radiobutton(selection_frame, text="Mandheling", variable=coffee_var, value="mandheling", command=lambda: display_recipe("mandheling"))
    mandheling_button.place(relx=0.5, rely=0.5, anchor="center", y=80)

    lihat_favorit_button = tk.Button(selection_frame, text="Lihat Favorit", command=lambda: lihat_favorit())
    lihat_favorit_button.place(relx=0.05, rely=0.85, relwidth=0.9, relheight=0.1)

def lihat_favorit():
    for widget in selection_frame.winfo_children():
        widget.destroy()

    tree = ttk.Treeview(selection_frame, columns=("Kopi"), show="headings", height=10)
    tree.heading("Kopi", text="Kopi")
    tree.column("Kopi", width=200)

    scrollbar = Scrollbar(selection_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.place(relx=0.95, rely=0.05, relwidth=0.05, relheight=0.8)

    for coffee, _ in favorit:
        tree.insert("", "end", values=(coffee,))

    tree.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.75)

    hapus_terakhir_button = tk.Button(selection_frame, text="Hapus Terakhir", command=lambda: hapus_terakhir_favorit())
    hapus_terakhir_button.place(relx=0.55, rely=0.8, relwidth=0.4, relheight=0.08)

    kembali_button = tk.Button(selection_frame, text="Kembali", command=lambda: confirm_exit())
    kembali_button.place(relx=0.05, rely=0.8, relwidth=0.4, relheight=0.08)

def hapus_terakhir_favorit():
    pop(favorit)
    lihat_favorit()

def confirm_exit():
    while True:
        response = messagebox.askyesno("Konfirmasi", "Apakah Anda ingin kembali ke menu utama?")
        if response:
            reset_menu()
            break
        else:
            break

keluar_menu = tk.Menu(window)
window.config(menu=keluar_menu)

keluar_menu.add_command(label="Keluar", command=window.destroy)

window.mainloop()
