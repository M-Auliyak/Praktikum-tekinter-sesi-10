# Formulir Identitas Mahasiswa (Tkinter)

Aplikasi GUI sederhana berbasis **Python + Tkinter** untuk mengisi, menampilkan, dan mengosongkan data identitas mahasiswa. Dibuat untuk **Tugas Praktikum Sesi 1 – Membuat Formulir Identitas Mahasiswa**.

## Deskripsi

Pengguna mengisi Nama, NIM, Program Studi, dan Alamat, lalu menekan **Simpan** untuk menampilkan data pada sebuah Label. Tombol **Reset** mengosongkan formulir, dan tombol **Keluar** menutup aplikasi setelah konfirmasi.

## Fitur

| Fitur | Implementasi |
|---|---|
| Jendela berjudul "Formulir Identitas Mahasiswa" | `root.title(...)`, ukuran `480x520` |
| Label Nama, NIM, Program Studi, Alamat | `tk.Label` |
| Input Nama dan NIM | `tk.Entry` |
| Pilihan Program Studi | `ttk.Combobox` (mode `readonly`) |
| Input Alamat (multi-baris) | `tk.Text` |
| Tombol Simpan + hasil pada Label | `simpan_data()` dan `hasil_label` |
| Tombol Reset | `reset_form()` |
| Tombol Keluar dengan konfirmasi | `keluar_aplikasi()` dan `messagebox.askyesno` |
| Validasi input tidak kosong | `messagebox.showerror` jika ada kolom kosong |
| Warna, font, dan tata letak konsisten | Konstanta warna, font Segoe UI, `grid()` |

## Pilihan Program Studi

Teknik Informatika, Manajemen, Akuntansi, Sistem Informasi, Teknik Elektro.

## Persyaratan

- Python 3.8 atau lebih baru
- Tkinter (sudah termasuk pada instalasi Python di Windows dan macOS)
  - Linux (Debian/Ubuntu): `sudo apt install python3-tk`
- Tidak memerlukan library tambahan.

## Cara Menjalankan

1. Clone repositori ini atau unduh file `main.py`.
   ```bash
   git clone <url-repositori>
   cd <nama-folder-repositori>
   ```
2. Jalankan program.
   ```bash
   python main.py
   ```
   (Gunakan `python3 main.py` jika `python` tidak dikenali.)

## Cara Menggunakan

1. Isi **Nama**, **NIM**, **Program Studi**, dan **Alamat**.
2. Klik **Simpan**. Jika ada kolom kosong, muncul pesan peringatan. Jika lengkap, data tampil pada kotak hasil:
   ```
   --- DATA BERHASIL DISIMPAN ---
   Nama          : ...
   NIM           : ...
   Program Studi : ...
   Alamat        : ...
   ```
3. Klik **Reset** untuk mengosongkan seluruh input dan hasil.
4. Klik **Keluar** lalu pilih **Yes** untuk menutup aplikasi.

## Struktur Program

```
.
├── main.py      # Seluruh kode aplikasi
└── README.md    # Dokumentasi
```

Alur kode di `main.py`:

1. Membuat jendela utama dan konfigurasi warna (`BG_COLOR`, `PRIMARY_COLOR`, `ACCENT_COLOR`, `DANGER_COLOR`, `TEXT_COLOR`).
2. Membuat judul, form (Entry, Combobox, Text), dan Label hasil, semuanya ditata dengan `grid()`.
3. Mendefinisikan fungsi `simpan_data()`, `reset_form()`, dan `keluar_aplikasi()`.
4. Membuat tombol Simpan, Reset, Keluar pada satu Frame.
5. Menjalankan `root.mainloop()`.

## Tugas Pengembangan yang Dikerjakan

- [x] Input alamat menggunakan widget `Text`
- [x] Kombinasi warna yang konsisten
- [x] Validasi agar kolom tidak kosong
- [x] Layout menggunakan `grid()`
- [x] Tombol Keluar

## Catatan

- Font **Segoe UI** tersedia di Windows; di sistem lain Tkinter otomatis memakai font pengganti sehingga tampilan bisa sedikit berbeda.
- Data hanya ditampilkan pada Label dan tidak disimpan ke file atau database.

## Tangkapan Layar

<!-- Tambahkan screenshot, misalnya: ![Tampilan aplikasi](screenshot.png) -->

## Identitas Pembuat

- Nama   : Muhammad Auliyak Akbar
- NIM    : 2595114019
- Mata Kuliah / Kelas : Pemograman berorientasi object / Ti B