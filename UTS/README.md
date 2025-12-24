# MINI SECNE RUMAH
### implementasi algoritma dan transfotmasi 2 dimensi
Proyek ini mendemonstrasikan bagaimana sebuah grafis sederhana dibentuk dari nol menggunakan koordinat piksel dan algoritma dasar komputer grafis tanpa menggunakan library eksternal tingkat tinggi.

### 1. Algoritma DDA
Digunakan untuk: Menggambar garis lurus (Dinding, Atap, Pintu).
Algoritma DDA adalah algoritma pembentukan garis yang bekerja berdasarkan perhitungan selisih koordinat x dan y.
Prinsip Kerja: Algoritma ini mencari selisih jarak (\Delta x dan \Delta y) antara dua titik.
Increment: Nilai koordinat ditambah secara bertahap (step-by-step) berdasarkan kemiringan garis (gradien).
Rasterisasi: Karena layar komputer terdiri dari piksel (bilangan bulat), hasil perhitungan desimal dalam DDA akan selalu dibulatkan menggunakan fungsi round() untuk menentukan posisi piksel yang paling akurat di layar.

### 2. Algoritma Mid Point Circle
Algoritma ini jauh lebih efisien daripada menggunakan fungsi trigonometri (sin / cos) karena hanya menggunakan operasi aritmatika penjumlahan dan pengurangan.
Prinsip Kerja: Algoritma ini menentukan jalur piksel yang paling mendekati lengkungan lingkaran dengan mengevaluasi "Decision Parameter" di setiap langkahnya.
Simetri 8-Oktan: Kita hanya perlu menghitung koordinat untuk seperdelapan lingkaran. Sisa tujuh bagian lainnya digambar dengan mencerminkan titik-titik tersebut secara matematis, sehingga proses rendering menjadi jauh lebih cepat.

### 3. Transformasi Translasi
Digunakan untuk: Menggerakkan matahari secara interaktif.
Transformasi 2 dimensi ini memungkinkan objek untuk berpindah posisi dari koordinat lama ke koordinat baru di dalam canvas.
Prinsip Kerja: Translasi dilakukan dengan menambahkan nilai pergeseran (tx untuk horizontal dan ty untuk vertikal) pada titik pusat objek. Dalam proyek ini, nilai tx dan ty dipicu oleh input keyboard. Setiap kali posisi berubah, sistem akan menghitung ulang seluruh piksel menggunakan algoritma DDA dan Mid Point agar matahari terlihat berpindah tempat secara real-time.
