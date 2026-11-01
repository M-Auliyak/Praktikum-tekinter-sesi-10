import tkinter as tk
from tkinter import ttk, messagebox

# Inisialisasi Jendela Utama
root = tk.Tk()
root.title("Formulir Identitas Mahasiswa")
root.geometry("480x520")
root.configure(bg="#f4f6f9")  # Warna latar belakang konsisten

# Konfigurasi Styling Warna & Font
BG_COLOR = "#f4f6f9"
PRIMARY_COLOR = "#1e3d59"
ACCENT_COLOR = "#17b978"
DANGER_COLOR = "#ff5252"
TEXT_COLOR = "#333333"

# Judul Aplikasi
title_label = tk.Label(
    root, 
    text="FORM IDENTITAS MAHASISWA", 
    font=("Segoe UI", 16, "bold"),
    bg=BG_COLOR,
    fg=PRIMARY_COLOR
)
title_label.grid(row=0, column=0, columnspan=2, pady=15)

# Frame Form menggunakan grid()
form_frame = tk.Frame(root, bg=BG_COLOR)
form_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=5, sticky="nsew")

# 1. Label & Entry Nama
tk.Label(form_frame, text="Nama", font=("Segoe UI", 10, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, sticky="w", pady=8)
nama_entry = tk.Entry(form_frame, width=32, font=("Segoe UI", 10))
nama_entry.grid(row=0, column=1, pady=8, padx=10)

# 2. Label & Entry NIM
tk.Label(form_frame, text="NIM", font=("Segoe UI", 10, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, sticky="w", pady=8)
nim_entry = tk.Entry(form_frame, width=32, font=("Segoe UI", 10))
nim_entry.grid(row=1, column=1, pady=8, padx=10)

# 3. Label & Combobox Program Studi
tk.Label(form_frame, text="Program Studi", font=("Segoe UI", 10, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=2, column=0, sticky="w", pady=8)
prodi_combobox = ttk.Combobox(
    form_frame,
    values=[" Teknik Informatika", "Manajemen", "Akuntansi", "Sistem Informasi", "Teknik Elektro"],
    state="readonly",
    width=30
)
prodi_combobox.grid(row=2, column=1, pady=8, padx=10)

# 4. Label & Text Widget Alamat (Tugas Pengembangan 1)
tk.Label(form_frame, text="Alamat", font=("Segoe UI", 10, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=3, column=0, sticky="nw", pady=8)
alamat_text = tk.Text(form_frame, width=24, height=4, font=("Segoe UI", 10))
alamat_text.grid(row=3, column=1, pady=8, padx=10, sticky="w")

# Label untuk Menampilkan Hasil Input
hasil_label = tk.Label(
    root, 
    text="", 
    font=("Segoe UI", 10), 
    bg="#ffffff", 
    fg=TEXT_COLOR,
    justify="left",
    relief="solid",
    bd=1,
    padx=10,
    pady=10
)
hasil_label.grid(row=2, column=0, columnspan=2, padx=20, pady=15, sticky="nsew")

# Fungsi Tombol Simpan dengan Validasi (Tugas Pengembangan 3)
def simpan_data():
    nama = nama_entry.get().strip()
    nim = nim_entry.get().strip()
    prodi = prodi_combobox.get().strip()
    alamat = alamat_text.get("1.0", tk.END).strip()

    # Validasi input tidak boleh kosong
    if not nama or not nim or not prodi or not alamat:
        messagebox.showerror("Peringatan", "Semua kolom (Nama, NIM, Program Studi, Alamat) wajib diisi!")
        return

    # Menampilkan hasil pada Label
    teks_hasil = (
        f"--- DATA BERHASIL DISIMPAN ---\n"
        f"Nama          : {nama}\n"
        f"NIM           : {nim}\n"
        f"Program Studi : {prodi}\n"
        f"Alamat        : {alamat}"
    )
    hasil_label.config(text=teks_hasil, fg="#000000")

# Fungsi Tombol Reset
def reset_form():
    nama_entry.delete(0, tk.END)
    nim_entry.delete(0, tk.END)
    prodi_combobox.set("")
    alamat_text.delete("1.0", tk.END)
    hasil_label.config(text="")

# Fungsi Tombol Keluar (Tugas Pengembangan 5)
def keluar_aplikasi():
    if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin keluar?"):
        root.destroy()

# Frame Tombol-tombol Aksi menggunakan grid()
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.grid(row=3, column=0, columnspan=2, pady=10)

btn_simpan = tk.Button(button_frame, text="Simpan", command=simpan_data, bg=ACCENT_COLOR, fg="white", font=("Segoe UI", 9, "bold"), width=10, relief="flat")
btn_simpan.grid(row=0, column=0, padx=5)

btn_reset = tk.Button(button_frame, text="Reset", command=reset_form, bg="#ffc107", fg="black", font=("Segoe UI", 9, "bold"), width=10, relief="flat")
btn_reset.grid(row=0, column=1, padx=5)

btn_keluar = tk.Button(button_frame, text="Keluar", command=keluar_aplikasi, bg=DANGER_COLOR, fg="white", font=("Segoe UI", 9, "bold"), width=10, relief="flat")
btn_keluar.grid(row=0, column=2, padx=5)

# Menjalankan Mainloop
root.mainloop()