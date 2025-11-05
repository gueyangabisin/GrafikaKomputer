<img width="1102" height="682" alt="titik46" src="https://github.com/user-attachments/assets/b0104185-ca75-4b0a-8308-aeaf71781d52" />
1.	Titik koordinat (4.6)
membuat titik dengan ukuran 10 x 10 dimana titik koordinat (4,6) ditandai  dengan “X”. target koordinat disimpan dalam variable ‘x’ dan ‘y’. print vertical menggunakaniterasi 0 sampai 10 dengan variable ‘a’, setiapiterasi vertical dilakukan   iterasi horizontal 0 sampai 10 dengan variable ‘b’. Setiap iterasi horizontal terdapatkondisi Ketika nilai a = 6, dan b = 4  makaakan mengeluarkan “X”, dan jika tidak akan mengeluarkan “.”.

<img width="1102" height="713" alt="titikKoordinat42" src="https://github.com/user-attachments/assets/5c52aa35-6ef5-4bd1-86c1-6a0bbcebf66a" />
2.	Titik koordinat (4,2)
membuat titik dengan ukuran5 x 10 dimana titik koordinat (4,2) ditandai dengan “X”. target koordinat disimpan dalam variable ‘x’ dan ‘y’. print vertical menggunakan iterasi 0 sampai 5 dengan variable ‘a’, setiap iterasi vertical dilakukan iterasi horizontal 0 sampai 10 dengan variable ‘b’. Setiapp iterasi horizontal terdapat kondisi Ketika nilai a = 2, dan b = 4maka akan mengeluarkan “X”, dan jika tidak akan mengeluarkan “*”.


<img width="1102" height="1002" alt="kuadran" src="https://github.com/user-attachments/assets/5833c259-5c3f-4354-b6c9-0ebd1cfadb9b" />
3.	Menghitung kuadran
koordinat titik satu disimpan dalam variable ‘a’ dan ‘b’, koordinat titik kedua disimpan dalam variable ‘c’ dan ‘d’.
fungsi ‘kuadran’ dengan parameter ‘x’ dan ‘y’ berfungsi untuk mendeteksi posisi titik, apakah berada pada kuadran 1,2,3 atau 4, dengan menggunakan percabangan.
perhitungan jarak antar pasangan titik koordinat dilakukan dengan rumus, kemudian di simpan dalam variabel ‘jarak’.
pemanggilan fungsi ‘kuadran’ dengan memasukkan parameter berupa titik yang dicari posisi koordinatnya.

<img width="960" height="1020" alt="gambarGaris" src="https://github.com/user-attachments/assets/b05292a7-ace3-4e85-9ce9-403632e43183" />
4.	menggambar garis
dimuli dengan inisialisasi pasangan nilai titik koordinat 1 dan 2 kedalam variabel ‘y1’, ‘x1’, ‘y2’, ‘x1’.
Kemudian mendeklarasikan variabel ‘kx’ dan ‘ky’ untuk menyimpan titik koordinat yang akan dilewati garis.
Variabel ‘lkh’ menyimpan jumlah titik yang diperlukan untuk mencapai garis dari titik pertama ke titik kedua.
Variabel ‘dx’ dan ‘dy’ menyimpan nilai lompatan setiap langkah titik vertikal dan horizontal.
Perhitungan titik koordinat garis dilakukan dengan iterasi sebanyak jumlah langkah, di setiap iterasi dilakukan penjumlahan titik x dan y dengan nilai lompatan titik x dan titik y. Hasil perhitungan setiap iterasi disimpan kedalam variabel ‘kx’ untuk nilai vertikal, dan ‘ky’ untuk nilai horizontal, nilai dibulatkan dengan menggunakan fungsi round().
Dibuat variabel ‘koor’ untuk menyimpan gabungan nilai variabel ‘kx’ dan ‘ky’ dengan menggunakan fungsi set() dan zip().
