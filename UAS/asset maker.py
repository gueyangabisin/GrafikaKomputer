# Script untuk membersihkan file OBJ agar bisa dibaca Ursina
nama_file_asli = 'Vehicle_Sports.obj'
nama_file_baru = 'mobil_fix.obj'

print(f"Sedang memperbaiki {nama_file_asli}...")

try:
    with open(nama_file_asli, 'r') as f_masuk:
        lines = f_masuk.readlines()

    with open(nama_file_baru, 'w') as f_keluar:
        # Tulis ulang header sederhana
        f_keluar.write("# OBJ File Fixed for Ursina\n")
        
        for line in lines:
            # Kita hanya ambil data Geometri (v=vertex, vt=texture, vn=normal) dan Wajah (f=face)
            # Kita buang data Material (usemtl, mtllib) dan Group (o, g, s) yang bikin error
            if line.startswith(('v ', 'vt ', 'vn ', 'f ')):
                f_keluar.write(line)

    print(f"SUKSES! File baru bernama '{nama_file_baru}' telah dibuat.")
    print("Sekarang update main.py kamu untuk menggunakan file ini.")

except FileNotFoundError:
    print(f"ERROR: File {nama_file_asli} tidak ditemukan di folder ini.")